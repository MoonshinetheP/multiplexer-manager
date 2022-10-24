import pandas as pd
import numpy as np
import scipy as sp
from sp.scipy.stats import linregress

path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'test.csv'
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16")
ndf = df.dropna()   # removes null values (blank in excel) from the dataframe

array = ndf.to_numpy()
print(array.shape)

