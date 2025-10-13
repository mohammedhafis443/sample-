class shape :
    def area(self):
        print("what is the area of rectangle?")
       # raise NotImplementedError("sub class implement area() method")
        
class rectangle :
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    
rec=rectangle(30,24)
print("area of rectangle ",rec.area())
    