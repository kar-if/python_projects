#calculator

numbers = []

Q1 = int(input('what would you like to do? 1)ADD 2) SUBTRACT 3) MULTIPLE 4) DIVIDE '))
if Q1 == 1:
    a = int(input('whats your first number? '))
    b = int(input('whats your second number? '))
    c = (a + b)
    print(f'your answer is {c}')
elif Q1 == 2:
    a = int(input('whats your first number? '))
    b = int(input('whats your second number? '))
    c = (a - b)
    print(f'your answer is {c}')
elif Q1 == 3:
    a = int(input('whats your first number? '))
    b = int(input('whats your second number? '))
    c = (a * b)
    print(f'your answer is {c}')
elif Q1 == 4:
    a = int(input('whats your first number? '))
    b = int(input('whats your second number? '))
    c = (a / b)
    print(f'your answer is {c}')
else:
    print('invalid input')