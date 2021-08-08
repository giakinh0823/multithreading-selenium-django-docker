from django.urls import path

from . import consumers

ws_urlpatterns = [
    path('ws/getData/<str:room_name>/', consumers.ProductsConsumer.as_asgi()),
]