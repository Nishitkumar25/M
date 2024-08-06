import numpy as np
import pandas as pd

file_path = 'C:\Users\apsni\Downloads\Lab Session Data.xlsx'

df = pd.read_excel(file_path, sheet_name='Purchase data')

A = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
C = df['Payment (Rs)'].values

pseudo_inverse_A = np.linalg.pinv(A)
X = pseudo_inverse_A @ C
print("Cost per product (Candies, Mangoes, Milk Packets):", X)
