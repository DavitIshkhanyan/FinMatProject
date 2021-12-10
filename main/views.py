from django.shortcuts import render
from django.http import HttpResponse
import requests
import sched, time
from bs4 import BeautifulSoup
import schedule
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
# Create your views here.

def index(request):
    # return HttpResponse("<h4>Hello</h4>")
    return render(request, 'main/index.html')

def about(request):
    # return HttpResponse("<h4>About</h4>")
    return render(request, 'main/about.html')

price = 0
diag = 0
def priceTracker():
    global price, diag, data_loaded
    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')

    # price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].findAll('span')[3].text
    # price = soup.find_all('div', {'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].find('span').text
    price = soup.find_all('div', {'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].find('fin-streamer').text
    # obj = open('price.json', 'wb')
    # obj.write({'price': price})
    # obj.close
    data = {'price': price}
    # import json
    # with open('price.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    # with open('price.json') as data_file:
    #     data_loaded = json.load(data_file)
    # print(data_loaded)
    # print(price)

    # diag = soup.find_all('div', {'smartphone_Mt(40px)'})
    diag = soup.find_all('canvas')

    
    return price

    # while True:
    #     print('Current Price of Apple: ', priceTracker())
    #     time.sleep(60)

import io
import base64


fig = plt.figure()
ax = plt.axes()

def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())
# encoded = fig_to_base64(fig)
# encoded = fig_to_base64(1)
# my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))

def refresh(request):
    global price, diag
    # schedule.every(30).seconds.do(priceTracker)
    priceTracker()

    encoded = fig_to_base64(fig)
    my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
    # while True:
    #     schedule.run_pending()
    #     time.sleep(30)
    # schedule.run_all()
    # context = 
    # print(price)
    res = price+my_html
    return HttpResponse(res)
    # return data_loaded
    return render(request, 'main/index.html', data_loaded)
    # return render(request, 'main/index.html')



