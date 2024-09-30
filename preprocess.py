import pandas as pd
import numpy as np  
import os

# Set the current working directory
root = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(root, 'datasets/financial_transaction_data.csv')

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file)

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:\n", df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Check if there are any missing values
if df.isnull().values.any():
    df.dropna(inplace=True)
    print("\nAfter dropping missing values, dataset shape:", df.shape)