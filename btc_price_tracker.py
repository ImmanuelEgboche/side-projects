import time
from datetime import datetime
import requests
from pycoingecko import CoinGeckoAPI
"""
WE CANT USE A COMPARISON OPERATOR ON A DICT OBJECT SO INDEX TEH DICT AND TAKE TEH VALUE OUT THEN DO COMPARISONS """

cg = CoinGeckoAPI()
btc_threshold = 40000

def btc_price():
    btc_dict = cg.get_price(ids='bitcoin',vs_currencies='gbp')
    print('success')
    return btc_dict["bitcoin"]["gbp"]

def webhook(event, value):
    # Paylaod that'll be sent to teh IFTTT
    data = {'value1':value}
    #inserting the actual event
    url = 'https://maker.ifttt.com/trigger/test_event/with/key/nnRLHCaO-qpMRsfGFroi2VBpeWCfXuzKcn71GSYakwV'
    ifttt_url = url.format(event)
    requests.post(ifttt_url, json=data)
    print('success')

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price["date"].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price["price"]
        #These bold tags dont appear on iphone
        row = f"{date} - Current bitcoin price is {price}"
        rows.append(row)
        print('success')
    return "\n".join(rows)

#Standard command line app skeleton
def main():
    bitcoin_history = []
    while True:
        price = btc_price()
        date = datetime.now()
        bitcoin_history.append({'date':date,'price':price})
        #creating emergency warning
        if price < btc_threshold:
            webhook('btc_emergency_price',price)
        #Sending a notification
        if len(bitcoin_history) == 5:
            webhook('bitcoin price',format_bitcoin_history(bitcoin_history))
            bitcoin_history = []
        
        #Because im only allowed 1 request a minute 
        #This sleeps by seconds not minutes lol
        time.sleep(86400)
        

if __name__ == '__main__':
    main()



