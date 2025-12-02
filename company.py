
import sqlite3
conn=sqlite3.connect("my4.db")
cursor=conn.cursor()
#create table
cursor.execute("CREATE TABLE IF NOT EXISTS employee(id INT PRIMARY KEY , name VARCHAR(100) , role VARCHAR(50) , salery INT)")

def insert_employe():
    name=input("enter your name: ")
    role=input("enter your job role:")
    salery=float(input("enter your salery:"))
    cursor.execute("INSERT INTO employee(name,role,salery) VALUES (?,?,?)",(name,role,salery))
    print("employe is added")
    
def view_employe():
    cursor.execute("SELECT * FROM employee")
    rows=cursor.fetchall()
    print("employee")
    if rows:
        for row in rows :
            print(row)
    else:
        print("no result found")
        
#def update_employe():
def delete_employe():
    empid=input("enter employe id to delete")
    cursor.execute("DELETE FROM employee WHERE id=?,(empid)")
    if cursor.rowcount:
        print("delete successfully")
    else:
        print("employe not found")
        
        
def menu():
    while True :
        print("employee")
        print("insert")
        print("view employee")
        print("update employee")
        print("delete")
        print("exit")
        choice=input("enter your choice 1-6 :")
        if choice == "1":
            insert_employe()
        elif choice=="2":
            view_employe()
        elif choice =="3":
            update_employe()
        elif choice=="4":
            delete_employe()
        elif choice=="5":
            print("exiting...")
            break
        else:
            print("invalid syntax")        
        
menu()
conn.close()

print("database connection is closed")

        
    
    