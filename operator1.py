'''
x = 10
= is assignment operator
== equality or comparison operator and the value will be either true or false

'''
import math
r = int(input("enter the radius of circle\n"))
print(r)
Area = math.pi * r * r

print("ares of circle =",Area)

x = int(input("enter first number\n"))
y = int(input("enter second number\n"))
if x>y:
    print(x,"is greater")
else:
    print(y,"is greater")

square = x * x
print("square of a number =", square)

cube = y * y * y
print("cube of a number =", cube)

power1 = x ** y
print("power of", x, "=", power1)

xor = x ^ y
print("xor of numbers are", xor)

