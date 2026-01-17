from abc import ABC, abstractmethod
class Car:
    @abstractmethod
    def fuel_type(self):
        pass
    @abstractmethod
    def max_speed(self):
        pass

class BMW(Car):
    def fuel_type(self):
        print("Diesel Gasoline")
    def max_speed(self):
        print("500 mph")
    
class Ferrari(Car):
    def fuel_type(self):
        print("Premiem Gasoline")
    def max_speed(self):
        print("600 mph")

a = Ferrari()
a.fuel_type()
a.max_speed()
b = BMW()
b.fuel_type()
b.max_speed()
