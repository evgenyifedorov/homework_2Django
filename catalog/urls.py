from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import index, contacts, product

app_name = CatalogConfig.name

urlpatterns = [path("", index),
               path("contacts/", contacts, name='contacts'),

               path('catalog/<int:pk>/', product, name='product'),
               ]
