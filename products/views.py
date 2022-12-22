import datetime

from django.shortcuts import HttpResponse, render
from .models import Product, Review, Category


# Create your views here.
def main(request):
    return  HttpResponse('Hello! Its my project')

def data(request):
    return HttpResponse(datetime.datetime.now())


def goodby(request):
    return HttpResponse('Goodby user!')


def main_view(request):
    return render(request, 'layouts/index.html')

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)

def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])

        else:
            products = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': products
        })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        data={
            'product': product,
            'reviews': Review.objects.filter(product=product),
            'categories': product.categories.all()
        }
        return render(request, 'products/detail.html', context= data)



def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)
