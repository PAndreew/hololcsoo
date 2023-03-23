from .models import Grocery, Category, Item, Price
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer

class SearchView(APIView):
    def get_items_and_prices(self, request, format=None):
        query = request.query_params.get('q', '')
        products = Item.objects.filter(name__icontains=query)
        serializer = ItemSerializer(products.order_by('price__value'), many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
