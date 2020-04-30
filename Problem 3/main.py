target = 600851475143
lpf = 2
# Loops while the target is greater than 2
while target > lpf:
    # Checks if the highest factor is a factor
    # of the target
    if target % lpf == 0:
        # Finds the division of that number
        target = target / lpf
        # Resets the largest factor
        lpf = 2
    else:
        # Adds one to the factor otherwise to then check        
        lpf += 1
print(lpf)
