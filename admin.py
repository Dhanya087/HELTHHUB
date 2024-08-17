from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
     list_display = ('title','price','description')

# Register your models here.

admin.site.register(Product)
# admin.site.register(Offer,OfferAdmin)

