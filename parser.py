import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_table(table, chose):
    res = ''
    if chose == "name":
        res = table.find('a').get('title').strip()
    if chose == "price":
        try:
            res = table.find('span', {'class': 'class_where_is_a_current_price'}).text.strip()
        except AttributeError:
            res = "Empty"
    return(res)

name_phone = []
price_phone = []
pages = 10
baseurl = 'https://the_website/catalog/phone_catalog/??id=%25p%3D10&p={}'
url = [baseurl.format(x) for x in range(1, pages+1)]
for i in range(0, pages):
    r = requests.get(url[i])
    with open('mytest.html', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)
    soup = BeautifulSoup(r.text)
    phonenames = soup.find_all('div', {'class': 'div_class_with_name'})
    phoneprices = soup.find_all('div', {'class': 'div_class_with_price'})
    for item in phonenames:
        name = "name"
        res = parse_table(item, name)
        name_phone.append(res)
    for item in phoneprices:
        price = "price"
        res = parse_table(item, price)
        price_phone.append(res)
result = pd.DataFrame({'model': name_phone, 'price': price_phone})
result.to_excel('myresult.xlsx')

