# Factorial algorithms
# Input: a number to calculate the factorial
# Output: the resulted factorial calculated

def factorial(num):

    #base case
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
