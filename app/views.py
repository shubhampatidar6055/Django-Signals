from django.shortcuts import render
from .models import *
# from .forms import Usermodelform

# Create your views here.

def index(request):
    return render(request, "index.html")