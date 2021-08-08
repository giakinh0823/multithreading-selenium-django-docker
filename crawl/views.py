from django.shortcuts import render
from  django.http import JsonResponse
from .models import *
from .getData import *
from multiprocessing import Pool
from django.shortcuts import render,redirect
import threading
import random
import string
from multiprocessing import Process



def crawl(request):
    return render(request, 'crawl.html')

def getDataAjax(request):
    if request.is_ajax():
        pool=Pool(10)
        pool.map_async(data_scrap,(1,2,3,4,5,6,7))
        pool.close()
        pool.join()

def getData(request):
    task = threading.Thread(target=getDataAjax,args=[request])
    task.daemon = True
    task.start()
    # process = Process(target=getDataAjax, args=[request])
    # process.start()
    return JsonResponse({})