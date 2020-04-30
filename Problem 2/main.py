# Numbers to be 0 and 1 initially
# for the loops to work
n1, n2 = 0, 1
total = 0
while True:
    nth = n1 + n2
    # Will break the loop if the nth term in sequence
    # is higher than 4 million =
    if nth < 4000000:
        # Only adds those to the total that are
        # multiples of 2
        if nth % 2 == 0:
            total += nth
        # Changes the n1 and n2 to then gernerate
        # the next number in the sequence
        n1, n2 = n2, nth
    else:
        break
print(total)
