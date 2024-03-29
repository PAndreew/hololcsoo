from django.conf import settings
from django.db import models
from django.utils import timezone


class Grocery(models.Model):
    grocery_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="grocery_photos")

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
                                   blank=True,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   related_name="categories")
    product_link = models.URLField()
    photo = models.ImageField(upload_to="product_photos")
    is_vegan = models.BooleanField()
    is_cooled = models.BooleanField()
    is_local_product = models.BooleanField()
    is_bio = models.BooleanField()
    is_favorite_of = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    on_stock = models.CharField(max_length=50)
    energy = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in kJ/100g")
    protein = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in g/100g")
    fat = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in g/100g")
    carbohydrates = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in g/100g")
    fiber = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in g/100g")
    sodium = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in mg/100g")
    sugar = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="in g/100g")

    def __str__(self) -> str:
        return f"{self.name}"


class Price(models.Model):
    item = models.ForeignKey(Item, blank=False, null=False, on_delete=models.CASCADE, related_name="items")
    value = models.DecimalField(max_digits=9, decimal_places=1)
    sale_value = models.DecimalField(max_digits=9, decimal_places=1)
    unit = models.CharField(max_length=20, default="darab")
    unit_price = models.DecimalField(max_digits=9, decimal_places=1)
    timestamp = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.item.categories.sold_by.grocery_name}: {self.item.name}'s price @ {self.timestamp}"

    class Meta:
        unique_together = ('value', 'timestamp', 'item')
