# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Hello, Python!')
print("Python is a really great language, ", "isn't it?")

print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')
print('\t\tUp above the world so high,')
print('\t\tLike a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')

#세금계산프로그램
rate = .2
std_ded = 10000
dep_ded = 3000

income = float(input('Enter the gross income: '))
num_dep = int(input('Enter the number of dependents: '))
tax = (income - std_ded - dep_ded * num_dep)*rate
print('The income tax is $' + str(tax))
