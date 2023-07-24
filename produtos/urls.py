from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_products, name="list_products"),
    path("criar/", views.create_product, name="create_product"),
]
