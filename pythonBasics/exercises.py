# Challenge #1
#
# Create a Python script that asks the user for a number and then prints out a list of all the divisors
# of each number less than the asked number.
import string

# num = int(input("insert num: "))
#
# for x in range(1, num):
#     if num % x == 0:
#         print(x)



# Challenge #2
#
# Write a Python program to check if an integer (x) is the power of another integer (y).
# Prompt the user to input both integers.
#
# Input: 16, 2
#
# Output: 2 ** 4 = 16

# a = int(input("power of :"))
# b = int(input("power to: "))
#
# for k in range(2, a // 2):
#     if b ** k == a:
#         print(f"{b} to the power of {k} == {a}")
#         break
# else:
#     print(f"not possible")

# Challenge #3
#
# Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
#
# Input str: Hello Everybody!
#
# Output: 5
#

# answer = input("Word: ")
# count = 0
# for ch in answer.lower():
#     if ch in ("a", "e", "i", "o", "u"):
#         count += 1
#         print(ch)
# print(count)


# Challenge #4
#
# Write a Python script that checks if a triangle is equilateral, isosceles or scalene.
#
# The user will be prompted for the triangle sides.
#
# Note:
#
# An equilateral triangle is a triangle in which all three sides have the same length.
#
# An isosceles triangle is a triangle that has two equal sides.
#
# A scalene triangle is a triangle that has three unequal sides.
#
#
#
# Input: Enter the lengths of the triangle sides:
#
# x: 6
#
# y: 8
#
# z: 12
#
# Expected Output: Scalene triangle.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #5
#
# Write a Python program that calculates and displays the sum, the product and the average of n float numbers entered by the user,
# each on a separate line. Enter 0 to finish.
#
# number_list = list()
# while True:
#     ans = float(input("Give me a number : "))
#     if ans == 0:
#         break
#     number_list.append(ans)
#
# sum_x, prod_x, avg_x = 0, 1, 0
#
# for item in number_list:
#     sum_x += item
#     prod_x *= item
#
# print(f"Sum of numbers is {sum_x:.2f}",
#       f"Product of numbers is {prod_x:.2f}",
#       f"average is {sum(number_list) / len(number_list)}")



# Challenge #6
#
# Given the string s1, write a program to return the sum and the average of the digits that appear in the string,
# ignoring all other characters.
#
# Input: Python31py50
#
# Output: Sum: 9, Average: 2.25


# ans = input("Give me a word: ")
# sum = 0
# count = 0
#
# for ch in ans:
#     if ch in string.digits:
#         sum += int(ch)
#         count += 1
#
# print(f"sum is {sum} and average is {sum/count}")


# Challenge #7
#
# Write a Python program that displays the multiplication table (from 1 to 10)
# of a specific integer number entered by the user.
#
# Input: User enters 8
#
# Output:
#
# 8 x 1 = 8
#
# 8 x 2 = 16
#
# 8 x 3 = 24
#
# 8 x 4 = 32
#
# 8 x 5 = 40
#
# 8 x 6 = 48
#
# 8 x 7 = 56
#
# 8 x 8 = 64
#
# 8 x 9 = 72
#
# 8 x 10 = 80

# num = int(input("give me a number: "))
#
# for _ in range(11):
#     print(f"{_} x {num} = {_*num}")



# Challenge #8
#
# Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
#
# If the user enters 6 it will display:
#
# 1
#
# 22
#
# 333
#
# 4444
#
# 55555
#
# 666666

# num = int(input("give me a num: "))
#
# for x in range(num + 1):
#     print(x * str(x), end = "\n\n")



# Challenge #9
#
# Write a Python program that finds the common characters that appear in two given strings.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #10
#
# Write a Python program that iterates over the integers from 1 to 50.
#
# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".
#
# For numbers that are multiples of both three and five print "FooBar".
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #11
#
# Write a Python script that prints out the Fibonacci series up to a given number n.
#
# Fibonacci Series: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
#
# Example: if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #12
#
# Write a Python script that draws the following pattern using for loops.
#
# *
#
# * *
#
# * * *
#
# * * * *
#
# * * * * *
#
# * * * *
#
# * * *
#
# * *
#
# *