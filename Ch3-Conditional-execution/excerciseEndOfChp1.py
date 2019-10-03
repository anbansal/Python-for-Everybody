promt = "Please enter hours: "
hours = float(input(promt))
promt = "Please enter rate: "
rate = float(input(promt))
multiplier = 1.0
if hours > 40:
    multiplier = 1.5
pay = multiplier*hours * rate
print("Pay: ", round(pay, 2), "$")
