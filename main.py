#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passlen = nr_letters+nr_numbers+nr_symbols
rand_nums = random.choices(numbers , k = nr_numbers)
rand_lets = random.choices(letters , k = nr_letters)
rand_syms = random.choices(symbols , k = nr_symbols)
total = rand_lets + rand_nums + rand_syms
print(total)
a = ''
for rand_let in rand_lets :
  a+=rand_let
  

for rand_num in rand_nums :
   a+=rand_num


for char in range(1 , nr_symbols +1): #looping to the no of time 
   a+=random.choice(symbols)          # to get a random element from a list


print(a)

random.shuffle(total)
print(total)
e = ''
for toa in total :
  e+=toa 
print (e)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P