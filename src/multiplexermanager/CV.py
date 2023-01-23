import numpy as np

def smooth():
    pass

def peakfinder(input):
    '''Returns the maximum and minimum current values/positions for each of the current values'''
    output = np.empty((input.shape[0:2],4))
    for ix,iy in np.ndindex((input.shape[0:2])):  
        output[ix,iy,0] = input[ix,iy,2,np.argmax(input[ix,iy,3,:])]
        output[ix,iy,1] = np.max(input[ix,iy,3,:])
        output[ix,iy,2] = input[ix,iy,2,np.argmin(input[ix,iy,3,:])]
        output[ix,iy,3] = np.min(input[ix,iy,3,:])
    return(output)
