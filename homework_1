"""
* Name: Hannah Lee
* Date: 01/13/23
* CSE 160, Winter 2023
* Homework 1
* Description: This program solves the series of problems given in
    Homework 1 using for loops and variables.
"""

# Uncomment the line below to make the math.sqrt function available
import math

# Problem 1
# This code finds the roots via the quadratic formula with the use of
#   variables to make finding the solutions for different equations easier
print("Problem 1 solution follows:")
a = 3
b = -5.86
c = 2.5408
root1 = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
root2 = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
print("Root 1:", root2)
print("Root 2:", root1)

print()

# Problem 2
# This code uses a for loop to find the values of 1/2 to 1/denom
print("Problem 2 solution follows:")
denom = 10
for num in range(denom - 1):
    print("1/" + str(num + 2) + ": " + str(1 / (num + 2)))

print()

# Problem 3
# This code uses a for loop to find the triangular numbers for n
#   by adding n by the subsequent numbers and prints the answer
#   as well as the answer provided by the given formula
print("Problem 3 solution follows:")

# Provided partially-working solution to problem 3
# `...` are placeholders and should be replaced
n = 10
triangular_num = 0
for i in range(1, n + 1):
    triangular_num += i
print("Triangular number", n, "via loop:", triangular_num)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)

print()

# Problem 4
# This code finds and prints the factorial of factorialNum which
#   in this case is 10
print("Problem 4 solution follows:")
factorialNum = 10
product = 1
for i in range(1, factorialNum + 1):
    product *= i
print(str(factorialNum) + "!: " + str(product))

print()

# Problem 5
# This code finds and prints the factorials of all the numbers up
#   to num_lines which in this case is 10
print("Problem 5 solution follows:")
num_lines = 10
for i in range(num_lines, 0, -1):
    product2 = 1
    for j in range(1, i + 1):
        product2 *= j
    print(str(i) + "!: " + str(product2))

print()

# Problem 6
# This code finds and prints the sum of the reciprocal of factorials
#   using a for loop
print("Problem 6 solution follows:")
factFract = 10
sum = 1
for i in range(1, factFract + 1):
    product3 = 1
    for j in range(1, i + 1):
        product3 *= j
    sum += (1 / product3)
print("e:", sum)
