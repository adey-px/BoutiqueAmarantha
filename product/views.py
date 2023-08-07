from django.shortcuts import render, redirect, reverse, get_object_or_404, render
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product


# All products, search & sort queries
def aLLproducts(request):
    products = Product.objects.all()
    inputName = None
    selectedCategory = None

    # search by input name in search form
    if request.GET:
        if "query" in request.GET:
            inputName = request.GET["query"]
            if not inputName:
                messages.error(request, "You didn't enter any name")
                return redirect(reverse("aLLproducts"))
            if inputName:
                queryText = Q(name__icontains=inputName) | Q(
                    description__icontains=inputName
                )
                products = products.filter(queryText)

        # search by category in navbar items
        if "category" in request.GET:
            selectedCategory = request.GET["category"].split(",")
            products = products.filter(category__name__in=selectedCategory)
            selectedCategory = Category.objects.filter(name__in=selectedCategory)

    context = {
        "products": products,
        "searchBy": inputName,
        "sortedBy": selectedCategory,
    }
    return render(request, "product/aLLproducts.html", context)


# Product details
def productDetail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "product/productDetail.html", context)
