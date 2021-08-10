# ce/taks.py
# Create your tasks here
from celery import shared_task
from .models import *
from cralThread.celery import *

@app.task
def getDataCelery(request):
    from .getData import data_scrap
    import threading
    thread = threading.Thread(name='getdata',target=data_scrap)
    thread.daemon = True
    thread.start()    
    return True

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
     

