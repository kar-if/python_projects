import sys
actual_list = []
invalid = 0

print(f'type "DONE" when fishished')

if invalid > 5:
    print('Too many invalid responses')
    sys.exit(0)
    
while True:
        Q1 = input('What would you like to do? 1)ADD 2)REMOVE 3) READ LIST ').upper()
    
        if Q1 == "1":
            Q2 = input('what would you like to ADD? ')
            if Q2 in actual_list:
                Q4 = int(input('already in list. would you like to double? 1)YES 2)NO '))
                if Q4 == 1:
                    actual_list.append(Q2)
                    print(f'{Q2} has been added to the list AGAIN')
                elif Q4 == 2:
                    print(f'{Q2} is NOT ADDED to the list AGAIN')
                else:
                    print('invalid input')
                    invalid = invalid + 1
            else:
                actual_list.append(Q2)
                print(f'{Q2} has been ADDED to the list')
        elif Q1 == "2":
            Q3 = input('what would you like to REMOVE? ')
            if Q3 not in actual_list:
                print('not in list')
            else: 
                actual_list.remove(Q3)
                print(f'{Q3} has been REMOVED from the list')
        elif Q1 == "3":
            print(actual_list)
        elif Q1 == "DONE":
            print('application finsihed')
            sys.exit(0)
        else:
            print('invalid input, try again')
            invalid = invalid + 1 