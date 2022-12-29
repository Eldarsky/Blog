import datetime

from django.shortcuts import HttpResponse, render, redirect
from products.forms import ProductCreateForm, ReviewCreateForm
from .models import Product, Review, Category


# Create your views here.
def main(request):
    return  HttpResponse('Hello! Its my project')

def data(request):
    return HttpResponse(datetime.datetime.now())


def goodby(request):
    return HttpResponse('Goodby users!')


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
            'products': products,
            'users': None if request.user.is_anonymous else request.user
        })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        data={
            'product': product,
            'reviews': Review.objects.filter(product=product),
            'categories': product.categories.all(),
            'review_form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context= data)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                product_id=id,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/products/{id}/')
        else:
            return render(request, 'products/detail.html', context={
                'product': product,
                'reviews': Review.objects.filter(product=product),
                'categories': product.categories.all(),
                'review_form': form

            })



def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)


def products_create_view(request):
    if request.method == 'GET':
        return render(request, 'products/create.html', context={
            'form': ProductCreateForm
        })

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                auther=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price', 0),
                rating=form.cleaned_data.get('rating', 0)
            )

            return redirect('/products/')
        else:
            return render(request,'products/create.html',context={
                'form':form
            })

