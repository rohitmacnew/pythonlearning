'''
# Check Even/Odd
num = int(input("Enter the number: "))
if num%2==0:
    print(num,"is Even")
else:
    print(num,"is Odd")

# Factorial
fact = 1
num = int(input("Enter a number: "))
if num <0:
    print("Please enter a non negative number")
elif num == 0:
    print("Factorial of 0 = 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of",num,"=",fact)
'''
