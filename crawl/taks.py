from __future__ import absolute_import

from celery import shared_task
from .models import *
from cralThread.celery import app

@app.task( max_retries=3)
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

@shared_task
def deleteProduct(request):
    Product.objects.all().delete()
     

