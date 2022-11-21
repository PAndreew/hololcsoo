from django.conf import settings
from django.db import models
from grocery.models import Item


class ShoppingList(models.Model):
    items = models.ManyToManyField(Item, through='ShoppingListItem')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.customer.username}'s {self.nickname} list"


class ShoppingListItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} {self.item}"


