from django.shortcuts import render
from  django.http import JsonResponse
from .models import *
from .getData import *
from django.shortcuts import render
from .tasks import *
import redis


def crawl(request):
    products = Product.objects.all()
    return render(request, 'crawl.html', {"products": products})

def delete(request):
    Product.objects.all().delete()
    return JsonResponse({})

def celery(request):
    getDataCelery.delay()
    return JsonResponse({})

def sedNoti(request):
    sendNoti.delay()
    return JsonResponse({})


