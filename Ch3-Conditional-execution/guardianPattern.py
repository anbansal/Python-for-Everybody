prompt = "Please type a number: "
x = float(input(prompt))
prompt = "Please type another number: "
y = float(input(prompt))
try:
    if x > 1 and (x / y) > 0:
        print("The first number is greater than One and the second number is not zero !")
except:
    print("The second number is zero")


if x > 1 and y != 0 and (x / y) > 0:
    print("The first number is greater than One and the second number is not zero and not negative !")