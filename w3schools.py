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

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
for x in thislist:
  print(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
'''
