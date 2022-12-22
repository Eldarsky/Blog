from django.db import models



class Category(models.Model):
    title = models.CharField('Категория', max_length= 55)
class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.FloatField()
    photo = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null= True, related_name='review')
    text = models.TextField()
    create_up = models.DateField(auto_now=True)