import random

print("This program print 10 random numbers between a range, which used defines!")
try:
    min_value = float(input("Enter the lower value of range: "))
except:
    print("Only numeric value, please!")
    quit(0)
try:
    max_value = float(input("Enter the higher value of range: "))
except:
    print("Only numeric value, please!")
    quit(0)
for i in range(10):
    x = random.random()
    randomNumber=min_value + (max_value-min_value)*x
    print(randomNumber)


