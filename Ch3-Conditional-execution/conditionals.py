prompt = "Enter the first value: "
x = float(input(prompt))
prompt = "Enter the second value: "
y = float(input(prompt))

if x == y:
    print("Both the values are same", x, "=", y)
elif x <= y:
    print("First value is smaller or equal to second value", x, "<=", y)
elif x >= y:
    print("First value is greater or equal to second value", x, ">=", y)
elif x != y:
    print("First value is not equal to second value", x, "!=", y)
else:
    print("I am sorry, I could not figure out the comparison between these two value", x, y)
