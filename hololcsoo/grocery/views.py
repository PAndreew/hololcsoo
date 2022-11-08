from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Grocery, Category, Food, Price


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Price
    template_name = 'home.html'
    ordering = ['-value']

    def get_queryset(self):
        query = self.request.GET.get("q")
        day_of_newest_data = Price.objects.latest('timestamp').timestamp.day
        price_list = Price.objects.filter(
            Q(food__name__icontains=query) | Q(timestamp__day=day_of_newest_data)
        ).order_by('value')
        return price_list
