import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '-', '_']

print("Welcome to Python Password Generator")

abLetters = int(input("How many letters would you like in your password?\n"))
bcSymbols = int(input("How many symbols would you like?\n"))
cdNumbers = int(input("How many numbers would you like?\n"))


password = ""

for char in range(1, abLetters, +1):
    password += random.choice(letters)

for char in range(1, bcSymbols, +1):
    password += random.choice(symbols)

for char in range(1, cdNumbers, +1):
    password += random.choice(numbers)
    
print(password)