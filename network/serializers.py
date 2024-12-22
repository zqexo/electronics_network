from rest_framework import serializers

from network.models import Network, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "model", "release_date", "network"]


class NetworkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Network.objects.all(), allow_null=True
    )

    class Meta:
        model = Network
        fields = [
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "products",
            "supplier",
            "debt",
        ]
        read_only_fields = ["debt"]  # Задолженность доступна только для чтения

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        network = Network.objects.create(**validated_data)

        for product_data in products_data:
            Product.objects.create(network=network, **product_data)

        return network
