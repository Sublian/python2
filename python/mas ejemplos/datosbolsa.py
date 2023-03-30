import yfinance as yf
import pandas as pd
import json, requests

    
def sp500():
    sp500df = yf.Ticker("^GSPC").history(period="1y")
    sp500df.to_csv("sp500.csv")
    print(sp500df)
    print("Extraction finished for sp500")

def gold():
    goldf = yf.Ticker("GC=F").history(period="1y")
    goldf.to_csv("gold1.csv")
    print(goldf)
    print("Extraction finished for Gold")
    
    
sp500()
gold()

gold = json.loads(requests.get("https://forest-data-feed.swissquote.com/public-quotes/bbquotes/instrument/XAU/USD").text)
data = gold[0]
dataclean= data["spreadProfilePrices"]
datafinish = dataclean[0]["ask"]
print(str(datafinish))


