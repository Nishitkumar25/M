import numpy as np
import pandas as pd

data = {
    'Customer': ['C_1', 'C_2', 'C_3', 'C_4', 'C_5', 'C_6', 'C_7', 'C_8', 'C_9', 'C_10'],
    'Candies (#)': [20, 16, 27, 19, 24, 22, 15, 18, 21, 16],
    'Mangoes (Kg)': [6, 3, 6, 1, 4, 1, 4, 4, 1, 2],
    'Milk Packets (#)': [2, 6, 2, 2, 2, 5, 2, 2, 4, 4],
    'Payment (Rs)': [386, 289, 393, 110, 280, 167, 271, 274, 148, 198]
}

df = pd.DataFrame(data)

A = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
C = df['Payment (Rs)'].values

dimensionality = A.shape[1]

num_vectors = A.shape[0]

rank_A = np.linalg.matrix_rank(A)

pseudo_inverse_A = np.linalg.pinv(A)
costs = pseudo_inverse_A @ C

print("Dimensionality of the vector space:", dimensionality)
print("Number of vectors in the vector space:", num_vectors)
print("Rank of Matrix A:", rank_A)
print("Cost of each product (Candies, Mangoes, Milk Packets):", costs)
