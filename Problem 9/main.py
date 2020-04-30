import math
def triplet():
    # Creates 3 loops to get all numbers from 1, 999
    # as the numbers must add to 1000 so no need to go higher
    for a in range(1, 999):
        for b in range(1, 999):
            # The answer requires for a < b < c
            if b > a:
                for c in range(1, 999):
                    if c > b:
                        # Checks if the found numbers adds to 1000
                        if a + b + c == 1000:
                            # Since there's only one solution if this is true then the value has been found
                            # no need to continue seraching for values
                            if a ** 2 + b ** 2 == c ** 2:
                                print(f"{a} {b} {c}")
                                # returns the multiple
                                return (a * b * c)
print(triplet())
