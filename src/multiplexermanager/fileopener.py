'''MODULES'''
import pandas as pd
import numpy as np

import operations as op
import plotting as plot
import FETs as fet



class Multiplexer:
    '''Takes the .csv file from PSTrace as an input and returns a 4D array 
    with data organised by channel, experiment number, columns, and rows'''
    def __init__(self, filepath = '', bipot = True, channels = 16):

        self.filepath = filepath
        self.bipot = bipot
        self.channels = channels

      
        dataframe = pd.read_csv(self.filepath, sep = ',', header = 5, encoding = "utf16", low_memory = False)
        newdataframe = dataframe.dropna()
        array = newdataframe.to_numpy().astype(float)


        if self.bipot == True:
            fields = 4
        else:
            fields = 2
        
        rows = array.shape[0]
        experiments = array.shape[1] // (self.channels * fields)
        
        newarray = np.empty((self.channels,experiments,fields,rows))

        for x,y,z in np.ndindex((channels,experiments,fields)):
            newarray[x,y,z,:] = array[:,(z+(channels*y)+(fields*x))]
        
        self.array = newarray

if __name__ == '__main__':
    file = 'C:/Users/SLinf/Documents/GitHub/multiplexer-manager/src/multiplexermanager/20221017_1400_PBSpH7 ozoncleaner.csv'
    instance = Multiplexer(file, bipot = True, channels = 16)
    data = instance.array
    plot.compare_channels(data)
    #logged = op.logarithm(data)
    #fet.piecewise(logged)
    pass
   