from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import datetime

@shared_task(name="get_data")
def getDataCelery():
    from .getData import data_scrap
    data_scrap()

@shared_task(name="get_product")
def getProduct(request):
    products = Product.objects.all()
    return products

@shared_task(name="save_product")
def saveProduct(name):
    product = Product.objects.create(name =name)
    product.save()
    return True

@shared_task(name="delete_product")
def deleteProduct():
    Product.objects.all().delete()
    return True
     

@shared_task(name="send_noti")
def sendNoti():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
            'noti',
            {
                'type': 'send_message',
                'message': f"{datetime.datetime.now():%Y/%m/%d %H:%M:%S}",
            }
        )
    return True
