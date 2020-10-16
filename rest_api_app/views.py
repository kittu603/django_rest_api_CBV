from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import ProductSerializer
from .models import Product


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # query in this query set
    queryset = Product.objects.all()
    # query above using this lookup field
    lookup_field = 'product_id'
    # serialize the data returned by passing to this class
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    # what to view, you can filter or other ORM funcs to see desired data
    queryset = Product.objects.all()
    # passing the returned data to serializer class to convert
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    # ask for fields from our Model taking from serializer and converts to serialized data
    serializer_class = ProductSerializer




