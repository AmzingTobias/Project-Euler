def return_number(number):
    # Stores the text version of each unique number that will be returned on function call
    if number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    elif number == 4:
        return "four"
    elif number == 5:
        return "five"
    elif number == 6:
        return "six"
    elif number == 7:
        return "seven"
    elif number == 8:
        return "eight"
    elif number == 9:
        return "nine"
    elif number == 10:
        return "ten"
    elif number == 11:
        return "eleven"
    elif number == 12:
        return "twelve"
    elif number == 13:
        return "thirteen"
    elif number == 14:
        return "fourteen"
    elif number == 15:
        return "fifteen"
    elif number == 16:
        return "sixteen"
    elif number == 17:
        return "seventeen"
    elif number == 18:
        return "eighteen"
    elif number == 19:
        return "nineteen"
    elif number == 20:
        return "twenty"
    elif number == 30:
        return "thirty"
    elif number == 40:
        return "forty"
    elif number == 50:
        return "fifty"
    elif number == 60:
        return "sixty"
    elif number == 70:
        return "seventy"
    elif number == 80:
        return "eighty"
    elif number == 90:
        return "ninety"

# The total length of the digits
total = 0
for i in range(1, 1001):
    # The string is reversed so the lowest number will be in the index 0 position and increase accordingly
    number_string = str(i)[::-1]
    # Stores the text version of the number in an array
    number_array = []
    # The length of the number, used to check if 11-19 needs to be set seperately
    length_number = len(number_string)
    # If the number 11-19 needs to be used then the tenth digit should be skipped as it's already been assigned
    skip_tenth_digit = False

    # Cycles through each of the index for the number from the for loop
    for y in range(length_number):
        # If the y == 0 then it ranges from 1-9
        if y == 0:
            # Checks if the number is more than 1 digit big
            if length_number > 1: 
                # This then allows to check if the number needs to be set seperately for 11-19
                if number_string[y + 1] == "1":
                    # f string joins the numbers together to make them two digits long 
                    number_array.append(return_number(int(f"{number_string[y + 1]}{number_string[y]}")))
                    skip_tenth_digit = True
                else:
                    # Same as the else below, treats it as a single digit number and finds the equivelent
                    if number_string[y] != "0":
                        number_array.append(return_number(int(number_string[y])))
            else:
                if number_string[y] != "0":
                        number_array.append(return_number(int(number_string[y])))
        if y == 1 and not skip_tenth_digit:
            if number_string[y] != "0":
                # Because of how the numbers are set in the function above, the 0 is added to show it as a two digit number being passed through
                number_array.append(return_number(int(f"{number_string[y]}0")))
        if y == 2:
            if number_string[y] != "0":
                # If the hundreds is it's own number e.g 100 then it does not need the and at the end
                if number_string[y - 1] == "0" and number_string[y - 2] == "0":
                    number_array.append(f"{return_number(int(number_string[y]))}hundred")
                # However, if any other number like 102 then it does need the and at the end
                # the solution does not count spaces, hence the hundred & and joined
                else:
                    number_array.append(f"{return_number(int(number_string[y]))}hundredand")
        if y == 3:
            # For the one occurance of 1000
            if number_string[y] != "0":
                number_array.append(f"{return_number(int(number_string[y]))}thousand")
    # Cycles through each digit in the number array
    for digit in number_array:
        # Adds the length of the digit to the total
        total += len(digit)
print(total)