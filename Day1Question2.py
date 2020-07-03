#Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, 
# the output should be:40320

n = int(input("Enter a number to find factorial: "))

def findingFactorial(n):

    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1

    for i in range (2, n+1):
        product *= i 
    return product

print("The factorial of",n , "is", findingFactorial(n))

