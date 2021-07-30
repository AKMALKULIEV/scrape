import requests
from bs4 import BeautifulSoup
import gspread
import datetime


def product_link(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = link
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def parse(soup):
    date = datetime.datetime.now()
    name = soup.find('h1').text.strip()
    price = soup.find('span', class_ = 'ty-price-num')
    shop = soup.find("head").find("title")
    brand_name = soup.find_all('span', class_="ty-control-group__label")
    product = {'date':date, 'name':name, 'price':price, ' brand_name':  "smart"}
    return product

def output(product, partner_name):
    gc = gspread.service_account(filename='secretclient.json')
    sh = gc.open('test').sheet1
    sh.append_row([str(product['date']), str(product['name']), str(product['price']), partner_name])
    return
# Icom - iPhone 11 64 Gb
data = product_link("https://alif.shop/phone/iphone/iphone-11-64-gb-ru-7/")
product = parse(data)
output(product,"iCom")

# Icom - IPHONE 12 PRO MAX 256 GB (NANO-SIM+ESIM)
data = product_link("https://alif.shop/phone/iphone/iphone-12-pro-max-256-gb-nano-simesim-ru-7/")
product = parse(data)
output(product,"iCom")

# Icom - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
data = product_link("https://alif.shop/telefony/iphone-12/iphone-12-pro-max-128-gb-nano-simnano-sim-ru-4/")
product = parse(data)
output(product,"iCom")

