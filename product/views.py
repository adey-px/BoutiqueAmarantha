from django.shortcuts import render, redirect, reverse, get_object_or_404, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Product


# All products, search & sort queries
def aLLproducts(request):
    products = Product.objects.all()
    inputNames = None
    sortParameter = None
    sortPattern = None
    categories = None

    if request.GET:
        # search products by names input in search form
        if "query" in request.GET:
            inputNames = request.GET["query"]
            if not inputNames:
                messages.error(request, "You didn't enter any name")
                return redirect(reverse("aLLproducts"))
            if inputNames:
                queryText = Q(name__icontains=inputNames) | Q(
                    description__icontains=inputNames
                )
                products = products.filter(queryText)

        # sort products by parameters thru navbar `PRODUCTS` link
        # minus '-' for a reverse value, as in 'descending'
        if "parameter" in request.GET:
            parameter = request.GET["parameter"]
            sortParameter = parameter
            if parameter == "name":
                parameter = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            
            # sort by category name in reverse order
            if parameter == 'category':
                parameter = 'category__name'

            if "pattern" in request.GET:
                sortPattern = request.GET["pattern"]
                if sortPattern == "desc":
                    parameter = f"-{parameter}"
            products = products.order_by(parameter)

        # filter products by category thru navbar `other links`
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    # vars passed in select box for products sorting
    sortParams = f"{sortParameter}_{sortPattern}"

    # export variables to template
    context = {
        "products": products,
        "inputNames": inputNames,
        "sortParams": sortParams,
        "filterCats": categories,
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
