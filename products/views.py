import datetime

from django.shortcuts import HttpResponse, render
from .models import Product, Review


# Create your views here.
def main(request):
    return  HttpResponse('Hello! Its my project')

def data(request):
    return HttpResponse(datetime.datetime.now())


def goodby(request):
    return HttpResponse('Goodby user!')


def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    return render(request, 'products/products.html', context={'products': Product.objects.all()})

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        data={
            'product': product,
            'reviews': Review.objects.filter(product=product)
        }
        return render(request, 'products/detail.html', context= data)
