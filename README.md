# multiplexer-manager package

This package is designed to allow users to manage multiplexer files and process them with a variety of functions (plotting, averaging, linear regression, etc.). So far there is only the capability to import .csv files from the PSTrace software from PalmSens B.V., but in future updates there may even be more flexibility with the multiplexer files that are compatible. 

### Installation

To install the package, enter the following into the terminal
```
pip install multiplexer-manager
```

### Importing

Import the multiplexer-manager module using:
```
import multiplexermanager as mm
```
This will give you access to the Multiplexer class as well as various data manipulation and plotting functions.


### Multiplexer class
At the core of the multiplexer-manager package is the Multiplexer class. This is a class that produces 4D numpy array objects (channels, experiments, rows, columns) using the 2D arrays (rows + columns) of a .csv file. You can pass a string containing the filename (with path) of your data as an attribute of the class. The 4D array can be accessed by specifying the .array attribute of the class instance.
```
file = 'C:/Users/User/Documents/data.csv'

data = mm.Multiplexer(file).array
```

You can also pass in the values 
```
bipot = True
``` 
or 
```
bipot = False
```
to switch between two and four columns per data set, although the default is True, and you can specify the number of channels using
```
channel = 8
```
although the default is 16.


### Data processing functions
There are a number of function availabe for manipulating data.

###### logarithm()
Call this function with your data array passed as a parameter, and it will return the array with log10 of every 2 and 4th column.

###### smooth()
Call this function with your data array passed as a parameter, and it will return the array with every 2 and 4th column smoothed with a moving average. The second function parameter decides the length of the moving average window. 

###### peakfinder()
Call this function with your data array passed as a parameter, and it will return the minimum and maximum current values for each 4th column. 



### Plotting functions
There are a number of function availabe for manipulating data.

###### compare_channels()
Call this function with your data array passed and it will plot the same channel over all experiments for every channel.

###### compare_experiments()
Call this function with your data array passed and it will plot the same experiment with all channels for every experiment.