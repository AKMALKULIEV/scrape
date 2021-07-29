import requests
from bs4 import BeautifulSoup
import gspread
import datetime

def request():
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
    brand_name = soup.find('a', href = 'https://alif.shop/bezos/')
    product = {'date':date, 'name':name, 'price':price, ' brand_name':  brand_name}
    return product

def output(product):
    gc = gspread.service_account(filename='secretclient.json')
    sh = gc.open('test').sheet1
    sh.append_row([str(product['date']), str(product['name']), str(product['price']), str(product[' brand_name'])])
    return

data = request()
product = parse(data)
output(product)