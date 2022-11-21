from django.contrib import admin

from .models import Item, Grocery, Category, Price


admin.site.register(Item)
admin.site.register(Grocery)
admin.site.register(Category)
admin.site.register(Price)
