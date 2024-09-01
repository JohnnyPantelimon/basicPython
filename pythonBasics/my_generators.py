class Dog:

    def __str__(self):
        return "My Dog"


d = Dog()
print(d)

# from collections import Counter
#
# myList = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
#
# print(Counter("aaaaaaassssssssssssddddddddddddddffffffffff"))
# print(Counter(myList))


# import random
#
#
# def gensquares(n):
#     for x in range(1, n + 1):
#         yield x ** 2
#
#
# g = gensquares(4)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
#
# def rand_num(low, high, n):
#     for i in range(n):
#         yield random.randint(low, high)
#
#
# print(rand_num(5, 20, 1))
#
#
# s = "hello"
#
# g = iter(s)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
