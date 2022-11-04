import numpy as np

def smooth(input, window = 100):
    '''Returns the input array with a moving average operation on each of the current values'''
    output = np.empty((input.shape))
    for ix,iy in np.ndindex((input.shape[0:2])):
        output[ix,iy,0,:] = input[ix,iy,0,:]
        output[ix,iy,1,:] = np.convolve(input[ix,iy,1,:], window) / window
        output[ix,iy,0,:] = input[ix,iy,2,:]
        output[ix,iy,3,:] = np.convolve(input[ix,iy,3,:], window) / window
    return output

def peakfinder(input):
    '''Returns the maximum and minimum current values/positions for each of the current values'''
    for ix,iy in np.ndindex((input.shape[0:2])):  
        imax = np.max(input[ix,iy,3,:])
        imax_index = np.argmax(input[ix,iy,3,:])
        imin = np.min(input[ix,iy,3,:])
        imin_index = np.argmin(input[ix,iy,3,:])
    return(imax,imax_index,imin,imin_index)

def logarithm(input):
    '''Returns the input array with a log10 operation on each of the current values'''
    output = np.empty((input.shape))
    for ix,iy in np.ndindex((input.shape[0:2])):
        output[ix,iy,0,:] = input[ix,iy,0,:]
        output[ix,iy,1,:] = np.log10(np.absolute(input[ix,iy,1,:]))
        output[ix,iy,2,:] = input[ix,iy,2,:]
        output[ix,iy,3,:] = np.log10(np.absolute(input[ix,iy,3,:]))
    return output
    
def linear_regression(input):
    pass