from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Product

# Create your views here.
# def index(request):
#     return HttpResponse("haii, welcome")

def allProdCat(request,c_slug=None,):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.all().filter(Category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,"category.html",{'category':c_page,'products':products})
def  proDetail(request,c_slug,Product_slug):
    try:
        product=Product.objects.get(catgory__slug=c_slug,slug=Product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product} )
