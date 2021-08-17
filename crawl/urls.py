from django.urls import path,include
from . import views

app_name = 'crawl'

urlpatterns = [
    path('',  views.crawl, name="home"),
    path('delete/',  views.delete),
    path('celery/',  views.celery),
    path('sendnoti/',  views.sedNoti),
]