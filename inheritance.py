class vehicle :
    def __init__(self,brand):
        self.brand=brand
        
    def start(self):
        print(f"{self.brand} vehicle is starting ")

class car (vehicle):
    def play_radio(self):
        print("playing radio")
        
v= vehicle ("nissan")
v.start()

d= car("toyota")
d.start()              # inherited method
d.play_radio()           # own method 