import random
guess = 0
tries = 0
num = random.randint(1, 9)

while guess != num and tries < 5:
  guess = int(input('Guess the number: '))
  tries = tries + 1

if guess != num:
  print('You ran out of tries.')
else:
  print('You got it!')