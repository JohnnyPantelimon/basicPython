# f = open("../../files/configuration.txt")
# content = f.read(5)
# print(content)
#
# content = f.read(3)
# print(content)
#
# print(f.tell())
# f.seek(2)
# print(f.read(2))
# f.close()


# with open("../../files/configuration.txt") as f:
#     content = f.read().splitlines()
#     print(content)
#
# with open("../../files/configuration.txt") as f:
#     content = [line.strip("\n") for line in f.readlines()]
#     print(content)
#
# with open("../../files/configuration.txt") as f:
#     content = list(f)
#     print(content)
# ips = list()
# user = list()
# passw = list()
# file = list()
#
# with open("../../files/devices.txt") as f:
#     content = [line.strip("\n") for line in f.readlines()][1:]
#     for line in content:
#         ips.append(line.split(":")[1])
#         user.append(line.split(":")[2])
#         passw.append(line.split(":")[3])
#         file.append(line.split(":")[4])
#
#     print(
#         list(zip(ips, user, passw, file))
#     )

# Challenge #1
#
# Consider this text file that contains multiple duplicate MAC addresses.
#
# Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.

# with open("../../files/mac_addresses.txt") as f:
#     results = set()
#     content = f.read().splitlines()
#     for line in content:
#         for item in line.split(" "):
#             results.add(item)
#
# with open("../../files/mac_addreses_cleaned.txt", "a") as f:
#     for item in results:
#         f.writelines(item+"\n")

# Challenge #2
#
# Create a Python script that reads a text file into a list and then converts the list into a string that
# has the entire file content.
#
# Click to download a sample text file.

# with open("../../files/file.txt") as f:
#     content = [word.strip("\n") for word in f.readlines()]
#     results = [item for item in content if len(item) > 0]
#     with open("../../files/results.txt", "w") as ff:
#         for result in results:
#             ff.write(result+"\n")




# Challenge #3
#
# Create a Python script that removes all empty lines including those that contain only spaces from a file.
#
# Click to download a sample text file.

# with open("../../files/scripting.txt", "r") as f:
#     content = f.read().splitlines()[-5:]
#     print("\n".join(content))


# Challenge #4
#
# Create a Python function called tail that reads the last n lines of a text file. The function has two arguments:
# the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
#
# Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
#
# Click to download a sample text file.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #5
#
# Change the solution from the previous challenge so that the script that prints out the last n lines of the file
# refreshes the output every 3 seconds (as the file changes or updates). This is similar to the tail -f Linux command.
#
# Click to download a sample text file.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #6
#
# Write a Python program to count the number of lines, words, and characters in a text file. This is similar to the Linux `wc` command. Create a function, if possible.
#
# Click to download a sample text file.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #7
#
# Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in a text file.
#
# The file format is as follows:
#
# D:50
#
# W:100
#
# D means deposit while W means withdrawal.
#
# Suppose that the following file is supplied to the program:
#
# D:300
#
# D:300
#
# W:500
#
# D:200
#
# Then, the output should be: 300
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #8
#
# Write a Python script that compares line by line two text files and displays the lines that differ.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #9
#
# Consider this dictionary file.
#
# Write a Python script that reads the file in a dictionary. The words in the file will be the dictionary keys and the length of each word the corresponding values.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #10
#
# Consider the dictionary file from the previous challenge.
#
# Write a Python script that finds the first 100 longest words in the file.
#
# Tip: See how to get a sorted view of a dictionary.
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #11
#
# Consider this dictionary file.
#
# Write a Python script that finds the number of occurrences of each letter of the alphabet in all the words of the dictionary. Make a distinction between lower and uppercase letters.
#
# You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on appear in all the words in the dictionary.
#
# Which is the most frequently used letter in English words? But the least frequently used one?
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #12
#
# Change the solution from the previous challenge so that the script considers all letters lowercase (it makes no distinction between lower and uppercase letters).
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #13
#
# Continue the previous challenge and find the 3 most frequently used letters in all English Words.
#
# You should get: ('e', 67681), ('s', 50872), ('i', 50818)


import sys
sys.path.append(r"E:\DataEngineer\The Complete Python Bootcamp 2024\basicPython\mylibrary")

from functions import add

print(add(2,5))









