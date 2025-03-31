# write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# and a plot of the function  h(x)=x^3 in the range 0 to 10, 
# on the one set of axes.


# Author: Philip Cullen

# Part 1: Histogram
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

# Part 2: Subplot
# plot the function  h(x)=x^3 in the range 0 to 10
xpoints = np.array(range(1, 10))
ypoints = xpoints ** 3

# create the plot
plt.plot(xpoints, ypoints, label = 'h(x) = x^3')

plt.xlabel("h(x)")
plt.ylabel("x^3")
plt.title("Histogram and Function Plot")
plt.legend()

# display plot
plt.show()








