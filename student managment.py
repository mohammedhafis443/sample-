print("student managment")
class student :
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def grade (self):
        print(f"name is {self.name},age is {self.age},mark ={self.mark}")
student1=student("appu",19,169)
student2=student("alice",22,200)
student3=student("ammu",18,210)
student4=student("achu",21,390)


student1.grade()
student2.grade()
student3.grade()
student4.grade()
        
        
        