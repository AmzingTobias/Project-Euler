class Problem:
    def __init__(self):
        self.highest_length = 0
        self.highest_starting_number = 0

    def collatz(self, n):
        # Adds the number to the collatz list
        self.collatz_list.append(n)
        # Checks if the number is even
        if n % 2 == 0:
            n = n // 2
        # If not even will be odd instead
        else:
            n = 3 * n + 1
        if n == 1:
            self.collatz_list.append(1)
            return
        else:
            # Recursion used until n = 1
            self.collatz(n)
    
    def check_length(self, n):
        # Updates the highest variables if the length of the current list
        # is higher than the previous highest length
        if len(self.collatz_list) > self.highest_length:
            self.highest_length = len(self.collatz_list)
            self.highest_starting_number = n


problem_solver = Problem()

# Works down from the list, a number can be used higher than 0 as it's unlikely for numbers less than half
# of 1 million will generate a sequence of lower length than numbers higher than that. Doing this
# would reduce the time taken to solve
for number in range(999999, 0, -1):
    # List needs to be reset each time
    problem_solver.collatz_list = []
    problem_solver.collatz(number)
    problem_solver.check_length(number)
print(f"Highest Length: {problem_solver.highest_length}")
print(f"Highest Number: {problem_solver.highest_starting_number}")
