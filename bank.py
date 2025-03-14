# bank.py
# Takes 2 amounts in cents, adds them together, and prints the sum in €
# author: Philip Cullen

# This line creates a variable for amount 1.
# The user is told to input their amount in sense.
amount1 = int(input("Amount in cent : "))

#This line works the same as above but creates a variable for the second amount.
amount2 = int(input("Amount in cent : "))

# This line adds the values entered by the user.
totalcent = (amount1 + amount2)

# The total amount entered in cents is divided by 100 to give the amount in Euro
totaleuro = totalcent / 100

# The amount is then printed in Euro.
print(f'The Sum of these is €{totaleuro}')