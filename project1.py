from abc import ABC, abstractmethod
class Abclass(ABC):
    def print(self,x):
        print("Output:-",x)
    @abstractmethod
    def task(self):
        print("We are inside an abstract class task.")

class thing_class(Abclass):
    def task(self):
        print("We are inside the text class.")

o = thing_class()
o.task()
o.print(67)