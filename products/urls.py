from django.urls import path
from .views import ProductsViewset

urlpatterns = [
    path('', ProductsViewset.as_view({'get': 'list'}), name='product-list'),
    path('<int:pk>/',
         ProductsViewset.as_view({'get': 'retrieve'}), name='product'),
    path('new-product/',
         ProductsViewset.as_view({'post': 'create_product'}), name='create-product'),
    path('<int:pk>/delete-product/',
         ProductsViewset.as_view({'delete': 'delete_product'}), name='delete-product'),
    path('<int:pk>/update-stock/',
         ProductsViewset.as_view({'patch': 'update_stock'}), name='delete-product'),

]
