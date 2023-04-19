from datetime import date, timedelta
import pandas as pd
from binance import Client
import os

today=date.today()
yesterday= today-timedelta(days=1)


def criptodata(dataticker):
    api_key = "uSexr2maDXNQx6gfGR0AbMGdIBfZs9lQ2KEBEC4qbCxJevfbRO68wn4uNci1dUOY"
    api_secret = "K1kRCyuDaqK0jvPVXeRPL59ADsFh2CIXUp71X5T3RUSRHdHC5800J5iqIymrSsdR"
    #Se saca en: https://testnet.binance.vision/
    client = Client(api_secret, api_secret)
    price = client.get_symbol_ticker(symbol=dataticker)
    print(price)
    asset= dataticker
    start ="2021.01.01"
    end=str(yesterday)
    timeframe="1d"
    df= pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
    df= df.iloc[:,:6]
    df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    df = df.set_index("Date")
    df.index = pd.to_datetime(df.index, unit="ms")
    df = df.astype("float")
    print(df)
    
    #save to csv
    df.to_csv(os.path.dirname(__file__)+"/"+dataticker+".csv", encoding='utf-8')
    print("Data Extraction finished for", dataticker, " :) ")


list = ["BTCUSDT","ETHUSDT","ADAUSDT","XRPUSDT", "BNBUSDT"]
for i in list:
    criptodata(i)