from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *

@shared_task
def getDataCelery():
    from .getData import data_scrap
    data_scrap()


@shared_task
def getProduct(request):
    products = Product.objects.all()
    return products

@shared_task
def saveProduct(name):
    product = Product.objects.create(name =name)
    product.save()
    return True

@shared_task
def deleteProduct():
    Product.objects.all().delete()
    return True
     

