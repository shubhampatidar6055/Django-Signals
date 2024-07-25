from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import Usermodelform

# Create your views here.

def index(request):
    obj=Usermodel.objects.all()
    return render(request, "table.html", {"obj":obj})

def register(request):
    form = Usermodelform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "index.html" ,{"form":form})

def update(request,id):
    model = get_object_or_404(Usermodel,id=id)
    form = Usermodelform(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "index.html" ,{"form":form})

def delete(request,id):
    model = get_object_or_404(Usermodel,id=id)
    if request.method == "POST":
        model.delete()
        return redirect("/")
    return render(request,"delete.html",{'model':model})



