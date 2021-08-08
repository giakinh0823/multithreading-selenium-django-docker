import time
from selenium import webdriver
from .models import *
# Import packages
import pandas as pd
from selenium import webdriver  
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def data_scrap(number):
    driver = webdriver.Remote("http://selenium-hub:4444/wd/hub", DesiredCapabilities.FIREFOX)
    driver.get("https://github.com/giakinh0823?tab=repositories")
    time.sleep(2)
    htmlSource = driver.page_source
    only_class = SoupStrainer("div", {"id": "user-repositories-list"})
    list_product = BeautifulSoup(htmlSource, "html.parser", parse_only=only_class)
    for item in list_product.findAll("h3", {"class": "wb-break-all"}):
        name = str(item.find("a", attrs={"itemprop": "name codeRepository"}).text)
        print(name)
        time.sleep(3)
    driver.quit()
