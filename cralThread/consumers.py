import json
import math
from datetime import datetime
from decimal import Decimal
from time import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from crawl.models import Product
import random
import string
from crawl.getData import data_scrap
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import threading
from multiprocessing import Pool
from multiprocessing import Process



class ProductsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect')
        await self.accept()
        room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(room_name, self.channel_name)
        print(f"Thêm {self.channel_name} channel vào nhóm lấy dữ liệu")

    def getDataAjax(number):
        pool=Pool(10)
        pool.map_async(data_scrap,(1,2,3,4,5,6,7))
        pool.close()
        pool.join()

    async def receive(self, text_data):            
        # task = threading.Thread(target=self.getDataAjax(), args=[1])
        # task.daemon = True
        # task.start()
        process = Process(target=self.getDataAjax(), args=[1])
        process.start()

       
    async def disconnect(self, close_code):
        room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_discard(room_name, self.channel_name)
        print(f"Xóa {self.channel_name} channel từ nhóm lấy dữ liệu")