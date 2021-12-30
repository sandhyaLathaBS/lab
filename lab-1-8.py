from random import randrange

Number = int(input("Enter a Number between 0 & 9"))
luckyNumber = randrange(0, 9)
if (Number == luckyNumber):
    print("Today Is your lucky day....!!! Go with the number %d", Number)
elif (Number > luckyNumber):
    print("You are FAr Away ...!!! we are in  %d", luckyNumber)
else:
    print("You are behind us ...!!! we are in  %d", luckyNumber)
