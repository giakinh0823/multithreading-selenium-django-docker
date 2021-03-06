import time
from selenium import webdriver
from .models import *
# Import packages
from selenium import webdriver  
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .models import Product
from  .tasks import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def data_scrap():
    channel_layer = get_channel_layer()
    driver = webdriver.Remote("http://selenium-hub:4444/wd/hub", DesiredCapabilities.FIREFOX)
    driver.get("https://github.com/giakinh0823?tab=repositories")
    time.sleep(2)
    htmlSource = driver.page_source
    only_class = SoupStrainer("div", {"id": "user-repositories-list"})
    list_product = BeautifulSoup(htmlSource, "html.parser", parse_only=only_class)
    for item in list_product.findAll("h3", {"class": "wb-break-all"}):
        name = str(item.find("a", attrs={"itemprop": "name codeRepository"}).text)
        async_to_sync(channel_layer.group_send)(
            'product',
            {
                'type': 'send_data_products',
                'product': name,
            }
        )
        product = Product.objects.create(name =name)
        product.save()
        time.sleep(2)
    driver.quit()


