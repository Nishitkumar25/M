import pandas as pd
import numpy as np

file_path = 'C:\Users\apsni\Downloads\Lab Session Data.xlsx'

stock_data= pd.read_excel(file_path, sheet_name = "IRCTC Stock Price")

prices = stock_data.iloc[:3]