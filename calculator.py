def menu():
    print("calculator")
    print("1.addition")
    print("2.subraction")
    print("3.multiplication")
    print("4.division")

def add ():
    num1=int(input("enter number"))
    num2=int(input("enter number"))
    print(num1+num2)

def sub():
    num1=int(input("enter no"))
    num2=int(input("enter no"))
    print(num1-num2)

def multi():
    num1=int(input("enter number"))
    num2=int(input("enter number"))
    print(num1*num2)

def divi():
    num1=int(input("enter no"))
    num2=int(input("enter no"))
    print(num1/num2)

def calc():
    while True:
         menu()
         choice=input("enter your option")
         if choice=="5":
            print("good bye")
            break
         elif choice not in ["1","2","3","4"]:
             print("invalid option")
             continue 
         elif choice=="1":
            add()
         elif choice=="2":
            sub()
         elif choice=="3":
            multi()
         elif choice=="4":
            divi()
calc()



    
    
    
    
