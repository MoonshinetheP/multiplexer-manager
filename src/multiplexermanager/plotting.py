"""Modules"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf


"""Font Settings"""
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20


def compare_channels(input):
    for ix in range(0, input.shape[0]):    
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.set_title('Channel ' + str(ix + 1), loc = 'center', pad = 20, fontsize = 15)
        
        for iy in range(0, input.shape[1]):
            ax.plot(input[ix,iy,0,:], input[ix,iy,1,:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None )
            try:
                ax.plot(input[ix,iy,2,:], input[ix,iy,3,:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = str(iy+1))
            except:
                pass

        plt.legend(loc='best')
        plt.show()
        plt.close()
        
def compare_experiments(input):
    for ix in range(0, input.shape[1]):    
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.set_title('Experiment ' + str(ix + 1), loc = 'center', pad = 20, fontsize = 15)
        
        for iy in range(0, input.shape[0]):
            ax.plot(input[iy,ix,0,:], input[iy,ix,1,:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None )
            try:
                ax.plot(input[iy,ix,2,:], input[iy,ix,3,:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = str(iy+1))
            except:
                pass

        plt.legend(loc='best')
        plt.show()
        plt.close()

def average_channels(input):
    for ix in range(0, input.shape[0]):    
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.set_title('Channel ' + str(ix + 1), loc = 'center', pad = 20, fontsize = 15)
            
        for iy in range(0, input.shape[1]):
            ax.plot(input[ix,iy,0,:], input[ix,iy,1,:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None )
            try:
                ax.plot(input[ix,iy,2,:], input[ix,iy,3,:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = str(iy+1))
            except:
                pass

        plt.legend(loc='best')
        plt.show()
        plt.close()