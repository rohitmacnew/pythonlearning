'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

import random
print(random.randrange(1, 10))

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

thislist = list(("apple", "banana", "cherry"))
print(thislist)
thislist.insert(2, "watermelon")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
for x in thislist:
  print(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Polymorphism

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, plane1):
  x.move()
'''
