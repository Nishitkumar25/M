import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

file_path = 'path_to_your_file/Lab Session Data.xlsx'  
df = pd.read_excel(file_path, sheet_name='Purchase data')

df['Class'] = np.where(df['Payment (Rs)'] > 200, 1, 0)  # 1 for RICH, 0 for POOR

X = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']]
y = df['Class']

classifier = LogisticRegression()
classifier.fit(*train_test_split(X, y, test_size=0.3, random_state=42)[:2])
y_pred = classifier.predict(X_test := train_test_split(X, y, test_size=0.3, random_state=42)[1])

print(f"Model Accuracy: {accuracy_score(y_test := train_test_split(X, y, test_size=0.3, random_state=42)[3], y_pred):.2%}")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=['POOR', 'RICH']))
