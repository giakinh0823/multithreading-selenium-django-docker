from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import datetime
from cralThread.celery import app
import threading

@shared_task(name="get_data_child")
def getDataCeleryChild():
    from .getData import data_scrap
    data_scrap()

@shared_task(name="get_data")
def getDataCelery():
    getDataCeleryChild.delay()
    return True


@shared_task(name="send_noti")
def sendNoti():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
            'noti',
            {
                'type': 'send_message',
                'message': f"Now - {datetime.datetime.now():%Y/%m/%d %H:%M:%S}",
            }
        )
    return True
