import django_filters
from .models import Price, Grocery


class MyFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(lookup_expr='gt')

    class Meta:
        model = Price
        fields = ["value"]
