from django.urls import path

from network import views
from network.apps import NetworkConfig

app_name = NetworkConfig.name

urlpatterns = [
    path("network/", views.NetworkListView.as_view(), name="network-list"),
    path("create/", views.NetworkCreateView.as_view(), name="network-create"),
    path(
        "<int:pk>/",
        views.NetworkRetrieveUpdateDestroyView.as_view(),
        name="network-detail",
    ),
    path(
        "products/", views.ProductListCreateView.as_view(), name="product-list-create"
    ),
    path(
        "products/<int:pk>/",
        views.ProductRetrieveUpdateDestroyView.as_view(),
        name="product-detail",
    ),
]
