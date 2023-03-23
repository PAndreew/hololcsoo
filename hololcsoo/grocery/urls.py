from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, SearchView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/search/', SearchView.as_view()),
    # add authentication URLs here, e.g. using Django REST Framework's built-in views
]
