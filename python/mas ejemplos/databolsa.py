import yfinance as yf
import pandas as pd
import json, requests, csv

def sp500():
    sp500df= yf.Ticker("^GSPC").history(period="1y")   
    print(sp500df)
    sp500df.to_csv("sp500.csv")
    print("SP500 csv extraction Finished :)")

def golddata():
    golddata= yf.Ticker("GC=F").history(period="1y")   
    print(golddata)
    golddata.to_csv("gold.csv")
    print("Gold csv extraction Finished :)")

sp500()
golddata()

gold = json.loads(requests.get("https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD").text)
data = gold[0]
dataextract = data["spreadProfilePrices"]
dataextract = dataextract[0]["ask"]
print("Data:")
print(dataextract)
f = open ('goldrealtime.csv','w')
f.write(str(dataextract))
f.close()
print("Gold real time csv extraction Finished :)")