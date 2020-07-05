import pandas as pd
path =""
df = pd.read_csv(path+ "stock_data.csv", header=None, names=["tickers","eps","revenue","price","people"])
# to read only two rows
#df = pd.read_csv(path+ "stock_data.csv", header=None, names=["tickers","eps","revenue","price","people"], nrows=2) 
print(df)