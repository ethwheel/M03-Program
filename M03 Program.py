class Vehicle():
    def __init__(self,type):
        self.type = type
    def setType(self):
       self.type = input("What type of vehicle is it?: ")

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, door, roof):
        super().__init__(type)
    def setYear(self):
        self.year = input("What year is your vehicle?: ")
    def setMake(self):
        self.make = input("What make is it?: ")
    def setModel(self):
        self.model = input("What model?: ")
    def setDoor(self):
        self.door = input("How many doors does it have?: ")
    def setRoof(self):
        self.roof = input("Does it have a sun roof? (Y/N): ")
        if input == "Y":
            self.roof = "Sun roof"
        else:
            self.roof = "Solid"






vic = Vehicle(0)
for loop in range (1):
    vic.setType()
vic2 = Automobile(0,0,0,0,0,0)
for loop in range(1):
    vic2.setYear
    vic2.setMake
    vic2.setModel
    vic2.setDoor
    vic2.setRoof
print("Vehicle type: ",vic2.type)
print("Year: ",vic2.year)
print("Make: ",vic2.make)
print("Model: ",vic2.model)
print("Number of doors: ",vic2.door)
print("Type of roof: ",vic2.door)