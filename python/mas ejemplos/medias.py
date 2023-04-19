import pandas as pd
import os


df = pd.read_csv(os.path.dirname(__file__)+"/ETHUSDT.csv")

#get the last 30 prices

last_30_prices = df["Close"].tail(30)

#calculate the mean of the last 30 prices
mean_price = last_30_prices.mean()

#calculate the standard deviation of the prices
std_price = last_30_prices.std()

#calculate the support and resistance level
suport_price= mean_price-std_price
resistance_price= mean_price+std_price

#get the last price
last_price=df["Close"].iloc[-1]

#compare the last price with the support and resitance level
if last_price>resistance_price:
    status="Resistance"
    difference=last_price-resistance_price
elif last_price<suport_price:
    status="Support"
    difference=suport_price -last_price
else:
    status="Neutral"
    difference=0

#print the result
print(f"The last price of 30 days is: ({last_price}) is {status} with a difference of {difference}")

if status=="Resistance":
    print("Sell")
elif status=="Support":
    print("Buy")
else:
    print("Hold!!!")    