class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

p1=Person("hehe",20)
print(p1.name)
print(p1._Person__age)