from time import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from crawl.getData import data_scrap
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import threading
import json
from crawl.models import Product
import asyncio
from asgiref.sync import sync_to_async


class ProductsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect')
        await self.accept()
        await self.channel_layer.group_add("product", self.channel_name)
        print(f"Kết nối vào {self.channel_name}")

    async def receive(self, text_data): 
        pass
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("product", self.channel_name)
        print(f"Thoát khỏi {self.channel_name}")

    async def send_data_products(self, event):
        await self.send(text_data=json.dumps({
            'product': event['product']
        }))

    async def send_error_products(self, event):
        await self.send(text_data=json.dumps({
            'error': event['error']
        }))
        


