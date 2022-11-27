from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("search/is_bio/", views.FilterBioProductsView.as_view(), name="bio_results"),
    path("", views.HomePageView.as_view(), name="home"),
]