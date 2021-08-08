import requests
from bs4 import BeautifulSoup
import gspread
import datetime
iphone12 = "https://alif.shop/telefony/iphone-12/"

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
# Connect - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-nano-simesim-ru-ru/")),"iCom")
                           https://alif.shop/telefony/iphone-12/iphone-12-pro-max-256-gb-nano-simesim-ru-ru/
# Sam - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("iphone12""iphone-12-pro-max-256-gb-nano-simesim-ru-2/")),"iCom")

# Dumarket - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-nano-simesim-ru-3/")),"iCom")
# Mobisell - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-nano-simesim-ru-4-ru/")),"iCom")
# Mobi Like - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-nano-simesim-ru-5/")),"iCom")
# TajStore - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-ru-2/")),"iCom")
# Real 2 - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-nano-simesim-ru-6-ru/")),"iCom")
# Icom - IPHONE 12 PRO MAX 128 GB (NANO-SIM+NANO-SIM)
output(parse(product_link("https://alif.shop/telefony/iphone-12-pro-max-256-gb-nano-simesim-ru-7/")),"iCom")
                           https://alif.shop/telefony/iphone-12/iphone-12-pro-max-256-gb-nano-simesim-ru-7/