from django.contrib import admin
from product.models import *


# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    # list_display = ['name']
    pass

@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    pass

@admin.register(Product)
class Product(admin.ModelAdmin):
    pass

# Register your models here.
