import pandas as pd
import numpy as np
from sympy import diff
from scipy.stats import linregress
import matplotlib as mpl
import matplotlib.pyplot as plt

#test file already saved as Log10
path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'test.csv'
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16")
ndf = df.dropna()   # removes null values (blank in excel) from the dataframe

array = ndf.to_numpy()

#convert to 4D array - current version is reaching correct shape, but data is in wrong place
narray= np.reshape(array, (16, int((array.shape[1])/64), int(array.shape[0]), 4))
print(narray.ndim, narray.size, narray.shape)
new = narray[0,0,:,:]
#print((new[:,0:1]).size)

#for x in narray[:,:,1,1]:
    #print(x[:,2:4])
    
#find region of linear of each transistor
#fit to linear region
#plot data to confirm
#use line of best fit to report
#colour map


'''Plotting'''
x = new[1:,2]
y = new[1:,3]

fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

ax.plot(x, y, linewidth = 2, linestyle = '-', color = 'green', marker = None, label = None)

#plt.show()
plt.close()