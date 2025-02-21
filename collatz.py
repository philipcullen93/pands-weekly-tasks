# the program asks the user to input any positive integer (represented by c) and 
# outputs the successive values of the following calculation.

# the program creates a loop where
# even values are divided by 2 and
# odd values are multiplied by 3 and adds 1
# the code runs until the calculated value is 1.

# author: Philip Cullen

c = int(input("Please enter a positive integer: ")) 
while c != 1: 
    if c % 2 == 0: 
       c = c // 2 
       print(c) 
    else:
        c = c * 3 + 1
        print(c)

