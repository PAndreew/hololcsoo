from django.contrib import admin

from .models import ShoppingListItem, ShoppingList


admin.site.register(ShoppingListItem)
admin.site.register(ShoppingList)
