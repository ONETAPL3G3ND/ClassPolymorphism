#https://github.com/ONETAPL3G3ND
from functools import singledispatchmethod


class Petrol95:
    def __init__(self):
        ...

class Diesel:
    def __init__(self):
        ...

class Car:
    def __init__(self, name):
        self.Name = name
        self.Fuel = 0

    def StartEngine(self):
        if self.Fuel != 0:
            print("Engine started")
            return
        print("low gasoline level")

    @singledispatchmethod
    def FillCar(self, fuel):
        print("This fuel is not suitable")

    @FillCar.register
    def _(self, fuel: Petrol95):
        self.Fuel = 100
        print("The car is refueled")
    @FillCar.register
    def _(self, fuel: Diesel):
        self.Fuel = 100
        print("The engine is refueled, but does not work stably")


car = Car("Tesla")
car.StartEngine()

petrol = Petrol95()
diesel = Diesel()

car.FillCar("Other fuel")
car.FillCar(petrol)
car.FillCar(diesel)

car.StartEngine()




