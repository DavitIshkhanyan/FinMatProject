from django.shortcuts import render
from django.http import HttpResponse
import requests
import sched, time
from bs4 import BeautifulSoup
import schedule
import json
# Create your views here.

def index(request):
    # return HttpResponse("<h4>Hello</h4>")
    return render(request, 'main/index.html')

def about(request):
    # return HttpResponse("<h4>About</h4>")
    return render(request, 'main/about.html')

price = 0
def priceTracker():
    global price, data_loaded
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
    return price

    # while True:
    #     print('Current Price of Apple: ', priceTracker())
    #     time.sleep(60)
def refresh(request):
    global price
    # schedule.every(30).seconds.do(priceTracker)
    priceTracker()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(30)
    # schedule.run_all()
    # context = 
    # print(price)
    return HttpResponse(price)
    # return data_loaded
    return render(request, 'main/index.html', data_loaded)
    # return render(request, 'main/index.html')



