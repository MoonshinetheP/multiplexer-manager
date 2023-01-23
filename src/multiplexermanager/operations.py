import numpy as np

def logarithm(input):
    '''Returns the input array with a log10 operation on each of the current values'''
    output = np.empty((input.shape))
    for ix,iy in np.ndindex((input.shape[0:2])):
        output[ix,iy,0,:] = input[ix,iy,0,:]
        output[ix,iy,1,:] = np.log10(np.absolute(input[ix,iy,1,:]))
        output[ix,iy,2,:] = input[ix,iy,2,:]
        output[ix,iy,3,:] = np.log10(np.absolute(input[ix,iy,3,:]))
    return output

def smooth(input, window = 100):
    '''Returns the input array with a moving average operation on each of the current values'''
    output = np.empty((input.shape))
    for ix,iy in np.ndindex((input.shape[0:2])):
        output[ix,iy,0,:] = input[ix,iy,0,:]
        output[ix,iy,1,:] = np.convolve(input[ix,iy,1,:], window) / window
        output[ix,iy,2,:] = input[ix,iy,2,:]
        output[ix,iy,3,:] = np.convolve(input[ix,iy,3,:], window) / window
    return output

def ten_to_power(input):
    '''Returns the input array with a 10^x operation on each of the current values'''
    output = np.empty((input.shape))
    for ix,iy in np.ndindex((input.shape[0:2])):
        output[ix,iy,0,:] = input[ix,iy,0,:]
        output[ix,iy,1,:] = np.power(10,input[ix,iy,1,:])
        output[ix,iy,2,:] = input[ix,iy,2,:]
        output[ix,iy,3,:] = np.power(input[ix,iy,3,:])


def average_channels(input):
    '''Returns a 3D array with the currents of each channel averaged for each experiment number'''
    output = np.empty((input.shape[1:4]))
    for ix,iy in np.ndindex((input.shape[1], input.shape[3])):
        output[ix,iy,:] = np.average(input[:,ix,iy,:], axis = 0)
    return output

def average_experiments(input):
    '''Returns a 3D array with the currents of each experiment averaged for each channel'''
    output = np.empty((input.shape[0], input.shape[2:4]))
    for ix,iy in np.ndindex((input.shape[0],input.shape[2])):
        output[ix,iy,:] = np.average(input[ix,:,iy,:], axis = 0)
    return output 