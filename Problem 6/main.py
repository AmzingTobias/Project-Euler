square_sum_total = 0
sum_total = 0

for i in range(1, 101):
    # Adds the number to the sum total
    sum_total += i
    # Squares the total then adds that to the total
    square_sum_total += i ** 2
# Squares the sum_total and finds the difference compares to the
# squared sum total
difference = (sum_total ** 2) - square_sum_total
print(difference)