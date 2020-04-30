import time
# A function to check if a given number is a prime number
# returns true if it is or false if not a prime number
def check_if_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
# A list to store all found prime numbers
prime_number_list = []
number = 1
# Will keep looping until it has found 10001 prime numbers
while len(prime_number_list) != 10001:
    number += 1
    if check_if_prime(number):
        # If a prime number adds it to the list
        prime_number_list.append(number)
print(prime_number_list[10000])