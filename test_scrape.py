import requests
from bs4 import BeautifulSoup
import gspread
import datetime

def bezos():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = 'https://alif.shop/telefony/iphone-12/iphone-12-pro-max-256-gb-nano-sim-esim/'
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

def output(product):
    gc = gspread.service_account(filename='secretclient.json')
    sh = gc.open('test').sheet1
    sh.append_row([str(product['date']), str(product['name']), str(product['price']), 'Bezos.shop'])
    return

data = bezos()
product = parse(data)
output(product)

def icom():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = 'https://alif.shop/telefony/iphone-12/iphone-12-pro-max-128-gb-nano-simnano-sim-ru-4/'
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

def output(product):
    gc = gspread.service_account(filename='secretclient.json')
    sh = gc.open('test').sheet1
    sh.append_row([str(product['date']), str(product['name']), str(product['price']), 'iCom'])
    return

data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)
data = icom()
product = parse(data)
output(product)