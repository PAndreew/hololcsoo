from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django_filters.views import FilterView

from .models import Grocery, Category, Item, Price


class HomePageView(TemplateView):
    template_name = 'home-03-green.html'


class SearchResultsView(ListView):
    model = Price
    template_name = 'home-03-green.html'
    ordering = ['-value']

    def get_queryset(self):
        query = self.request.GET.get("q")
        day_of_newest_data = Price.objects.latest('timestamp').timestamp.day
        price_list = Price.objects.filter(
            Q(item__name__icontains=query) & Q(timestamp__day=day_of_newest_data)
            # Q(item__name__icontains=query)
        ).order_by('value')
        return price_list


class FilterBioProductsView(ListView):
    model = Price
    template_name = 'home-03-green.html'
    ordering = ['-value']

    def get_queryset(self):
        query = self.request.GET.get("q")
        day_of_newest_data = Price.objects.latest('timestamp').timestamp.minute
        bio_price_list = Price.objects.filter(
            Q(item__name__icontains=query) & Q(timestamp__day=day_of_newest_data) & Q(item__is_bio=True)
            # Q(item__name__icontains=query)
        ).order_by('value')
        return bio_price_list
