from django.db import models


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


class Food(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE,
                                   related_name="categories")
    price = models.FloatField()
    product_link = models.URLField()
    is_vegan = models.BooleanField()
    is_cooled = models.BooleanField()
    is_local_product = models.BooleanField()
    is_hungarian_product = models.BooleanField()
    is_bio = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name}"


class Price(models.Model):
    food = models.ForeignKey(Food, blank=False, null=False, on_delete=models.CASCADE, related_name="foods")
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField()
    timestamp = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.food.name}'s price @ {self.timestamp}"


