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


    def getDataAjax(self,number):
        data_scrap()

    async def receive(self, text_data): 
        count_thread = 0 
        for thread in threading.enumerate():
            if thread.name == "getdata":
                count_thread+=1
        if(count_thread<10):
            thread = threading.Thread(name='getdata',target=self.getDataAjax, args=[1])
            thread.daemon = True
            thread.start()
            await self.send(text_data=json.dumps({
                "Trạng thái": "Thành công! Bắt đầu lấy dữ liệu"
            }))
        else:
            await self.send(text_data=json.dumps({
                 "Trạng thái": "Lỗi! Phải đợi để tiếp tục"
            }))
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("product", self.channel_name)
        print(f"Thoát khỏi {self.channel_name}")

    async def send_data_products(self, event):
        await self.send(text_data=json.dumps({
            'product': event['product']
        }))


