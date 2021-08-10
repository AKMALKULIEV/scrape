import requests
from bs4 import BeautifulSoup
import gspread
import datetime
import pandas as pd

df = pd.read_csv("dict.csv")
new_df = df.to_dict()

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


# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-ru/")),"Connect")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-2/")),"Sam")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-3/")),"Dumarket")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-4-ru/")),"Mobisell")  
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-5/")),"Mobi Like")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-ru-2/")),"TajStore")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-6-ru/")),"Real 2")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simnano-sim-ru/")),"New Mobile") 
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-ru/")),"Galaxy Dushanbe")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-ru-2/")),"City Mobile")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru/")),"Ali Store")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-4/")),"Rudaki Mobile")  
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-6/")),"Rudaki Mobile (Dom Pechati)")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-7/")),"iCom")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-ru-2/")),"Salam store")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-ru-3/")),"Boir's Mobile Sadbarg")    
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-3-ru/")),"Kalla Mobile")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-ru-ru/")),"Svyaznoy")  
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-4-ru-ru-ru-ru/")),"reStore.tj")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-4-ru-ru-ru/")),"Ok Mobile")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-4-ru-ru-2/")),"Nasha set")
# output(parse(product_link(iphone12+"iphone-12-pro-max-256-gb-nano-simesim-ru-4-ru-ru/")),"Game Shop")                        


partner_dict = {"iphone-12-pro-max-256-gb-nano-simesim-ru-ru/":"Connect","iphone-12-pro-max-256-gb-nano-simesim-ru-2/":"Sam"}
# print(partner_dict)

for key in partner_dict:
     output(parse(product_link(iphone12+key)),partner_dict[key])