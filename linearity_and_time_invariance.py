# %%

import numpy as np
import matplotlib.pyplot as plt

def main():
    linearity()

def linearity():

    #define x(t)
    def x(t):
        return np.cos(t)
    #time axis
    t = np.arange(0,12,0.01)

    #define y1 and y2
    y1 = 2 * np.exp(-0.5*t)*x(t)
    y2 = 4 * np.exp(-0.5*t)*x(t)

    #x3 = a*x1 + b*x2
    x3 = 2*x(t)+4*x(t)

    #check if the sum of the inputs results in the sum of the outputs
    y = y1 + y2
    y3 = np.exp(-0.5*t)*x3

    plt.plot(t,y3, 'r')     #plot y3 in red
    plt.plot(t,y, '--g')    #plot y in green (dashed lines)


def time_invariant():
    #define x(t) and y(t)
    def x(t):
        return np.cos(2*np.pi*5*t)
    def y(t):
        return 3*np.cos(t)*x(t)
    
    t = np.arange(0,10,0.01)
    #time axis

    #y1 and shifted y1
    y1 = np.array(y(t))
    y2 = np.array(y(t-1))

    plt.plot(t,y1)
    plt.plot(t,y2, '--r') #red

main()


# %%
