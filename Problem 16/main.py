# Calculates 2 to the power of 1000
power = str(2 ** 1000)
total = 0
# Cycles through each digit in the number
for digit in power:
    # Adds each digit to the total
    total += int(digit)
print(total)