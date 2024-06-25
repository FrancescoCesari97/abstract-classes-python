
# * Abstract class: A class that cannot be instantiated on it's own; meant to be subclassed.
# *###############  They can contain abstract methods, which are declared but have no implementation.
# *###############  Abstract classes benedits:
# *###############  1. Prevents instantiation of the class itself
# *###############  2. Requires children to use inherited abstract methods 

from abc import ABC, abstractmethod

class Veichle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Veichle):
    
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Veichle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
