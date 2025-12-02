import sqlite3

conn=sqlite3.connect("student.db")
cursor=conn.cursor()
#cursor.execute("CREATE TABLE students (id INT PRIMARY KEY , name VARCHAR(50) , mark INT )")
#insert
cursor.execute("INSERT INTO students ( id, name,mark) VALUES(1,'alice',30)")
cursor.execute("INSERT INTO students (id,name,mark) VALUES(2,'ammu',40)")
cursor.execute("SELECT * FROM students")
cursor.execute("DELETE FROM students WHERE name='ammu'")
cursor.execute("UPDATE students SET mark=50 WHERE name='alice'")
cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()
for row in rows :
    print(row)
conn.close()
print("database create successfully")