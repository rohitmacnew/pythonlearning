print("Starting my Python journey")

a = 2+5j
l1 = a, type(a) 
print("Type of variable")
print(l1)

# Airthmetic Ops
a,b = 10, 20
l2 = a+b, a-b, a*b, a/b, b-a, b/a
print("Airthmetic Ops")
print(l2)

# Relational Ops
l3 = a>b, a<b, a==b, a!=b
print("Relational Ops")
print(l3)

# Logical Ops
a = True
b = False
l4 = a&a, a&b, b&b, a|a, a|b, b|b
print("Logical Ops")
print(l4)

# String Ops
myString = "I am Rohit Moond"
print("String Ops")
print(myString[5:])
print("Length of string =",len(myString))
print(myString.lower())
print(myString.upper())
print(myString.replace('I',"Yo! I"))
print(myString.count('o'))
print(myString.find("Moond"))
l5 = myString.split()
print(l5)

# Tuple
tup1 = (1,'a',True,2,'b',False)
print(tup1, type(tup1))
print(tup1[2:5])
