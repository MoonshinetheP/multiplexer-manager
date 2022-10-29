'''MODULES'''
import pandas as pd
import numpy as np


class Multiplexer:
    '''Takes the .csv filepath as an input and returns a 4D array with data organised 
    by channel, experiment number, columns, and rows'''
    def __init__(self, filepath = '', bipot = True, channels = 16):

        self.filepath = filepath
        self.bipot = bipot
        self.experiments = experiments
        self.channels = channels

        
        dataframe = pd.read_csv(filepath, sep = ',', header = 5, encoding = "utf16", low_memory = False)
        newdataframe = dataframe.dropna()
        array = newdataframe.to_numpy().astype(float)


        if bipot == True:
            fields = 4
        else:
            fields = 2
        
        rows = array.size[0]
        experiments = array.size[1] / (channels * fields)
        
        newarray = np.empty((channels,experiments,fields,rows))

        for x in range(1, channels + 1):
            for y in range(1,experiments + 1):
                for z in range(1,fields + 1):
                    newarray[x,y,z,:] = array[:,z+(experiments*y)+(fields*x)]
        
        return newarray    