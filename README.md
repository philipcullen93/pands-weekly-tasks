# pands-weekly-tasks

Author: Philip Cullen

## Contents
This repository contains weekly programming tasks for the Programming and Scripting module.

In this README.md each task contains:
- any required modules
- requirements for each task
- how to run and use each program
- how each program works
- references

## Week 2: Statements
Task: Write a program call bank.py

Requirements: This program should:
- Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in the format €X.XX (e.g. €12.50)

How to use:

To use this program, run the script (python bank.py)

Enter positive integers when propted. Youll will have to do this twice.

How It Works:
- The user is prompted to add an amount in cents twice
- The values are added together to give an amount in cent
- The amount in cents is divided by 100 to give the euro amount
- This amount is then printed

### References bank.py
[1] Python input() function: https://docs.python.org/3/library/functions.html#input

[2] Integer conversion with int(): https://docs.python.org/3/library/functions.html#int

[3] String formatting with f-strings: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals


## Week 3: Variables
Task: Write a program called accounts.py

Requirements: This program should
- read in a 10 character account number 
- output the account number with only the last 4 digits showing
- first 6 digits replaced with Xs e.g. ******7890
- *Extra* Have the program work for account numbers of any length

How to Use:

To use this program, run the script (python account.py). 

Enter an account number when prompted.

How it works:
- Accepts any account number as input.
- Displays only the last four digits while masking the rest.

### References account.py
[1] Python string methods: https://docs.python.org/3/library/stdtypes.html#string-methods

[2] Python input() function: https://docs.python.org/3/tutorial/inputoutput.html

[3] String Slicing in Python: https://realpython.com/python-strings/#indexing-and-slicing

## Week 4:
Task: Write a program called collatz.py

Requirements: This program should: 
- take a positive integer as input
- generate a sequence of numbers based on the Collatz Conjecture.
- The sequence is calculated using the following rules:
-- If the number is even, it is divided by 2.
-- If the number is odd, it is multiplied by 3 and increased by 1.
-- The process repeats until the value reaches 1.

How to Use:

To use this program, run the script (python collatz.py)

Enter a positive integer when prompted.

How it works:
- int(input() ensures the user enters an integer.
- The while loop continues until c equals 1.
- The program checks if c is even or odd and applies the corresponding transformation.
- Each new value of c is printed as part of the sequence.

### References collatz.py
[1] Collatz Conjecture: https://study.com/academy/lesson/history-of-the-collatz-conjecture.html

[2] Integer Division in Python: https://www.learndatasci.com/solutions/python-double-slash-operator-floor-division/#:~:text=In%20Python%2C%20we%20can%20perform,floor()%20function.

## Week 5:
Task: Write a program called weekday.py

Requirements: This program should:
- determine the current day of the week 
- prints a message based on whether it is a weekday or a weekend.

Required Modules: 
- import datetime

How to Use:

To use this program, run the script (python weekday.py). 

The program will automatically determine the day and print the appropriate message.

How it works:
- datetime.datetime.now() gets the current date and time.
- now.weekday() returns an integer (0-6), this represents the current day of the week.
- The program maps this integer to the correct day name using the week_days tuple.
- If the day is Saturday or Sunday, it prints the weekend message; otherwise, it prints the weekday message.

### References weekday.py
[1] Python datetime module: https://docs.python.org/3/library/datetime.html

[2] Python Tuples: https://www.w3schools.com/python/python_tuples.asp

[3] Python Conditional Statements: https://www.w3schools.com/python/python_conditions.asp

[4] Python Conditional Statements 2: https://realpython.com/python-conditional-statements/

## Week 6:
Task: Write a program called squareroot.py

Requirements: This program should:
- calculate an approximation of the square root of a given positive floating-point number using Newton's method.
- it should not use built-in functions such as x ** 0.5 or math.sqrt(x).
- the result should round to the specified number of decimal places.

How to Use:

To use this program, run the script (python squareroot.py).

When prompted enter a positive floating point number.

When prompted enter a positive intger for the number of required decimal places.

How it works:
- creating the function newton_sqrt(n) implements Newton's method to approximate the square root.
- the program goes through iterations and improves the approximation until a convergence point is met.
- he result is rounded using Python's round() function to the specified decimal places.

### References squareroot.py
[1] Newton Square Root Method: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

[2] Python round() Function: https://www.w3schools.com/python/ref_func_round.asp

## Week 7:
Task: Write a program called count_e.py

Requirements: This program should:
- read a text file and count the number of lowercase 'e' characters in it. 
- if the specified file does not exist, the program should create a file with a default line of text containing multiple occurrences of 'e'.

Required Modules: 
- import sys

How to Use:

To use this program, run the script (python count_e.py), follwed by the required text filename i.e. example.txt 

The program will automatically read the file and count the number of lowercase 'e' in it.

If the file does not exist, it will automatically create a new file with the entered filename, containing a line of default text.

The program will then automatically count the number of lowercase 'e' in it. This is equal to 17 (any other number indicates a problem within the code).

How it works:
- reads a text file specified by the user.
- if the file does not exist, it creates the file with a predefined text.
- the function count_letter_e() counts occurrences of lowercase 'e' in the file.
- the program runs from the command line, requiring a filename as input.

### References count_e.py
[1] Python sys module: https://docs.python.org/3/library/sys.html#sys.argv

[2] Python Exception Handling: https://www.w3schools.com/python/gloss_python_error_handling.asp

[3] Python open() Function: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

[4] Python Conditional Statements: https://www.w3schools.com/python/python_conditions.asp

## Week 8: Plots
Task: Write a program called plottask.py

Requirements: This program should:
- display a histogram of a normal distribution with 1000 values, a mean of 5, and a standard deviation of 2.
- display a plot of the function h(x) = x³ in the range of 0 to 10.
  bBoth plots should be shown on the same set of axes.

Required Modules: 
- import random
- import numpy
- import matplotlib.pyplot

How to Use:

To use this program, run the script (python plottask.py).

The program will automatically generate a plot containg both the normal distribution histogram and function h(x) = x^3.

How it works:
- generates 1000 values from a normal distribution with a mean of 5 and standard deviation of 2.
- creates a histogram of the generated values.
- plots the function h(x) = x³ over the range 0 to 10.
- displays both plots on the same set of axes.

### References plottask.py
[1] Python random() Module: https://www.w3schools.com/python/module_random.asp

[2] Python matplotlib.pyplot.hist() - Histograms: https://www.w3schools.com/python/matplotlib_histograms.asp

[3] Python matplotlib.pyplot.plot() - https://www.w3schools.com/python/matplotlib_plotting.asp

[4] Python matplotlib.pyplot: https://matplotlib.org/stable/tutorials/pyplot.html

