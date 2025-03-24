# This program reads in a text file
# then outputs the number of e's that it contains

# Assumptions: 
# program needs to already have a vaid text file to read, if not it needs to create the file
# the text file needs to contain a sentence or sentences that have the letter e in it/them
# could also use a dictionary
# the program is case-sensitive and will only count lowercase e


# Author: Philip Cullen

# Import sys to handle command-line arguments
import sys

# This text will be added to a .txt file upon creation.
default_text = "This is an example text file. It contains a number of words that contain the letter e. The letter e appears 17 times in this text file"

# function is designed to read a .txt file and count occurences of e
def count_letter_e(FILENAME):
    # Reads a text file and counts occurrences of the letter 'e'.
    # If the file does not exist, it creates the file and writes default text.
    try:
    # trys to open the file in read mode
        with open(FILENAME,'r') as f:
            content = f.read()
            # count a and return occurances of e
            return content.count("e")
    except FileNotFoundError:
    # If the file doesn't exist, this will create and populate it with the text from default_text
        print(f'{FILENAME} not found. Creating empty file')
        with open(FILENAME, 'wt') as f:
            f.write(default_text)
    return default_text.count('e')

# This ensures the user provides a filename as a command-line argument, 
# This will create the .txt file with the filename entered by the user
if len(sys.argv) < 2:
    print("Usage python script.py <FILENAME> ")
else:
    # Pulls the filename from the command line
    FILENAME = sys.argv[1]
    # Calls the function to process the file
    count = count_letter_e(FILENAME)
    # If the count is valid, this will display the number of occurances
    if count is not None:
        print(f'The letter e appears {count} times in {FILENAME}') 





