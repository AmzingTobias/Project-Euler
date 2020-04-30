def smallest_multiple():
    # It doesn't make too much difference setting it to 20 but every little helps
    number = 20
    while True:
        # Each time in the loops it adds 1 to the number
        number += 1
        # The higher range is set to 21 because of how python works
        for i in range(1, 21):
            # Checks if the number returns no remainder when being divided
            if number % i == 0:
                # If it reaches the highest number, being 20 it has found the solution
                if i == 20:
                    return number
            else:
                # If at any time it produces a remainder from the range of numbers
                # It breaks the loop and moves to the next number
                break

print(smallest_multiple())