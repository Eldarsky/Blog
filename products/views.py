import datetime

from django.shortcuts import HttpResponse, render, redirect
from products.forms import ProductCreateForm, ReviewCreateForm
from .models import Product, Review, Category
from  django.views.generic import  ListView, CreateView


# Create your views here.

PAGINTION_LIMIT = 1
def main(request):
    return  HttpResponse('Hello! Its my project')

def data(request):
    return HttpResponse(datetime.datetime.now())


def goodby(request):
    return HttpResponse('Goodby users!')


def main_view(request):
    return render(request, 'layouts/index.html')

class CategoriesCBV(ListView):
    model = Category
    template_name = 'categories/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'categories': self.get_queryset(),
            'user': self.request.user if not self.request.user.is_anonymous else None
        }

class ProductsCBV(ListView):
    queryset = Product.objects.all()
    template_name = 'products/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'products': kwargs['products'],
            'max_page':kwargs['max_page'],
            'users': kwargs['users']
        }
    def get(self, request, **kwargs):
        if request.method == 'GET':
            category_id = request.GET.get('category_id')
            search = request.GET.get('search')
            page = int(request.GET.get('page', 1))

            if category_id:
                products = Product.objects.filter(categories__in=[category_id])

            else:
                products = Product.objects.all()
            if search:
                products = products.filter(title__icontains=search)

            max_page = products.__len__() // PAGINTION_LIMIT

            if round(max_page) < max_page:
                max_page = round(max_page) + 1

            products = products[PAGINTION_LIMIT * (page - 1):PAGINTION_LIMIT * page]



            return render(request, self.template_name, context=self.get_context_data(
                products = products,
                users=None if request.user.is_anonymous else request.user,
                max_page=range(1, max_page + 1)

            ))


class ProductDetailCBV(ListView):
    template_name = 'products/detail.html'
    form_class = ReviewCreateForm
    model = Product
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'product':kwargs['product'],
            'reviews':kwargs['reviews'],
            'categories':kwargs ['categories'],
            'review_form':kwargs['review_form']

        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                auther_id=request.user.id,
                text=form.cleaned_data.get('text'),
                product_id=kwargs['id'],
            )
            return redirect(f'/products/{kwargs["id"]}/')

        else:
            return render(request, self.template_name, context=self.get_context_data(
                form=form,
                product=Product.objects.get(id=kwargs['id'])
            ))

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs["id"])
        reviews = Review.objects.filter(product_id=kwargs["id"])
        categories = product.categories.all()


        return render(request, self.template_name, context=self.get_context_data(
            reviews=reviews,
            categories=categories,
            product=Product.objects.get(id=kwargs['id']),
            review_form = ReviewCreateForm
        ))







class ProductsCreateCBV(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'user': self.request.user if not self.request.user.is_anonymous else None,
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rating=form.cleaned_data.get('rating')
            )
            return redirect('/products')
        else:
            return render(request, self.template_name, context=self.get_context_data(form=form))



