from django.contrib import admin
from products.models import *

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)
# Register your models here.
