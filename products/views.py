from rest_framework import viewsets
from rest_framework.decorators import action
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class ProductsViewset(viewsets.ViewSet):
    serializer_class = serializers.ProductSerializer

    def list(self, request):
        products = models.Products.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            product = self.get_object(pk=pk)
            serializer = serializers.ProductSerializer(product)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def create_product(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete_product(self, request, pk=None):
        try:
            product = self.get_object(pk)
            product.delete()
            return Response({"status": 'success', 'data': 'Product deleted successfully'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['patch'])
    def update_stock(self, request, pk=None):
        try:
            product = self.get_object(pk=pk)
            serializer = serializers.UpdateproductStockSerializer(
                product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                uptated_product = serializers.ProductSerializer(
                    self.get_object(pk=pk))
                return Response({"status": "success", "data": uptated_product.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": "error", "data": uptated_product.errors}, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        return models.Products.objects.get(pk=pk)
