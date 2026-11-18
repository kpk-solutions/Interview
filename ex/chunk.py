import pandas as pd
import zipfile
with zipfile.ZipFile('/customers-10000.zip', 'r') as zip_ref:
    # Extract all contents to the specified directory
    zip_ref.extractall('C:/Users/pavan/work/')

print("Files extracted successfully!")

data_chunk = pd.read_csv('/customers-10000.csv', chunksize=1000)
for chunk in data_chunk:
    print(chunk.head())