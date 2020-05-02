import math
def triangular(n, adder):
    divisors = []
    # Once a number with a factor of 500 is found the loop breaks
    while len(divisors) < 500:
        # The number is then incremented by the adder
        # to form the triangular number sequence,
        # previous numbers are not needed to be stored
        n += adder
        # Adder is then incremented by one to be used in the next loop
        adder += 1
        # The factors are stored in a list returned from a function
        divisors = find_factors(n)
    return n

def find_factors(number):
    # The factors of the number is stored in a list
    factors = []
    # Finds the square root of the number and rounds it down
    root = int(math.sqrt(number))
    # Looks at the numbers from 1 to the root of the target number
    for n in range(root):
        # As n starts on 0 and wouldn't include rooot + 1 is needed
        n += 1
        # Divides the number to find the factor and pair
        factor_found = number / n
        # If the number gives no remainder then it's a factor
        if number % n == 0:
            # Adds both of the factors from the pairs to the list
            factors.append(n)
            factors.append(int(factor_found))
    return factors

print(triangular(1, 2))

# For my approach to find the factors of the numbers I used this website
# https://www.calculatorsoup.com/calculators/math/factors.php
# Find the square root of the integer number n and round down to the closest whole number. Let's call this number s.
# Start with the number 1 and find the corresponding factor pair: n ÷ 1 = n. So 1 and n are a factor pair because division results in a whole number with zero remainder.
# Do the same with the number 2 and proceed testing all integers (n ÷ 2, n ÷ 3, n ÷ 4... n ÷ s) up through the square root rounded to s. Record the factor pairs where division results in whole integer numbers with zero remainders.
# When you reach n ÷ s and you have recorded all factor pairs you have successfully factored the number n.