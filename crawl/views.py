from django.shortcuts import render
from  django.http import JsonResponse
from .models import *
from .getData import *
from django.shortcuts import render
import threading
from .tasks import *
from datetime import datetime, timedelta



def crawl(request):
    products = getProduct(request)
    return render(request, 'crawl.html', {"products": products})

def getDataAjax(request):
    if request.is_ajax():
        data_scrap()

def getData(request):
    thread = threading.Thread(target=getDataAjax,args=[request])
    thread.daemon = True
    thread.start()
    thread.join()

def delete(request):
    deleteProduct.delay()
    return JsonResponse({})

def celery(request):
    getDataCelery.delay()
    return JsonResponse({})


