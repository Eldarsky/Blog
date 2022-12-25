# Generated by Django 4.1.4 on 2022-12-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_remove_product_heashtegs_delete_heashtec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=55, verbose_name='Категория'),
        ),
    ]