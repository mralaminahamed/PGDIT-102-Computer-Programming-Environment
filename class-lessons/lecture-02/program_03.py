# Question: Write a program that converts Centigrade to Fahrenheit.

# Show message to the screen for getting centigrade temperature.
centigrade = int(input('Enter the temperature in centigrade: '))

# Calculate Centigrade to Fahrenheit and assign variable.
# formula: (0°C × 9/5) + 32 = 32°F
# formula: (32°F − 32) × 5/9 = 0°C
fahrenheit = (centigrade * 9/5) + 32

# Show the output.
print("The temperature in fahrenheit is : ", fahrenheit)
