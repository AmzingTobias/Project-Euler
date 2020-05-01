with open("numbers.txt") as file:
    # Opens each of the 50 digit numbers into a string
    number_list = file.readlines()
# Converts the strings into a list
number_list = [x.strip() for x in number_list]
total = 0
# Adds up each of the numbers in the list to the total
for number in number_list:
    total += int(number)
# Outputs the first 10 digits of the number
print(str(total)[:10])
