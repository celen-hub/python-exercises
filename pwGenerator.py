#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

rand_letters = random.randint(0, len(letters) - 1)
rand_numbers = random.randint(0, len(numbers) - 1)
rand_symbols = random.randint(0, len(symbols) - 1)
pwd_letters = []
pwd_symbols = []
pwd_numbers = []
for x in range(0,(nr_letters)):
  pwd_letters.append(letters[random.randint(0, len(letters) - 1)])
for y in range(0,(nr_symbols)):
  pwd_symbols.append(symbols[random.randint(0, len(symbols) - 1)])
for z in range (0,(nr_numbers)):
  pwd_numbers.append(numbers[random.randint(0, len(numbers) - 1)])

pwd_notrandom = pwd_letters + pwd_symbols + pwd_numbers
print(pwd_notrandom)
pwd_random = []
total_char = nr_letters + nr_symbols + nr_numbers

for v in range (0,len(pwd_notrandom)):
  pwd_random.append(pwd_notrandom[random.randint(0, (total_char -1))])

print(pwd_random)


print("Offered pw is: " + ''.join(pwd_random))