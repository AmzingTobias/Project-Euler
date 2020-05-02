import math
def function(n):
    # Discovering a formula online I saw that if you want to discover all paths in any
    # direction from top left to top right of an nxn grid, then the amount of different paths is
    # 2n factorial, however since the movement is rescricted to only right and down it needs
    # to be divided by n! * n! to produce the amount
    formula = (math.factorial(2 * n) / (math.factorial(n) * math.factorial(n)))
    return int(formula)

print(function(20))