import pandas as pd
import numpy as np

#select csv
def correlatin(file1, file2, name1, name2):
    vardf1 = pd.read_csv(file1).tail(30)
    vardf2 = pd.read_csv(file2).tail(30)

    #columns for study
    var_prices1 = vardf1[["Date", "Close"]]
    var_prices2 = vardf2[["Date", "Close"]]

    #fusion in a dame dataframe
    df =pd.merge(var_prices1, var_prices2, on="Date", how="inner")

    #correlation
    correlation =np.corrcoef(df["Close_x"], df["Close_y"])[0,1]
    
    #asign score for the correlation
    if correlation>0.8:
        score=10
    elif correlation>0.6:
        score=9
    elif correlation>0.4:
        score=8
    elif correlation>0.2:
        score=7
    elif correlation>0:
        score=6            
    elif correlation>-0.2:
        score=5
    elif correlation>-0.4:
        score=4
    elif correlation>-0.6:
        score=3
    elif correlation>-0.8:
        score=2
    else:
        score=1        
        
    print(f"{correlation} is the correlation, and the score between {name1} and {name2} for 30 days is:  {score}")
    
#CALLING FUNCTIONS
correlatin("BTCUSDT.csv", "ADAUSDT.csv", "BTC", "ADA")
correlatin("BTCUSDT.csv", "BNBUSDT.csv", "BTC", "BNB")
correlatin("BTCUSDT.csv", "ETHUSDT.csv", "BTC", "ETH")
correlatin("BTCUSDT.csv", "XRPUSDT.csv", "BTC", "XRP")
correlatin("sp500.csv", "gold.csv", "SP500", "GOLD")