#import my_math
# if __name__ == "__main__":
#     print(my_math.a)
#     print(my_math.my_sum(2, 3, 4, 5, 6))

# import sys
#
# name = sys.argv[1]
# print("Hello {0}".format(name))

import os

# print(os.getcwd())
# print(os.listdir(os.getcwd()))
#
# print(os.path.getmtime(r"C:\Users\ionut\Downloads\airlines.json"))
#
# print(os.path.`)

# os.chdir(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files")
#
# i = 1
# for file in os.listdir():
#     file_name, file_ext = os.path.splitext(file)
#     #print(file_name, "=>", file_ext)
#
#     new_name = f"{str(i)}_new_{file_name}{file_ext}"
#     i += 1
#     #print(new_name)
#
#     print(f"Renaming {file_name} to {new_name}")
#     os.rename(file, new_name)



user = {"username": "js", "level": "admin"}


def only_admin(func):
    def wrapper_only_admin(*args, **kwargs):
        if user["level"] == "admin":
            return func(*args, **kwargs)

        else:
            raise PermissionError("permission denied")

    return wrapper_only_admin


def show_password():
    return "abcde1234"

checking = only_admin(show_password)
print(checking())





















