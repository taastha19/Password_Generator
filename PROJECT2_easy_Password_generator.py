#PASSWORD GENERATOR

import random

s=['~','!','@','#','$','%','^','&','*',')','(','+','_','.']
a=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
n=['0','1','2','3','4','5','6','7','8','9']

print("----------WELCOME TO PASSWORD GENERATOR ----------\n")
letters=int(input('How many letters would you like in your password : '))
symbols=int(input('How many symbols would you like in your password : '))
numbers=int(input('How many numbers would you like in your password : '))

password=""

for letter in range(1,letters+1):
    alp=random.choice(a)
    password+=alp
for symbol in range(1,symbols+1):
    sym=random.choice(s)
    password+=sym
for number in range(numbers+1):
    num=random.choice(n)
    password+=num

print('\nPASSWORD GENERATED : ',password)

    








