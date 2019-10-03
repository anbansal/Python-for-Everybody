prompt = "Type the temperature in celsius: "
cel = input(prompt)  # Storing Celsius temperature
fahn = (float(cel) * 9 / 5) + 32.0  # converting Celsius to Fahrenheit
print("The temperature", cel, "in Celsius is same as", fahn, "in Fahrenheit.")
