from django.http import HttpResponse
from django.shortcuts import render
from . models import item,books
# Create your views here.
def fun(request):
    o=item.objects.all()
    ob= books.objects.all()
    return render(request,"index.html",{'r':o,'b':ob})
def car(request):
    item1=int(request.POST["item1"])
    item2 = int(request.POST["item2"])
    total=item1+item2
    return render(request,"cart.html",{"total":total})