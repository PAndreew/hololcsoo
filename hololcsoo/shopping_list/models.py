from django.conf import settings
from django.db import models
from grocery.models import Food


class ShoppingList(models.Model):
    items = models.ManyToManyField(Food, through='ShoppingListItem')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.customer.username}'s {self.nickname} list"


class ShoppingListItem(models.Model):
    item = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} {self.item}"


