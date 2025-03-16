# This program takes a positive floating-point number as input and 
# outputs an approximation of its square root.
# This program does not use in-built functions such as x ** .5 or math.sqrt(x)
# It round the result to 2 decimal places.

# Author: Philip Cullen

def newton_sqrt(n):
    approx = 0.5 * n
    betterapprox = 0.5 * (approx + n/approx)
    while betterapprox != approx:
        approx = betterapprox
        betterapprox = 0.5 * (approx + n/approx)
    return approx

n = float(input("Please Enter a Positive integer: "))
places = int(input("How many decimal places are required in the result: "))
# This uses the newton_sqrt function to give the square root of the entered value to the required decimal places
result = round(newton_sqrt(n),places)

print(f"The square root of {n} is approximately {result}")