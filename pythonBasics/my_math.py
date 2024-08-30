a = 10

def my_sum(*args):
    s = 0
    for item in args:
        s += item

    return s


if __name__ == "__main__":
    print("Message printed inside my_path.py")
    s = my_sum(10, 20, 30)
    print(f"sum calculated inside my_path.py is {s}")
else:
    print("This is the else block of code")
    print(f"__name__ inside my_math.py is {__name__}")