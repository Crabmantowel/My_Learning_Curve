# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]
#
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side", i + 1, "is", self.sides[i])
#
#
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 3)  # super().__init__(3)
#
#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#         print('The area of the triangle is %0.2f' % area)
#
#
# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 2)
#
#     def findArea(self):
#         a, b = self.sides
#         s = a * b
#         print(f'The area of the rectangle is {s}')
#
#
# rect = Rectangle()
# rect.inputSides()
# rect.findArea()

#TASK ONE
#Створити клас машина з атрибутами name,  make, model та методами start та
#stop, які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.


# class Vehicle():
#     def __init__(self, name, make, model):
#         self.name = name
#         self.make = make
#         self.model = model

#     def start(self):
#         print(f"The car - {self.name} {self.model}  made in  {self.make} started")

#     def stop(self):
#         print(f"The car - {self.name} {self.model}  made in  {self.make} stopped")


# car_itself = Vehicle("Mercedes", "Germany", "S 500 e")
# car_itself.start()
# car_itself.stop()

#TASK TWO
#Створити клас особа,  в якому конструктор встановлює ім’я, а метод info
#виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”,
#а також створити клас автомобіль,  в якому конструктор встановлює ім’я, а
#метод move виводить повідомлення


# class Person():
#     def __init__(self):
#         self.name = input("Enter your name: ")

#     def info(self):
#         print(f"Hello, my name is {self.name}")


# class Auto():
#     def __init__(self):
#         self.name = input("Enter your's car name: ")

#     def move(self):
#         print(f"Hello, my name is {self.name}")
