# %%

import numpy as np
import matplotlib.pyplot as plt

def main():
    # we want to add the signals y=x and y=2
    # ranging from -2 to 4
    n1 = np.arange(-2, 3)
    x1 = np.arange(-2, 3)
    n2 = np.arange(0, 5)
    x2 = np.ones(5) * 2
    multiply(n1,x1, n2,x2)


def add(n1,x1, n2,x2):
    i = np.min([np.min(n1),np.min(n2)]) #smallest number in both ranges
    j = np.max([np.max(n1),np.max(n2)]) #largest number in both ranges
    #range is from i -> j
    n = np.arange(i,j+1)

    #initialize the result
    x = np.zeros(j-i+1)
    #add x1 to the suffix
    x[:len(x1)] += x1
    #add x2 to the prefix
    x[len(n)-len(x1):] += x2
    plt.stem(n,x)

def multiply(n1, x1, n2, x2):
    # Determine the total range
    i = min(np.min(n1), np.min(n2))
    j = max(np.max(n1), np.max(n2))
    n = np.arange(i, j + 1)

    x_dummy1 = np.zeros(j - i + 1)
    x_dummy2 = np.zeros(j - i + 1)

    x_dummy1[:len(x1)] += x1
    x_dummy2[-len(x2):] += x2

    x = x_dummy1*x_dummy2
    plt.stem(n,x)


main()
# %%
