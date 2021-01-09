names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

x = len(names)

rand_int = random.randint(0, (x - 1))

print(f"WinnerXD {names[rand_int]}")