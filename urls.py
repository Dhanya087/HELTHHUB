from django.urls import path,include
from . import views
from django.contrib import admin



urlpatterns = [
    path('', views.home),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path('products/', views.admin_product_page, name='admin_product_page'),
    path('add/', views.product_add, name='product_add'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    # path('update/<int:pk>', views.update.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('admin_login/', views.admin_login, name='admin_login'),
    # path("product-detail/<int:pk>" , views.ProductDetail.as_view(),)
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase_quantity/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('search_results/', views.search_results, name='search_results'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
   
]
 


    

