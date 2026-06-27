#9. Convert temperature:
# Celsius (string input) → Fahrenheit

cel_text = input("Enter temperature in Celsius: ")
celsius = int(cel_text)

fahrenheit = (9/5 * celsius) + 32

print("Temerature in Fahrenheit = ", fahrenheit)
