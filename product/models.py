from typing import Tuple

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.db.models import Model
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # image = models.ImageField(blank=True, upload_to='home/static/img/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='home/static/img/')
    price = models.FloatField()
    amount = models.IntegerField()
    minimum_amount = models.IntegerField(default=1)
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src= "{}" height="50"/>'.format(self.image.url))

    # image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='home/static/img/')

    def __str__(self):
        return self.title
