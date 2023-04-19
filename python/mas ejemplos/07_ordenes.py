from binance import Client
import pandas as pd
import datetime as dt
import mplfinance as mpl

api_key="kfOPQj229TOIG33d2dqzAV3y7Eq4bgEq99YhSxzEee3GnoOMm5MaL6uGKa7XOFIg"
api_secret="m0wkADr5hasXRM53ppTZfzXgX1Bi1mVDHzMh2TYFrLttcjujhYh1DV03GfbefTzI"
client= Client(api_key,api_secret)
price= client.get_symbol_ticker(symbol="BTCUSDT")
print(price)

asset="BTCUSDT"
start="2022.04.11"
end="2023.04.11"
timeframe="1d"
df=pd.DataFrame(client.get_historical_klines(asset,timeframe,start,end))
df=df.iloc[:,:6]
df.columns=["Date", "Open", "High", "Low", "Close", "Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index, unit="ms")
df=df.astype("float")
#print(df)

mpl.plot(df, type="candle", volume=True, mav=7)