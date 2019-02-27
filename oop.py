#  #define class User
# class User:
#     # this method to run every time a new object is instantiated
#     def __init__(self, name, email):
# 	# instance attributes 
#         self.name = name
#         self.email = email
#         self.logged = True
#     # login method changes the logged status for a single instance (the instance calling the method)
# def login(self):
#         self.logged = True
#         print(self.name + " is logged in.")
#         return self
#     # logout method changes the logged status for a single instance (the instance calling the method)
# def logout(self):
#         self.logged = False
#         print(self.name + " is not logged in")
#         return self
#     # print name and email of the calling instance
# def show(self):
#         print("My name is {self.name}. You can email me at {self.email}.")
#         return self

# class bike:
#     def __init__(self, price, max_speed, miles=0):
#         self.price= price
#         self.max_speed= max_speed
#         self.miles= miles

#     def displayinfo(self):
#         print(self.price, self.max_speed, self.miles)
#         return self

#     def ride(self):
#         self.miles += 10
#         print("riding")
#         return self

#     def reverse(self):
#         self.miles -=5
#         if self.miles < 0:
#             self.miles=0
#         print("reversing")
#         return self


# bike1 = bike(200, "25mph").ride().ride().ride().reverse().displayinfo()


# file vehicles.py 
# class Vehicle:
#     def __init__(self, wheels, capacity, make, model):
#         self.wheels = wheels
#         self.capacity = capacity
#         self.make = make
#         self.model = model
#         self.mileage = 0
#     def drive(self,miles):
#         self.mileage += miles
#         return self
#     def reverse(self,miles):
#         self.mileage -= miles
#         return self
# class Bike(Vehicle):
#     def vehicle_type(self):
#         return "Bike"
# class Car(Vehicle):
#     def set_wheels(self):
#         self.wheels = 4
#         return self
# class Airplane(Vehicle):
#     def fly(self, miles):
#         self.mileage += miles
#         return self
# v = Vehicle(4,8,"dodge","minivan")
# print(v.make)
# b = Bike(2,1,"Schwinn","Paramount")
# print(b.vehicle_type())
# c = Car(8,5,"Toyota", "Matrix")
# c.set_wheels()
# print(c.wheels)
# a = Airplane(22,853,"Airbus","A380")
# a.fly(580)
# print(a.mileage)

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def show(self):
        print("Value: ", self.value, "Type: ", self.type)
class Deck:
    def __init__(self, name):
        self.deck = []
        self.name = name
        for i in ["clubs", "diamonds", "hearts", "spades"]:
            for j in range(1,14):
                self.deck.append( Card(j, i ) )
    def show(self):
        print("\n", "*"*30, self.name, "*"*30)
        for card in self.deck:
            card.show()
d1 = Deck("First Deck")
d1.show()
d2 = Deck("Second Deck")
d2.show()