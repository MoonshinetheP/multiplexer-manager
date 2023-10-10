'''
===================================================================================================
Copyright (C) 2023 Steven Linfield

This file is part of the multiplexer-manager package. This package is free software: you can 
redistribute it and/or modify it under the terms of the GNU General Public License as published 
by the Free Software Foundation, either version 3 of the License, or (at your option) any later 
version. This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details. You should have received a copy of the GNU General 
Public License along with electrochemistry-simulations. If not, see https://www.gnu.org/licenses/
===================================================================================================

Package title:      multiplexer-manager
Repository:         https://github.com/MoonshinetheP/multiplexer-manager
Date of creation:   03/11/2022
Main author:        Steven Linfield (MoonshinetheP)
Collaborators:      None
Acknowledgements:   None
    
Filename:           fileopener.py

===================================================================================================
How to use this file:
    
    1. Scroll down to the section titled 'OPENING MULTIPLEXED FILES FROM MAIN'
===================================================================================================
'''

'''MODULES'''
import sys
import os
import time
from errno import EEXIST
from tkinter import filedialog
import pandas as pd
import numpy as np

'''FILE OPENER CLASS'''
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


'''OPENING MULTIPLEXED FILES FROM MAIN'''

if __name__ == '__main__':
    
    '''2. DEFINE THE START TIME'''
    start = time.time()

    '''1. MAKE A /DATA FOLDER'''
    cwd = os.getcwd()    
    try:
        os.makedirs(cwd + '/data')
    except OSError as exc:
        if exc.errno == EEXIST and os.path.isdir(cwd + '/data'):
            pass
        else: 
            raise
    
    '''1. MAKE A /DATA FOLDER'''
    filename = filedialog.askopenfile()
    instance = Multiplexer(filename, bipot = True, channels = 16)
    data = instance.array

    '''2. DEFINE THE START TIME'''
    start = time.time()
   