class Car:
    numberOfWheels = 4
    _color = "Black" #Protected attribute
    __yearOfManufacture = 2017 #Private attribute

class BMW(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)

car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)

bmw = BMW()
print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)
# Note that for private attributes that call from the base class, it must be called in the following format: object._<baseclass>__<private-attribute>
