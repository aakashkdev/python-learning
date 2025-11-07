from abc import ABC, abstractmethod

class Vehicle(ABC):                     # Abstract Class
    @abstractmethod
    def start(self):                    # Abstract Method (only declared)
        pass

class Car(Vehicle):
    def start(self):                    # Implementing method
        print("Car starts with key or push button.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick or self start.")

# Object Creation
v1 = Car()
v2 = Bike()

v1.start()
v2.start()
