total = 0
# All numbers bellow the target
for factor in range(1000):
    # Checks if the factor being checked is divisble
    # by 3 or 5 with no remainders, hence
    # checking for the remainders of the division
    # to equal 0
    if factor % 3 == 0 or factor % 5 == 0:
        # Will add the total to the factor
        total += factor
print(total)
