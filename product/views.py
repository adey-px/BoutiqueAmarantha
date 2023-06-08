from django.shortcuts import get_object_or_404, render
from .models import Product


#
def aLLproducts(request):
    """
    View to show all products, including sorting
    and search queries
    """

    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "product/aLLproducts.html", context)


#
def productDetail(request, product_id):
    """
    View to show details for each product
    """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "product/productDetail.html", context)
