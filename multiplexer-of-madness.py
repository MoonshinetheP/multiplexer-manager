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
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16")

# Remove any null values from the dataframe
ndf = df.dropna()

# Convert the dataframe to an array
array = ndf.to_numpy()

print(array.shape)
'''Changing array shape'''
# Convert the 2D array given by excel into a 4D array: (channel, experiment, dataset, data)
# Note: Managed to make a 4D array, but data was placed incorrectly during reshape
# Still need to finish this, but for now, split the 2D array into 64 columns of 2D arrays and then reshaped
split = np.split(array, int((array.shape[1])), axis = 1)
resplitx = np.reshape(split[14], int(array.shape[0]))
resplity = np.reshape(split[15], int(array.shape[0]))


'''Finding linear region'''
# Find the max and min current values for each scan
min = np.min(resplity)
max = np.max(resplity)

# Determine the current range over which linear regression will be performed
range = max - min
start = max - (0.2 * range)
stop = min + (0.2 * range)

# Find indices that correlate to this range
for x in resplity:
    if x > start:
        pass
    else:
        start_index = int((np.where(resplity == x))[0][0])
        break

for y in resplity:
    if y > stop:
        pass
    else:
        stop_index = int((np.where(resplity == y))[0][0])
        break


'''Linear regression'''
print(type(start_index), start_index, type(stop_index), stop_index)
testx = np.array(resplitx[start_index:stop_index])
testy = np.array(resplity[start_index:stop_index])
print(type(array))
#data = np.stack(testx, testy)
extraction = linregress(testx.astype(float), testy.astype(float))


'''Plotting data'''
x = resplitx
y = resplity
z = extraction[0]*testx + extraction[1]
fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
ax.set_title('R =' + str(extraction[2]), loc = 'center', pad = 20, fontsize = 15)
ax.plot(x, y, linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
ax.plot(testx, z, linewidth = 2, linestyle = '-', color = 'blue', marker = None, label = None)
plt.show()
plt.close()


'''Data extraction'''

with open('example.txt', 'w') as file:
    for x in testy:
        file.write(str(x) + '\n')


'''Colour map'''