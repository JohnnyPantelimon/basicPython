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

#
# countries = ['Argentina', 'Somalia', 'Tuvalu', 'Malta', 'Armenia', 'Christmas Island', 'Uganda',
# 'Central African Republic', 'Gambia', 'Morocco', 'Sint Maarten (Dutch part)', 'Tunisia', 'Aland Islands',
# 'Angola', 'Yemen', 'Niue', 'Brunei Darussalam', 'Sudan', 'Holy See (Vatican City State)', 'Malaysia',
# 'New Zealand', 'Palestinian Territory, Occupied', 'Iran, Islamic Republic of', 'Macedonia, Republic of',
# 'Montenegro', 'Macao', 'Belarus', 'Netherlands', 'Greenland', 'Thailand', 'French Southern Territories',
# 'Cyprus', "Korea, Democratic People's Republic of", 'Rwanda', 'Ethiopia', 'Saint Barthélemy', 'Botswana',
# 'Puerto Rico', 'Cape Verde', 'Nicaragua', 'Croatia', 'Guadeloupe', 'Réunion', 'Belize',
# 'Northern Mariana Islands', 'Indonesia', 'Serbia', 'British Indian Ocean Territory', 'Wallis and Futuna',
# 'Saint Martin (French part)', 'Nigeria', 'Spain', 'Guernsey', 'Guyana', 'Namibia',
# 'Venezuela, Bolivarian Republic of', 'Pitcairn', 'Suriname', 'Switzerland', 'Portugal', 'Saudi Arabia',
# 'Tanzania, United Republic of', 'Norfolk Island', 'Iceland', 'Ukraine', 'Estonia', 'Nauru', 'Comoros',
# 'Andorra', 'Turks and Caicos Islands', 'Guatemala', 'Cameroon', 'Chile', 'Bulgaria', 'Afghanistan',
# 'Sri Lanka', 'Romania', 'Tokelau', 'Montserrat', 'Congo', 'Congo, The Democratic Republic of the',
# 'Luxembourg', 'Bolivia, Plurinational State of', 'South Georgia and the South Sandwich Islands',
# 'Djibouti', 'Brazil', 'Burkina Faso', 'Curaçao', 'Heard Island and McDonald Islands', 'Cook Islands',
# 'Cocos (Keeling) Islands', 'China', 'Haiti', 'Swaziland', 'Mali', 'Burundi', 'Taiwan, Province of China',
# 'Ireland', 'Maldives', 'France', 'Martinique', 'Nepal', 'Saint Lucia', 'Uruguay', 'Seychelles', 'Algeria',
# 'Panama', 'Anguilla', 'Cuba', 'San Marino', 'Dominica', 'Germany', 'Iraq', 'Chad', 'Tonga', 'Qatar',
# 'Lesotho', 'Liberia', 'Bosnia and Herzegovina', 'Canada', 'Turkey', 'French Guiana', 'Jersey', 'Niger',
# 'Paraguay', 'Bangladesh', 'Barbados', 'Mauritius', 'United Kingdom', 'Bhutan', 'Isle of Man',
# 'Svalbard and Jan Mayen', 'Falkland Islands (Malvinas)', "Lao People's Democratic Republic",
# 'Saint Vincent and the Grenadines', 'Korea, Republic of', 'Dominican Republic', 'Philippines',
# 'Austria', 'Samoa', 'South Africa', 'Australia', 'Bahamas', 'Fiji', 'Mayotte', 'Albania',
# 'Sierra Leone', 'Gibraltar', 'Kazakhstan', 'French Polynesia', 'Jordan', 'Ecuador', 'Liechtenstein',
# 'Solomon Islands', 'Belgium', 'Gabon', 'Bermuda', 'Georgia', 'Saint Pierre and Miquelon', 'Ghana',
# 'Guinea', 'Singapore', 'Vanuatu', 'New Caledonia', 'Sao Tome and Principe', 'Mexico', 'Equatorial Guinea',
# 'Pakistan', 'Marshall Islands', 'Jamaica', 'Antigua and Barbuda', 'South Sudan', 'Japan', 'Slovenia',
# 'Moldova, Republic of', 'Virgin Islands, British', 'Latvia', 'Kenya', 'Trinidad and Tobago', 'Norway',
# 'Timor-Leste', 'Faroe Islands', 'Zimbabwe', 'Kuwait', 'Mozambique', 'Mauritania', 'Benin', 'Togo',
# 'Sweden', 'Cayman Islands', 'Mongolia', 'United States', 'United States Minor Outlying Islands',
# 'Papua New Guinea', 'Hong Kong', 'Myanmar', 'Viet Nam', 'Malawi', 'Micronesia, Federated States of',
# 'Aruba', 'Virgin Islands, U.S.', 'Saint Helena, Ascension and Tristan da Cunha', 'Oman',
# 'Bonaire, Sint Eustatius and Saba', 'Senegal', 'Monaco', 'Russian Federation', 'Antarctica',
# 'American Samoa', 'Slovakia', 'Guinea-Bissau', 'Egypt', 'Madagascar', 'Guam', 'United Arab Emirates',
# 'Kiribati', 'Israel', 'Eritrea', 'Saint Kitts and Nevis', 'El Salvador', 'Lebanon', 'Poland',
# 'Syrian Arab Republic', 'Cambodia', 'Czech Republic', 'Tajikistan', 'India', 'Denmark', "Côte d'Ivoire",
# 'Kyrgyzstan', 'Peru', 'Italy', 'Bouvet Island', 'Palau', 'Lithuania', 'Colombia', 'Turkmenistan', 'Zambia',
# 'Libya', 'Greece', 'Honduras', 'Azerbaijan', 'Costa Rica', 'Uzbekistan', 'Hungary',
# 'Grenada', 'Bahrain', 'Finland']
# max_country = ""
# max_len_country = 0
#
# for country in countries:
#     if max_len_country < len(country):
#         max_len_country = len(country)
#         max_country = country
#
# print(max_country, max_len_country)


# words = "green-red-yellow-black-white"
#
# print(
#     "-".join(sorted([word for word in words.split("-")], reverse=False))
# )
#
# set1 = set()
#
# s1 = {}
# print(type(s1))
#
# fs1 = frozenset(1, 2, 3)

# my_dict = {"a": 1, "c": 3, "d": 4, "b": 2}
#
# print(
#     sorted(
#         my_dict, key= lambda x, y: x[y], reverse=False
#     )
# )


# d1 = {'a':
#           [1, 2, {10:'X', 20:'Y'}]
#       }
# print(d1['a'])

# import os
# print(os.getcwd())
# import csv
#
# word = input("Give me a word: ")
# alphabet = dict()
#
# with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\phonetic_alphabet.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         alphabet[line["Letter"]]= line["Code_word"]
#
# for ch in word.upper():
#     print(
#         alphabet[ch], end=" "
#     )




#
# Challenge #1
#
# Create a Python script that removes all the elements of a list that are duplicates.
# Do the challenge in a single line of code using sets.
#

#
#
#
# Challenge #2
#
# Consider a list of words (strings). Write a Python script that generates a dictionary where the key is the word in
# the list and the value is its length.
#
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# print(
#     dict((k, len(k)) for k in words)
# )
#
#
# # Challenge #3
# #
# # Considering the following dict, get a dict representation sorted by key.
# #
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# #
# # A dict representation means viewing or printing the dict.
#
# print(
#     sorted(
#         d1, key= lambda x: x[0]
#     )
# )

# employees = {'John': ('London', 4000, 28), 'Maria':('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# view = sorted(employees.items(), key=lambda x: x[1][1])
# print(view)


# Challenge #4
#
# Considering the following dict, get a dict representation sorted by value.
#
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
#
# A dict representation means viewing or printing the dict.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #5
#
# Let's generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).
#
# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.
#
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]
#
# P.S. Do it with a single line of code.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #6
#
# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.
#
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]
#
# P.S. Do it with a single line of code.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #7
#
# Consider the dictionary called COUNTRY declared in this Python script.
#
# The keys are the country codes and the values are the country names.
#
# Print a sorted view of the dictionary, by the key (country code).
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #8
#
# Consider the dictionary called COUNTRY declared in this Python script.
#
# Find the country which has the longest name.
#
# Use list comprehension if possible.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #9
#
# Consider the following two Python Lists that save information about company sales for the last 6 years:
#
# years = [2015, 2016, 2017, 2018, 2019, 2020]
#
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
#
# Create a new list that connects the year to the corresponding sales.
#
# The resulting list should be: [(2015, 350000), (2016, 400000), (2017, 410000), (2018, 439000), (2019, 500000), (2020, 290000)]
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #10
#
# Consider the following two Python Lists that save information about company sales for the last 6 years:
#
years = [2015, 2016, 2017, 2018, 2019, 2020]

sales = [350000, 400000, 410000, 439000, 500000, 290000]
#
# Create a new dictionary that has the keys, the years, and the values, the sales.
#
# The resulting dict should be: {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}

# print(
#     dict(zip(years, sales))
# )


# Challenge #11
#
# Consider the dictionary from the previous challenge.
#
# Create a new dictionary called profit that stores the profit of the company, if the profit margin is 25% of the sales.
#
# Use dictionary comprehension if possible.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #12
#
# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].
#
# Create a set that contains the elements of the 2 lists in pairs.
#
# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #13
#
# Consider the two Python lists. Write a Python Script to make a new list whose elements are the intersection of the two given lists. This means all elements of L1 that also belong to L2, but no other elements.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #14
#
# Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".
#
# If the email is not valid the script should display why it's not valid.
#
# We consider a valid email address if:
#
# it has at least 6 characters but no more than 16.
#
# it contains both . and @
#
# it does not contain any of the following characters:'[]{}()$*'
#
# x = 10
#
# def my_func(x = 2):
#     #global x
#     #x = 15
#     print(f"x inside the function: {x}")
#
# my_func()
# print(x)

#
# result = lambda x: x ** 2
# print(result(2))

# def perfect_number(x):
#     divisors = []
#     for i in range(1, x):
#         if x % i == 0:
#             divisors.append(i)
#
#     if sum(divisors) == x:
#         return f"{x} is a perfect number"
#     else:
#         return f"{x} is not a perfect number"
#
#
# print(
#     perfect_number(496)
# )
#
# def factorial(n):
#     result = 1
#     if n <= 1:
#         return 1
#     for x in range(1, n+1):
#         result *= x
#
#     return result
#
# print(
#     factorial(5)
# )
#
# def isPrime(n):
#     if n <= 0:
#         raise ValueError
#     for x in range(2, n // 2):
#         if n % x == 0:
#             return f"{n} is not prime"
#     else:
#         return f"{n} is prime"
#
# for x in range(2, 100):
#     print(isPrime(x))












