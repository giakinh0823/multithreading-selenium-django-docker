from django.urls import path

from . import consumers

ws_urlpatterns = [
    path('ws/getData/', consumers.ProductsConsumer.as_asgi()),
]