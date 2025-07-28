
#rating = 0.0
rating = float(input('rate your food (1-5) '))
#float = decimal, int = whole number

if rating > 4.5:
    print('Extraordinary')
elif rating == 4:
    print('Excellent')
elif rating == 3:
    print('Good')
elif rating == 2:
    print('Fair')
else:
    print('Poor')