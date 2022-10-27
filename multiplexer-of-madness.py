'''MODULES'''
import csv
import pandas as pd
import numpy as np
import piecewise_regression
from scipy.stats import linregress
import matplotlib.pyplot as plt


'''Importing data to dataframe/array'''
# Open file into a Pandas dataframe
path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'data.csv'
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16", low_memory = False)
# Remove any null values from the dataframe
ndf = df.dropna()
# Convert the dataframe to an array
array = ndf.to_numpy().astype(float)

rows = array.shape[0]
channels = 16
fields = 4
length = array.shape[1]
experiments = length // (channels*fields)

'''Changing array shape'''
# Convert the 2D array given by excel into a 4D array: (channel, experiment, dataset, data)
# Note: Managed to make a 4D array, but data was placed incorrectly during reshape
# Still need to finish this, but for now, split the 2D array into 64 columns of 2D arrays and then reshaped

x_source = array[ : , 0]
y_source = np.log10(np.absolute(array[ : , 1]))
x_drain = array[ : , 2]
y_drain = np.log10(np.absolute(array[ : , 3]))

fit = piecewise_regression.Fit(x_drain, y_drain, n_breakpoints = 2)
fit.summary


'''
linx = x_drain[upper:lower]
liny = y_drain[upper:lower]


extraction = linregress(linx, liny)

z = extraction[0]*linx + extraction[1]
        
        
  
fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
ax.set_title('R =' + str(extraction[2]), loc = 'center', pad = 20, fontsize = 15)
ax.plot(x_source, y_source, linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
ax.plot(x_drain, y_drain, linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None)
ax.plot(linx, z, linewidth = 2, linestyle = '-', color = 'blue', marker = None, label = None)
plt.show()
plt.close()
'''

'''Finding linear region'''
# Find the max and min current values for each scan


# Determine the current range over which linear regression will be performed


# Find indices that correlate to this range



'''Linear regression'''




'''Plotting data'''


'''Data extraction'''
""" 
with open('example.txt', 'w') as file:
    for x in testy:
        file.write(str(x) + '\n') """


'''Colour map'''
#hi """