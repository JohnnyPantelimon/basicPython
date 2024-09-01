import sqlite3

conn = sqlite3.connect("my_database")

cursor = conn.cursor()

# sql = """
#     create table person(
#         id INT,
#         name varchar(50),
#         age int,
#         phone varchar(50)
#     )
# """
# values = (1, "Ionut", 38, "07472933956")
#
# sql = """insert into person(id, name, age, phone)
#         VALUES (?, ?, ?, ?)
# """

sql = """Select * from person"""

cursor.execute(sql)

for row in cursor.fetchall():
    print(row[0], row[1], row[2], row[3])

conn.commit()
conn.close()