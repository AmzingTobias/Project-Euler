def pass_through(highest_number):
    # Sets a total to 0
    # An array created blank with the length of prime numbers up to highest number
    total, list_numbers = 0, [True] * highest_number
    # 1 is not a prime number so that can be skipped and looks for all numbers up to highest
    # number, hence + 1 is not needed to include the hgihest number
    for index in range(2, highest_number):
        # If the value is true then the index is a prime number
        if list_numbers[index]:
            # Adds the index (value of prime) to the total
            total += index
            # Finds all multiples up to the highest_number
            # and sets them to False so they're not later checked
            for multiple in range(index, highest_number, index):
                list_numbers[multiple] = False
    return total
# My previous version included an array with all the numbers from x to highest number
# This took longer as it searched through each of the lists and checked if they were multiples of
# the number being checked. However seeting each value to a boolean and using the index as the
# the number is much faster 
print(pass_through(2000000))