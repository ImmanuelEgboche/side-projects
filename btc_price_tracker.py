import time
from datetime import datetime
import requests
from pycoingecko import CoinGeckoAPI
import psycopg2

class database: 
    def __init__(self) -> str:
        self.mydb = psycopg2.connect(
        host = 'localhost',
        user = 'root',
        password =  'password',
        database='cryptos'
        )
        print("connection success")
        autocommit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        self.mydb.set_isolation_level(autocommit)
        self.cursor = self.mydb.cursor()
    def create_database(self):
        database_name = "cryptos";
        create_db = "create database "+database_name+";"
        self.cursor.execute(create_db)
        # self.cursor.close()
        # self.mydb.close()
        print('database created')
    def creating_Tables(self):
        btc_table, eth_table, polkadot_table = "BTC", "ETH", "POLK"
        create_btc,create_eth,create_polkadot = "create table "+btc_table+"( date timestamp not null default CURRENT_TIMESTAMP, price bigint);","create table "+eth_table+"( date timestamp not null default CURRENT_TIMESTAMP, price bigint);","create table "+polkadot_table+"( date timestamp not null default CURRENT_TIMESTAMP, price bigint);"
        self.cursor.execute(create_btc)
        self.cursor.execute(create_eth)
        self.cursor.execute(create_polkadot)
        self.mydb.commit()
        # self.cursor.close()
        #self.mydb.close()
        print('tables created')
    def price_upload(self):
        btc = str(btc_price())
        eth = str(eth_price())
        polkadot = str(polkadot_price())
        btc_sql = "insert into btc values(current_date,"+btc+");"
        eth_sql = "insert into eth values(current_date,"+eth+");"
        polkadot_sql = "insert into polk values(current_date,"+polkadot+");"
        self.cursor.execute(btc_sql)
        self.cursor.execute(eth_sql)
        self.cursor.execute(polkadot_sql)
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()
        print("prices uploaded successfully")
        
cg = CoinGeckoAPI()
btc_threshold = 40000

def btc_price():
    btc_dict = cg.get_price(ids='bitcoin',vs_currencies='gbp')
    print('getting btc price...')
    return btc_dict["bitcoin"]["gbp"]

def eth_price():
    eth_dict = cg.get_price(ids='ethereum',vs_currencies='gbp')
    print('getting eth price...')
    return eth_dict["ethereum"]['gbp']

def polkadot_price():
    polkadot_dict = cg.get_price(ids='polkadot',vs_currencies='gbp')
    print("getting shiba inu price...")
    return polkadot_dict['polkadot']['gbp']
#IFTT fucntion
def webhook(event, value):
    # Paylaod that'll be sent to teh IFTTT
    data = {'value1':value}
    #inserting the actual event
    url = 'https://maker.ifttt.com/trigger/test_event/with/key/nnRLHCaO-qpMRsfGFroi2VBpeWCfXuzKcn71GSYakwV'
    ifttt_url = url.format(event)
    requests.post(ifttt_url, json=data)
    print('success')

#IFTT fucntion
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
    connection = database()
    #connection.create_database()
    connection.creating_Tables()
    connection.price_upload()
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
        time.sleep(120)

if __name__ == '__main__':
    main()




