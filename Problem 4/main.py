class Palindrome:
    def __init__(self):
        self.highest_number = 0


    def check_number(self, number):
        # An even and positive length of a number needs different methods to solve
        if len(number) % 2 == 0:
            # For an even length, then the number will be split perfectly in half
            firstpart, secondpart = number[:len(number) // 2], number[len(number) // 2:]
            # Checks if the first part of the number is the same to the reverse of the number
            if firstpart == secondpart[::-1]:
                # Will change the highest number if greater
                if int(number) > int(self.highest_number):
                    self.highest_number = number
        else:
            firstpart, secondpart = number[:len(number) // 2], number[len(number) // 2:]
            # The difference for a number length not of a multiple of 2
            # is that the second part will always have 1 extra digit (the middle)
            # so this is then removed
            secondpart = secondpart[1:]
            if firstpart == secondpart[::-1]:
                if int(number) > int(self.highest_number):
                    self.highest_number = number


    def start(self):
        # Finds all the 3 digit numbers to then multiply
        for x in range(100, 1000):
            for y in range(100, 1000):
                self.check_number(str(x * y))

pal = Palindrome()
pal.start()
print(pal.highest_number)