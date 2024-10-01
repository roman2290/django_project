from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend






class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    # filter_backends = [BaseFilterBackend]
    # filterset_fields = ['products']
    # # при необходимости добавьте параметры фильтрации
    # def list(self, request):
    #     review =  ProductSerializer(data = request.data)
    #     if review.is_valid():
    #         review.save()
    #     return Response(review.data)


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    # filter_backends = [SearchFilter]
    # SearchFilter.search_param = 'products'
    # search_fields = ['products__title', 'products__description']
    #filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']

    # def patch(self, request, pk):
    #     sen_sor = Product.objects.get(pk=pk)
    #     seri_alizer = ProductPositionSerializer(sen_sor, data = request.data)
    #     if seri_alizer.is_valid():
    #         seri_alizer.save()
    #     return Response(seri_alizer.data)

    # def post(self, request):
    #     review = StockSerializer(data=request.data)
    #     if review.is_valid():
    #         review.save()
    #     return Response(review.data)
