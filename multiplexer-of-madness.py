import pandas as pd
import numpy as np
from sympy import diff
from scipy.stats import linregress
import matplotlib as mpl
import matplotlib.pyplot as plt


'''Importing data to dataframe/array'''
#test file already saved as Log10
path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'test.csv'
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16")
ndf = df.dropna()   # removes null values (blank in excel) from the dataframe

array = ndf.to_numpy()
print(array.shape[1])
#convert to 4D array - current version is reaching correct shape, but data is in wrong place

'''Changing array shape'''
#empty = np.ones((16, int((array.shape[1])/64), int(array.shape[0]), 4))
split = np.split(array, int((array.shape[1])), axis = 1)
resplitx = np.reshape(split[2], int(array.shape[0]))
resplity = np.reshape(split[3], int(array.shape[0]))
#resplitxy = np.concatenate((resplitx, resplity), axis = 1)

'''Finding linear region'''
#Find the max and min current values for each scan
#Find indices that correlate to those values
minimum = np.min(resplity)
maximum = np.max(resplity)
range = maximum - minimum
start = maximum - (0.2 * range)
stop = minimum + (0.2 * range)
print(minimum, maximum)
start_index = 0
stop_index = 0

for x in resplity:
    if x > start:
        pass
    else:
        start_index = (np.where(resplity == x))[0][0]
        break

for y in resplity:
    if y > stop:
        pass
    else:
        stop_index = (np.where(resplity == y))[0][0]
        break

'''Linear regression'''

extraction = linregress(resplitx[start_index:stop_index], resplity[start_index:stop_index])


#print(extraction[0])
#slope = extraction[0]
#intercept = extraction[1]
#R = extraction[2]


'''Data extraction

with open('example.txt', 'w') as file:
    for x in evenafter:
        file.write(str(x) + '\n')
'''
#for x in narray[:,:,1,1]:
    #print(x[:,2:4])
    
#find region of linear of each transistor
#fit to linear region
#plot data to confirm
#use line of best fit to report
#colour map

'''Plotting data'''
x = resplitx
y = resplity
z = extraction[0]*resplitx + extraction[1]
fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

ax.plot(x, y, linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
ax.plot(resplitx[start_index : stop_index], z, linewidth = 2, linestyle = '-', color = 'blue', marker = None, label = None)
plt.show()
plt.close()