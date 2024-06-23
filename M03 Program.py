class Vehicle():
    def __init__(self,type):
        self.type=type
class Automobile(Vehicle):
    def __init__(self,type,make,model,doors,roof):
        self.type=type
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof