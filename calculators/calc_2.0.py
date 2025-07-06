#calculator

import math
import sys
numbers = []

Q1 = int(input('what would you like to do? 1)ADD 2)SUBTRACT 3)MULTIPLE 4)DIVIDE '))
if Q1 == 1:
    while True:
        num = input('Enter a number to ADD (or type "done" to finish): ')
        if num.lower() == "done":
            break
        numbers.append(int(num))
    total = sum(numbers)
    print(f'Your answer is {total}')

elif Q1 == 2:
    while True:
        num = input('Enter a number to SUBTRACT (or type "done" to finish): ')
        if num.lower() == "done":
            break
        try:
            numbers.append(int(num))
        except ValueError:
            print('Invalid number, try again')
    if numbers:
        total = numbers[0]
        for n in numbers [1:]:
            total -= n
        print(f'your answer is {total}')
    else: 
        print('no numbers to subtract')
    
elif Q1 == 3:
    while True:
        num = input('Enter a number to MULTIPLY (or type "done" to finish): ')
        if num.lower() == "done":
            break
        try:
            numbers.append(int(num))
        except ValueError:
            print('Invalid number, try again')
    if numbers:
        total = numbers[0]
        for n in numbers [1:]:
            total *= n
        print(f'your answer is {total}')
    else:
        print('no numbers to multiply')
    
elif Q1 == 4:
    while True:
        num = input('Enter a number to DIVIDE (or type "done" to finish): ')
        if num.lower() == "done":
            break
        try:
            numbers.append(int(num))
        except ValueError:
            print('Invalid number, try again')
    if numbers:
        total = numbers[0]
        for n in numbers [1:]:
            total /= int(n)
        print(f'your answer is {total}')
    else: 
        print('no numbers to divide')

else:
    print('invalid input')