from django.contrib import admin

from .models import Food, Grocery, Category, Price


admin.site.register(Food)
admin.site.register(Grocery)
admin.site.register(Category)
admin.site.register(Price)
