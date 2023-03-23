from rest_framework import serializers
from .models import Grocery, Category, Item, Price


class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ['id', 'grocery_name', 'photo']


class CategorySerializer(serializers.ModelSerializer):
    sold_by = GrocerySerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_id', 'sold_by']


class ItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True)
    is_favorite_of = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'categories', 'product_link', 'photo', 'is_vegan', 'is_cooled', 'is_local_product', 'is_bio', 'is_favorite_of', 'on_stock']


class PriceSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Price
        fields = ['id', 'item', 'value', 'sale_value', 'unit', 'unit_price', 'timestamp']
