# bank.py
# Takes 2 amounts in cents, adds them together, and prints the sum in €
# author: Philip Cullen

amount1 = int(input("Amount in cent : "))
amount2 = int(input("Amount in cent : "))
totalcent = (amount1 + amount2)
totaleuro = totalcent / 100
print(f'The Sum of these is €{totaleuro}')