from django.shortcuts import render, redirect, reverse, get_object_or_404, render
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product


# All products, search & sort queries
def aLLproducts(request):
    products = Product.objects.all()
    inputName = None
    sortKeyword = None
    sortPattern = None
    filterCategory = None

    if request.GET:
        # search products by names input in search form
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

        # sort products by parameters thru navbar `PRODUCTS` link
        if "parameter" in request.GET:
            sortKey = request.GET["parameter"]
            sortKeyword = sortKey
            if sortKey == "name":
                sortKey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))

            if "pattern" in request.GET:
                sortPattern = request.GET["pattern"]
                if sortPattern == "descending":
                    sortKey = f"-{sortKey}"
            products = products.order_by(sortKey)

        # filter products by category thru navbar `other links`
        if "category" in request.GET:
            filterCategory = request.GET["category"].split(",")
            products = products.filter(category__name__in=filterCategory)
            filterCategory = Category.objects.filter(name__in=filterCategory)

    sortParameter = f"{sortKeyword}_{sortPattern}"

    # export variables to template
    context = {
        "products": products,
        "searchTxt": inputName,
        "sortParam": sortParameter,
        "filterCat": filterCategory,
    }
    return render(request, "product/aLLproducts.html", context)


"""
View for Product details
"""


# Product details
def productDetail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "product/productDetail.html", context)
