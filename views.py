
# from pyexpat.errors import messages
from multiprocessing import AuthenticationError
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import reverse_lazy
from django.views import View
from .models import Product
from .models import CartItem
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect



def home(request):
    products= Product.objects.all()
    return render(request,"app/home.html",{'products': products})


def about(request):
   return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def admin_product_page(request):
    products = Product.objects.all()
    return render(request, 'admin_product_page.html', {'products': products})



def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_page')  # Redirect to a success page after adding the product
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_page')  # Redirect to the product detail page after updating
    else:
        form = ProductUpdateForm(instance=product)
    return render(request, 'update_product.html', {'form':form, 'product':product})


    
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_product_page')  # Redirect to the product list page after deletion
    return render(request, 'delete_product.html', {'product': product})



def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_superuser:
                auth_login(request, user)
                return redirect('admin_product_page')
            else:
                return render(request, 'admin_login.html', {'form': form, 'error_message': 'Invalid credentials'})

    else:
        form = AuthenticationError()

    return render(request, 'admin_login.html', {'form': form})



# def product_details(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_details.html', {'product': product})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/product_details.html', {'product': product})



# views.py


def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(prodect_name__icontains=query)
    return render(request, 'search_results.html', {'products': products})




def add_to_cart(request, id):
    prod = get_object_or_404(Product, id=id)
    cart_item, created = CartItem.objects.get_or_create(product=prod, user=request.user)
    if not created and cart_item.quantity < prod.net_quantity:
        cart_item.quantity += 1
        cart_item.save()
        return redirect('view_cart')

    else:
        messages.error(request, "Item out of stock, please try later.")
        return redirect('view_cart')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([item.product.price * item.quantity for item in cart_items])
    return render(request, 'app/viewcart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, id):
    prod = get_object_or_404(Product, id=id)
    cart_item = get_object_or_404(CartItem, product=prod, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

# views.py
def increase_quantity(request, id):
    cart_item = get_object_or_404(CartItem, product_id=id, user=request.user)
    if cart_item.quantity < cart_item.product.net_quantity:
        cart_item.quantity += 1
        cart_item.save()
        return redirect('view_cart')
    else:
        messages.error(request, "Item out of stock, please try later.")
        return redirect('view_cart')

def decrease_quantity(request, id):
    cart_item = get_object_or_404(CartItem, product_id=id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('view_cart')

# views.py
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([item.product.price * item.quantity for item in cart_items])
    return render(request, 'app/checkout.html', {'cart_items': cart_items, 'total': total})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})