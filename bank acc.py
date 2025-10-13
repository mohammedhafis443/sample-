# BAnk Account
class bankaccount :
    def __init__(self,accountholder,balance): #attributes 
        self.accountholder=accountholder
        self.balance=balance
        
    def display(self) :    #method
        print(f"account holder {self.accountholder}\n balance=${self.balance}")
account1=bankaccount("anil ks",40000)
account2=bankaccount("Alice",350000)    #object

# calling
account1.display()
account2.display()
print("hi")


        
        
        
    
