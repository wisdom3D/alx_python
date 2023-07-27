#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    numberL = str(number)[-1]
else:
    numberL = '-'+str(number)[-1]
numberL = int(numberL)
if numberL > 5:
    print('Last digit of',number, 'is', numberL, 'and is greater than 5')
elif numberL == 0:
    print('Last digit of',number, 'is', numberL, 'and is 0')
elif numberL < 6 and numberL != 0:
    print('Last digit of',number, 'is', numberL, 'and is less than 6 and not 0')
