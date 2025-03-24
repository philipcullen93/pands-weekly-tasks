# this program takes an account number of 10 digits
# it displays only the last 4 digits
# any digits before the last 4 will be seen as Xs

# Author: Philip Cullen

anyaccountno = input("Please enter an account number: ")
anylengthaccountno = max(0, len(anyaccountno) - 4) 
print('X' * anylengthaccountno + anyaccountno[-4:])

# len(anycountno) gives the total number of digits in the account number
# - 4 determines how many digits should be replaced with X, in this cast it will leave the last 4 characters visible
