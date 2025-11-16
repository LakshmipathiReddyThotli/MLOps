import os
import pandas as pd


data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

# Create data directory
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Generate the file_path 
file_path = os.path.join(data_dir, 'sample.csv')

# Write data to csv file 
df.to_csv(file_path, index=False)

print(f"csv file is save to {file_path}")