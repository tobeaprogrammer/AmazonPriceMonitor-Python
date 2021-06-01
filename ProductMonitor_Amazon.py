# Web Scraper for amazon   |   packages : smtplib, json


from os import replace
from utilities import MailOperations
import json
from pprint import pprint
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


global data,product_name,product_price,product_url
product_name = ""
product_price = ""
product_url=""

def WebsiteOperations_FetchPrice(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    try:
        driver = webdriver.Chrome(executable_path="resources/chromedriver.exe",chrome_options=options)
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get(url)
        availability = driver.find_element_by_xpath("//div[@id='availability']/span").text
        if(availability == "In stock."):
            price = driver.find_element_by_id('priceblock_ourprice').text.replace("₹ ","").replace(',',"")
            return price
        else:
            print("Availability : " + availability)
            return "null"

    except:
        print("Failed to access Website")
    finally:
        driver.quit    

def MailTemplate(p_url,p_name,p_expectedprice,p_currentprice):
    with open("template.html", "r", encoding='utf-8') as f:
        temp_payload = f.read()
        try:
            payload = temp_payload.replace("[Name]",p_name)
            payload = payload.replace("[ePrice]",p_expectedprice)
            payload = payload.replace("[cPrice]",p_currentprice)
            payload = payload.replace("[url]",p_url)
            return payload
        except:
            raise Exception()

with open('JSON/products.json') as product_catalog:
    data = json.load(product_catalog)

for item in data['products']:
    current_price = WebsiteOperations_FetchPrice(item['url'])
    if current_price != "null":
        if float(current_price) < float(item['price']) or float(current_price) == float(item['price']):
            MailOperations.SendMail("WebScraper [~ Amazon ~] [ Price Change Notification ]",MailTemplate(item['url'],item['name'],item['price'],current_price))
        else:
            print("Product Price Not in Range.")
    else:
        print("Product availablity issue.")
