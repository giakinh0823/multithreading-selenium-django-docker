from django.shortcuts import render
from  django.http import JsonResponse
from .models import *
from .getData import *
from django.shortcuts import render
import threading
from .taks import *


def crawl(request):
    products = getProduct(request)
    return render(request, 'crawl.html', {"products": products})

def getDataAjax(request):
    if request.is_ajax():
        data_scrap()

def getData(request):
    if(threading.activeCount()<13):
        thread = threading.Thread(target=getDataAjax,args=[request])
        thread.daemon = True
        thread.start()
        thread.join()
        return JsonResponse({"Trạng thái": "Thành công! Loading"})
    return JsonResponse({"Trạng thái": "Lỗi! Phải đợi để tiếp tục"})

def delete(request):
    deleteProduct(request)
    return JsonResponse({})

def celery(request):
    getDataCelery.delay()
    return JsonResponse({})


