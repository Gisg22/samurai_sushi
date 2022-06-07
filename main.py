from bs4 import BeautifulSoup
import requests
from itertools import groupby
import os
import json


def get_sushi(url):
    global about_product
    data_products = []
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    for i in range(0, 18):
        req = requests.get(url + f'?PAGEN_4={i}')
        scr = req.text
        if not os.path.exists('sushi_data'):
            os.mkdir('sushi_data')
        with open(f'sushi_data/sushi_{i}.html', 'w', encoding='utf-8') as file:
            file.write(scr)
        soup = BeautifulSoup(scr, 'lxml')
        products = soup.find_all('div', class_='tovar')
        for item in products:
            about_product = soup.find_all('div', class_='about')
        for item in about_product:
            about_product.remove(item)
            title_product = item.find_next('div', class_='title').text
            price_product = item.find_next('span', class_='price').find('span').text
            description_product = item.find_next('p').text
            data = {
                'Name': title_product,
                'Price': price_product,
                'Description': description_product
            }
            data_products.append(data)
        with open('data_products.json', 'w', encoding='utf-8') as file:
            json.dump(data_products, file, indent=4, ensure_ascii=False)



def main():
    get_sushi('https://www.samurai-sushi.kz/menu/sushi/')


if __name__ == '__main__':
    main()
