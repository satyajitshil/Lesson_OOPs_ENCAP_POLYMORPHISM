from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither")

class Horse(Animal):
    def move(self):
        print("I can trot")

x = Human()
x.move()
y = Snake()
y.move()
z = Horse()
z.move()