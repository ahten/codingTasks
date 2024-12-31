import sqlite3

db = sqlite3.connect('task22.db')

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER,
    name TEXT,
    grade INTEGER)
""")

db.commit()

grade_record = [(55, 'Carl Davis',61),(66,'Dennis Fredrickson',88),(77,'Jane Richards',78),(12,'Peyton Sawyer',45),(2,'Lucas Brooke',99)]

cursor.executemany("""
INSERT INTO python_programming (id, name, grade)
VALUES (?,?,?)
""", grade_record)


#cursor.execute("""
#INSERT INTO python_programming (id, name, grade)
#VALUES (55, 'Carl Davis', 61),
#       (66,'Dennis Fredrickson', 88),
#        (77,'Jane Richards', 78),
#        (12,'Peyton Sawyer', 45),
#        (2,'Lucas Brooke', 99)
#""")


db.commit()

# check result 1
cursor.execute("""
SELECT *
FROM python_programming
""")

print('Check original data')
for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT *
FROM python_programming WHERE grade >=60 and grade <=80
""")

print('Grade between 60 and 80')
for row in cursor.fetchall():
    print(row)


cursor.execute("""
UPDATE python_programming
SET grade = 65 WHERE name = 'Carl Davis'
""")
db.commit()

# check result 3
cursor.execute("""
SELECT *
FROM python_programming
""")

print('Check Carl Davis data')
for row in cursor.fetchall():
    print(row)


cursor.execute("""
DELETE FROM python_programming
WHERE name = 'Dennis Fredrickson'
""")
db.commit()

# check result 4
cursor.execute("""
SELECT *
FROM python_programming
""")

print('Check Dennis Fredrickson data')
for row in cursor.fetchall():
    print(row)


cursor.execute("""
UPDATE python_programming
SET grade = 80 WHERE id>55
""")
db.commit()

# check result 5
cursor.execute("""
SELECT *
FROM python_programming
""")

print('Change grade to 80')
for row in cursor.fetchall():
    print(row)
