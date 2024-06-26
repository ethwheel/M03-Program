class Vehicle():
    def __init__(self,type):
        self.type = type
    def setType(self):
       self.type = input("Type a number: ")
vic = Vehicle(0)
for loop in range(2):
    vic.setType()
    print(vic.type)