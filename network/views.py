from rest_framework import filters, generics

from network.models import Network, Product
from network.serializers import NetworkSerializer, ProductSerializer
from users.permissions import IsActiveUser


class NetworkCreateView(generics.CreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NetworkListView(generics.ListCreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ["country"]
    permission_classes = [IsActiveUser]


class NetworkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActiveUser]

    def perform_update(self, serializer):
        # Запретить обновление поля `debt`
        serializer.save(debt=self.get_object().debt)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
