from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Grocery, Category, Food


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Food
    template_name = 'home.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Food.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

