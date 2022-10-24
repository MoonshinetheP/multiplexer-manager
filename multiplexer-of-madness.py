import pandas as pd
import numpy as np

path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'test.csv'
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16")
df.dropna(axis = 'rows')
print(df)

