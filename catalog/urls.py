from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import index, contacts, product, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", index),
    path("contacts/", contacts),
    path("base/", product, name="product_id"),
    path("products/<int:pk>", product_detail, name="product_detail"),
]
