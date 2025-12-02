balance=50000.00
def bank():
    print("banking app")
    print("cteate account")
    print("deposite")
    print("withdraw")
    print("check balence")

def createaccount():
    accno=(input("enter your account no:"))
    name=input("enter your name:")
    
    #balence=0.00#local variable
    print("created account succesfully")
    
def deposit():
    global balance
    acc_no=input("enter your account no:")
    amount=float(input("enter your amount:"))
    balance+=amount
    
    print("succesfully deposited:$",balance)
    
def withdraw():
    global balance
    acc_no=input("enter your account no:")
    balance-=amount
    print(amount)
    #balence=0
    print("withdraw amount succesfully:$",balance)
    
def checkbalance():
    acc_no=input("enter no:")
    print("your balance :",balance)
    
    #balence= deposite+amount
    print("check balance succesfully:$")
def banking():
    while True:
        bank()
        choice=input("enter your choice:")
        if choice=="5":
            print("exit")
            break
        if choice not in ["1","2","3","4"]:
            print("invalid")
            continue
        elif choice=="1":
            createaccount()
        elif choice=="2":
            deposit()
        elif choice=="3":
            withdraw()
        elif choice=="4":
            checkbalance()
banking()
            
        
            
        
        
    
    