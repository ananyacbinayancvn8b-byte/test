from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def milage(self):
        pass
class defender(Car):
    def milage(self):
        print("the milage is 7kmpl")

class  diago(Car):
    def milage(self):
        print("the milage is 13kmpl")

class pajero(Car):
    def milage(self):
        print("the milage is 14KMPL")

d=defender()
d.milage()

i=diago()
i.milage()

p=pajero()
p.milage()
