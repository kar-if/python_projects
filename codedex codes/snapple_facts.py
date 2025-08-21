# snapple facts

import random
fact = random.randint(0, 5)
open = input("type 'open' to open your snapple ").lower()
if open == 'open':
    read = input("would you like to read your random fact? Y/N ").upper()
    if read == 'Y':
        if fact == 0:
            print("Flamingos turn pink from eating shrimp.")
        elif fact == 1:
            print("The only food that doesn\'t spoil is honey.")
        elif fact == 2:
            print("Shrimp can only swim backwards.")
        elif fact == 3:
            print("A taste bud\'s life span is about 10 days.")
        elif fact == 4:
            print("It is impossible to sneeze while sleeping.")
        else:
            print("It is illegal to sing off-key in North Carolina.")
    else:
        print("I will not read your fun fact, hmph...")
else:
    print("invalid input")