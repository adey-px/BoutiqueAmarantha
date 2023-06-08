from django.urls import path
from .views import aLLproducts, productDetail


urlpatterns = [
    path("aLLproducts/", aLLproducts, name="aLLproducts"),
    path("product/<product_id>/", productDetail, name="productDetail"),
]
