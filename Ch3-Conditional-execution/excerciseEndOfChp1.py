promt = "Please enter hours: "
try:
    hours = float(input(promt))
except:
    print("Please enter hours in numeric!")
    quit(0)
promt = "Please enter rate: "
try:
    rate = float(input(promt))
except:
    print("Please enter rate in numeric!")
    quit(0)
multiplier = 1.0
if hours > 40:
    multiplier = 1.5
pay = multiplier*hours * rate
print("Pay: ", round(pay, 2), "$")
