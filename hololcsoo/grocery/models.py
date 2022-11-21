from django.conf import settings
from django.db import models
from django.utils import timezone


class Grocery(models.Model):
    grocery_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "groceries"

    def __str__(self) -> str:
        return f"{self.grocery_name}"


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_id = models.CharField(max_length=20)
    sold_by = models.ForeignKey(Grocery, blank=False, null=False, on_delete=models.CASCADE, related_name="sold_by")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return f"{self.category_name}"


class Item(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ForeignKey(Category,
                                   blank=False,
                                   null=False,
                                   on_delete=models.CASCADE,
                                   related_name="categories")
    product_link = models.URLField()
    is_vegan = models.BooleanField()
    is_cooled = models.BooleanField()
    is_local_product = models.BooleanField()
    is_hungarian_product = models.BooleanField()
    is_bio = models.BooleanField()
    is_favorite_of = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    on_stock = models.BooleanField()
    on_sale = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name}"


class Price(models.Model):
    item = models.ForeignKey(Item, blank=False, null=False, on_delete=models.CASCADE, related_name="items")
    value = models.FloatField()
    sale_value = models.FloatField()
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField()
    timestamp = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.item.categories.sold_by.grocery_name}: {self.food.name}'s price @ {self.timestamp}"

    @property
    def sale_ratio(self):
        return self.sale_value/self.value - 1
