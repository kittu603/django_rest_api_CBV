from django.urls import path
from .views import ProductRetrieveUpdateDestroyView, ProductListView, ProductCreateView

urlpatterns = [
    path('products/<int:product_id>/', ProductRetrieveUpdateDestroyView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/new/', ProductCreateView.as_view())
]
