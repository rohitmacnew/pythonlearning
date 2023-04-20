"""
print("Starting my Python journey")

a = 2+5j
c1 = a, type(a) 
print("Type of variable")
print(c1)

# Airthmetic Ops
a,b = 10, 20
c2 = a+b, a-b, a*b, a/b, b-a, b/a
print("Airthmetic Ops")
print(c2)

# Relational Ops
c3 = a>b, a<b, a==b, a!=b
print("Relational Ops")
print(c3)

# Logical Ops
a = True
b = False
c4 = a&a, a&b, b&b, a|a, a|b, b|b
print("Logical Ops")
print(c4)

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
c5 = myString.split()
print(c5)

# Tuple
tup1 = (1,'a',True,2,'b',False)
print(tup1, type(tup1))
print(tup1[2:5])
tup2 = (4,'c')
print(tup1 +tup2)
print(len(tup1))
print(tup2*3)

# List
l1 = [1,'mon',3.14,True,3+5j]
print(l1, type(l1))
print(l1[1:4])
l1.pop()
print(l1)
l1.append("rom")
print(l1)
l1.reverse()
print(l1)
l2 = [1,97,8,4,44,32,8]
l2.sort()
print(l2)

# Dictionary
fruit = {'apple':50,'banana':20,'peach':60,'grapes':40}
print(fruit,type(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit.items())
fruit['mango'] = 80
fruit['apple'] = 100
print(fruit)
fruit2 = {'ganna':10,"panna":30}
fruit.update(fruit2)
print(fruit)
fruit.pop('ganna')
print(fruit)

# Set
s1 = {1,'a',1}
print(s1,type(s1))
s1.add('hello')
print(s1)
s1.remove(1)
print(s1)
s1.update([1,False,3,'yo',5])
print(s1)
s2 = {1,3,'yo',8}
print(s1.union(s2))
print(s1.intersection(s2))

# IF Statement
a = 10
b = 20
c = 30
if a>b & a>c :
    print("a is greates")
elif b>a & b>c :
    print("b is greatest")
else:
    print("c is grestest")
l1 = [1,2,3,4]
if l1[3]==5:
    l1[3] = l1[3]+10
else:
    l1[3] = l1[3]+20
print(l1)
"""
# Looping
i,n = 1,2
while i<=10:
    print(n,'*',i,'=',n*i)
    i = i+1
l1 = ['brown','black','pink']
l2 = ['panther','mulgi']
for i in l1:
    for j in l2:
        print(i,j)
