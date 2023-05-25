import pandas as pd
import os

# save filepath to variable for easier access
melbourne_file_path = os.path.dirname(__file__)+'\input\melb_data.csv'
print(melbourne_file_path)
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()
print(melbourne_data)