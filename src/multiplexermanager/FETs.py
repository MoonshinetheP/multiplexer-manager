import numpy as np
import piecewise_regression as pr
from scipy.stats import linregress
from scipy.optimize import curve_fit as cf
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import plotting as plot

def piecewise(data, window = 250, folder = 'plots/'):    
    output = np.empty((data.shape[0], data.shape[1], 2, window))
    for ix,iy in np.ndindex((data.shape[0:2])):
        fit = pr.Fit(data[ix,iy,2,:], data[ix,iy,3,:], n_breakpoints = 2)
        bp1_value = fit.get_results()['estimates']['breakpoint1']['estimate']
        for iz in data[ix,iy,2,:]:
            if iz > bp1_value:
                bp1_index = np.where(data[ix,iy,2,:] == iz)
                bp1 = bp1_index[0][0]
                break
            else:
                pass
        linx = data[ix,iy,2,bp1:bp1 + window]
        liny = data[ix,iy,3,bp1:bp1 + window]

        extraction = linregress(linx, liny)

        z = extraction[0]*linx + extraction[1]
        output[ix,iy,0,:] = linx
        output[ix,iy,1,:] = z

    plot.make_directory(folder)
    with PdfPages(folder + 'regression.pdf') as pdf:
        for ix in range(0, output.shape[0]):    
            fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
            ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
            ax.set_title('Channel ' + str(ix + 1), loc = 'center', pad = 20, fontsize = 15)
                
            for iy in range(0, output.shape[1]):
                ax.plot(data[ix,iy,0,:], data[ix,iy,1,:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
                ax.plot(data[ix,iy,2,:], data[ix,iy,3,:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None)
                ax.plot(output[ix,iy,0,:], output[ix,iy,1,:], linewidth = 1, linestyle = '-', color = 'blue', marker = None, label = None)
            pdf.savefig()
            plt.close()
        plt.close()
    
    while True:
        print('\nPlease enter the number of the channel you want to look at:\n')
        channel = input()
        print(f'\nYou have chosen channel {channel}. Please enter a current value:\n')
        current = input()
        potential = np.array([])
        for ix in range(0,output.shape[1]):
            for iy in output[int(channel),ix,1,:]:
                if iy < float(current):
                    index = np.where(output[int(channel),ix,1,:] == iy)[0][0]
                    values = output[int(channel),ix,0,index]
                    potential = np.append(potential, values)
                    break
                else:
                    pass
        print(f'\nThe potentials at which this current is reached are:\n {np.array2string(potential)}\n')
        break      

