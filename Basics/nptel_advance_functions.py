from math import *
print(log(3))
print(sqrt(4))
print(sin(45))
m  = 10
n = 5
divisor = (m%n == 0)
print(divisor)
print((not divisor))
print(type( not divisor))

num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcd(a,b):
    if(a%b == 0):
        return b
    else:
        gcd(b,a%b)
if gcd(num,num2):
    print("GCD found")
else:
    print("GCD not found")


