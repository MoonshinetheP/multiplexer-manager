import numpy as np

def smooth(input, smooth = 100):
    np.convolve()
    pass

def linear_regression():
    pass

def peakfinder():
    pass

def logarithm(input):
    output = np.empty((input.shape))
    for x in range(0,input.shape[0]):
        for y in range(0,input.shape[1]):
            if input.bipot == True:
                output[x,y,0,:] = input[x,y,0,:]
                output[x,y,1,:] = np.log10(np.absolute(input[x,y,1,:]))
                output[x,y,2,:] = input[x,y,2,:]
                output[x,y,3,:] = np.log10(np.absolute(input[x,y,3,:]))

            else:
                output[x,y,0,:] = input[x,y,0,:]
                output[x,y,1,:] = np.log10(np.absolute(input[x,y,1,:]))
    return output