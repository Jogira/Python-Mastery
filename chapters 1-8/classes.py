from collections import namedtuple
from abc import ABCMeta, abstractmethod

# class Point:

#     default_color = "green"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"(Using defined str method:{self.x}, {self.y})"
#     # Factory method.

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

#     def __eq__(self, other):  # Overwrite the equality comparison.
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):  # Overwrite the equality comparison.
#         return ("Greater than? : " + str(self.x > other.x and self.y > other.y))

#     def __add__(self, other):
#         return Point(self.x + other. x, self.y + other.y)


# # point = Point()
# # print(isinstance(point, Point))
# # Instance variables can be changed on the fly.

# point = Point(1, 3)
# point3 = Point.zero()
# point2 = Point(5, 10)
# # print(point.default_color)
# # point.draw()
# # point2.draw()
# # Point.default_color = "Mint"

# # print(point.default_color)
# # print(point2.default_color)
# # Both do the same thing because we've redefined the str method.
# print(point)
# print(str(point))

# print(point == point2)
# print(point == point3)


# print(point < point2)
# print(point >  point3)
# print(point2 > point)

# pointSum = (point + point2)
# print(pointSum)

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     # Using a dictionary defined in the class to implement logic to it.
#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# print(cloud.__dict__)
# cloud["python"] = 10
# cloud.add("python")
# cloud.add("Python")
# cloud.add("Smarp")
# cloud.add("python")
# print(len(cloud))
# cloud.add("python")


# print(cloud.__TagC__tags)
# print(cloud["PythOn"])
# # len(cloud)
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # price = property(get_price, set_price)


# product = Product(10)
# print(product.price)
# class Animal:
#     def __init__(self):
#         print("Animal constructor.")
#         self.age = 1

#     def eat(self):
#         print("Eat")

# # Animal is the parent class. Mammal is the sub class.


# class Mammal(Animal):

#     def __init__(self):
#         super().__init__() #This calls upon the methods of the parent class.
#         print("Mammal constructor.")
#         self.weight = 2

#     def walk(self):
#         print("Walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# m = Mammal()
# m.eat()
# print(m.age)
# print(m.weight)

class Employee:
    def greet(self):
        print("Employee greet.")


class Person:
    def greet(self):
        print("Person greet.")

# Notice the ability to inherit from more than one base. Manager class will take the method
# the first method it comes across with a matching name. Manager.greet() will go to
# Employee.greet() first. If there isn't one, it'll go to Person.greet()

# Multiple inheritance can get tricky.
# class Manager(Employee, Person):
#     pass


# manager = Manager()
# manager.greet()


# #To define an abstract class, import from ABC and inherit from the ABC class.
# class exampleAbstract(ABC):
#     def __init__(self):
#         self.opened = False

#     @abstractMethod #This lets you know the class is abstract and you cannot direcltly call
#     # the read class for exampleAbstract. But the sub classes can.
#     def read(self):
#         pass

# class UIControl(metaclass=ABCMeta):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("Textbox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()


# #Polymorphism allows us to pass a list of objects and run them
# #all using the same method.
# ddl = DropDownList()
# print(isinstance(ddl, UIControl))
# # draw(ddl)
# ddl = DropDownList()
# textbox = TextBox()
# print(isinstance(ddl, UIControl))
# draw([ddl, textbox])


# This is duck typing because def draw will invoke the draw()
# function regardless of the type of the object calling it.
# class TextBox:
#     def draw(self):
#         print("Textbox")


# class DropDownList:
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()

# ddl = DropDownList()
# textbox = TextBox()
# draw([ddl, textbox])

# #We can also extend built in types. Here we're extending from the base class.
# class Text(str):
#     def duplicate(self):
#         return self + self

# class TrackableList(list):
#     def append(self, object):
#         #This way we can edit the default append function for lists.
#         #And call a print before the actually append happens.
#         print("Append called.")
#         super().append(object)

# text = Text("Python")
# print(text.duplicate())
# list = TrackableList()
# list.append("1")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# This a more compact way of defining classes that are entirely comprised of data.
# We can see here all we have to do is define a named tuple and don't even have to
# redefine the __eq__ class.
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
