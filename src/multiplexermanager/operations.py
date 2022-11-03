import numpy as np

def smooth():
    pass

def linear_regression():
    pass

def peakfinder():
    pass

def logarithm(input):
    working = input.array
    output = np.empty((working.shape))
    for x in range(0,working.shape[0]):
        for y in range(0,working.shape[1]):
            if input.bipot == True:
                output[x,y,0,:] = working[x,y,0,:]
                output[x,y,1,:] = np.log10(np.absolute(working[x,y,1,:]))
                output[x,y,2,:] = working[x,y,2,:]
                output[x,y,3,:] = np.log10(np.absolute(working[x,y,3,:]))

            else:
                output[x,y,0,:] = working[x,y,0,:]
                output[x,y,1,:] = np.log10(np.absolute(working[x,y,1,:]))
    return output