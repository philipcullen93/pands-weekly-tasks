# write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 
# on the one set of axes.


# Author: Philip Cullen

# start by import numpy and matplotlib.pyplot
import random
import numpy as np
import matplotlib.pyplot as plt

# First need to generate an array with 1000 values and a mean of 5, and standard deviation of 2
mean = 5
stddev = 2

values = np.random.normal(mean, stddev, 1000)

# create histogram

plt.hist(values, color = 'red', alpha = 1, edgecolor = 'black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title("Histogram of 1000 values in a Normal Distribution")
plt.show()

