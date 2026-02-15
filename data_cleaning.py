import pandas as pd
import os

# Get the directory of this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct path to data folder
csv_path = os.path.join(BASE_DIR, "..", "data", "raw_data.csv")

print("CSV path being used:")
print(csv_path)

# Read CSV
df = pd.read_csv(csv_path)

print("\nCSV loaded successfully!")
print(df.head())
print(df.info())
print(df.shape)



# 1. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Save cleaned data
output_path = os.path.join(BASE_DIR, "..", "data", "cleaned_data.csv")
df.to_csv(output_path, index=False)

print("\nCleaned data saved successfully at:")
print(output_path)