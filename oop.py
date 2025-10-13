# define class person
class person:
    def __init__(self,name,age):#initializing class
        self.name=name    #attribute
        self.age=age
    def greet (self):  # method
        print(f"hello,my name is {self.name},my age is {self.age}")
 # create object        
person1= person("alice",23)
person2=person("jabar",32)
person3=person("ammu",22)

person1.greet()
person2.greet()
person3.greet()
