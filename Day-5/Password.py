# Password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','*','(',')','&','+','-']

print("welcome to the password generator!")
nr_letters=int(input("How many latters would you like?\n"))
nr_numbers=int(input("How many numbers would you like\n"))
nr_symbols=int(input("How many symbol would you like\n"))

#generate Easy password
password=''

for char in range(nr_letters):
    password += random.choice(letters)

for num in range(nr_numbers):
    password += random.choice(numbers)

for symbol in range(nr_symbols):
    password += random.choice(symbols)

print(password)

#generate hard password

password_list=[]

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for num in range(nr_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
password_list
print(password_list)

password_string=''.join(password_list)
print(password_string)
    
