from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """
    View that renders index template
    """
    return render(request, "home/index.html")
