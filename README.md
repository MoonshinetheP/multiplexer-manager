# multiplexer-manager package

This package is designed to allow users to manage multiplexer files and process them with a variety of functions (plotting, averaging, linear regression, etc.). So far there is only the capability to import .csv files from the PSTrace software from PalmSens B.V., but in future updates there will be functions that can be applied to the data and there may even be more flexibility with the multiplexer files that are compatible. 

### Installation

To install the package, enter the following into the terminal
```
pip install multiplexer-manager
```

### Use

At the beginning of your code, import the multiplexer-manager module
```
import multiplexer-manager as mm
```

Using a string containing the filename (with path) of your data, call an instance of the Multiplexer class
```
file = 'C:/Users/User/Documents/data.csv'

conversion = mm.Multiplexer(file)
```

You can also pass in 
```
bipot = True
``` 
or 
```
bipot = False
```
to switch between two and four columns per data set.

Convert your file to a 4D numpy array using the following line
```
array = conversion.open()
```

This should give you your data in a form that allows easier processing.