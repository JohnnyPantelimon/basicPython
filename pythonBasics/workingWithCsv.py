import json
import requests
from pprint import pprint
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url=url)

results= response.json()


with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\airtravel.csv", "w", newline="") as f:
    writer = csv.writer(f,  delimiter=",", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(("Name", "City", "Lat/Lng", "Company"))
    for item in results:
        writer.writerow((item["name"], item["address"]["city"], (item["address"]["geo"]["lat"], item["address"]["geo"]["lng"]), item["company"]["name"]))


# url = "https://jsonplaceholder.typicode.com/todos"
#
# response = requests.get(url)
# obj = json.loads(response.text)
#
# #content = response.json()
#
# results = []
#
# for item in obj:
#     if item["completed"]:
#         results.append(item)
#
# pprint(results)



# friends = {
#     "Dan": [
#         20, "London", 3234342
#     ],
#     "Maria": [
#         25, "Madrid", 43525222
#     ]
# }
#
# with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\friends.json", "w") as f:
#     json.dump(friends, f)
#


# import csv
#
# # with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\airtravel.csv", "r") as f:
# #     content = csv.reader(f)
# #     for line in content:
# #         print(line[0], line[1], line[2], line[3])
#
# toWrite = [("Name", "Age", "Location"), ("Ionut", 38, "Ashford")]
# with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\myWriter.csv", "w+", newline="") as f:
#     writer = csv.writer(f)
#     for line in toWrite:
#         #writer.writerow(line)
#         writer.writerows(toWrite)

# import pickle
#
# friends = {
#     "Dan": [
#         20, "London", 3234342
#     ],
#     "Maria": [
#         25, "Madrid", 43525222
#     ]
# }
#
# with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\friends.dat", "wb") as f:
#     pickle.dump(friends, f)
#
#
# with open(r"E:\DataEngineer\The Complete Python Bootcamp 2024\files\friends.dat", "rb") as f:
#     obj = pickle.load(f)
#     print(type(obj))
#     print(obj)

