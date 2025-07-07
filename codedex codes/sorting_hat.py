Hufflepuff = 0
H = Hufflepuff
Slytherin = 0
S = Slytherin
Ravenclaw = 0
R = Ravenclaw
Gryffindor = 0
G = Gryffindor

print('Enter numbers only')

Q1 = int(input('Do you like Dawn or Dusk? 1) Dawn 2) Dusk '))
if Q1 == 1:
  G = G+1 
  R = R+1
elif Q1 == 2:
  H = H+1
  S = S+1
else:
  print('Wrong input')

Q2 = int(input('When I am dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold '))
if Q2 == 1:
  S = S+2
elif Q2 == 2:
  H = H+2
elif Q2 == 3:
  R = R+2
elif Q2 == 4:
  G = G+2
else:
  print('Wrong input')

Q3 = int(input('Which kind of instrument most pleases your 1) The violin 2) The trumpet 3) The piano 4) The drum '))
if Q3 == 1:
  S = S+4
elif Q3 == 2:
  H = H+4
elif Q3 == 3:
  R = R+4
elif Q3 ==4:
  G = G+4
else:
  print('Wrong input')

print('Slytherin = ')
print(S)
print('Hufflepuff = ')
print(H)
print('Ravenclaw = ')
print(R)
print('Gryffindor = ')
print(G)