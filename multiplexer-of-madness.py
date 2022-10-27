'''MODULES'''
import pandas as pd
import numpy as np
from sympy import diff
from scipy.stats import linregress
import matplotlib.pyplot as plt


'''Importing data to dataframe/array'''
# Open file into a Pandas dataframe
path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'test.csv'
df = pd.read_csv(path + file, sep = ',', header = 6, encoding = "utf16")

# Remove any null values from the dataframe
ndf = df.dropna()

# Convert the dataframe to an array
array = ndf.to_numpy()
channels = 16
fields = 4
length = int(array.shape[1])
experiments = int(length / (channels * fields))

'''Changing array shape'''
# Convert the 2D array given by excel into a 4D array: (channel, experiment, dataset, data)
# Note: Managed to make a 4D array, but data was placed incorrectly during reshape
# Still need to finish this, but for now, split the 2D array into 64 columns of 2D arrays and then reshaped
for j in range(0, channels):
    for i in range(1, experiments + 1):
        x_source = array[ : , 4*i - 4].astype(float)
        y_source = array[ : , 4*i - 3]
        x_drain = array[ : , 4*i - 2]
        y_drain = array[ : , 4*i - 1]

        min = np.min(y_drain)
        max = np.max(y_drain)
        range = max - min
        start = max - (0.2 * range)
        stop = min + (0.2 * range)
        
        for x in y_drain:
            if x > start:
                pass
            else:
                start_index = int((np.where(y_drain == x))[0][0])
                break

        for y in y_drain:
            if y > stop:
                pass
            else:
                stop_index = int((np.where(y_drain == y))[0][0])
                break
        
        linx = np.array(x_drain[start_index:stop_index])
        liny = np.array(y_drain[start_index:stop_index])


        extraction = linregress(linx.astype(float), liny.astype(float))

        z = extraction[0]*linx + extraction[1]
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.set_title('R =' + str(extraction[2]), loc = 'center', pad = 20, fontsize = 15)
        ax.plot(x_source, y_source, linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
        ax.plot(x_drain, y_drain, linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None)
        ax.plot(linx, z, linewidth = 2, linestyle = '-', color = 'blue', marker = None, label = None)
        plt.show()
        plt.close()   

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

