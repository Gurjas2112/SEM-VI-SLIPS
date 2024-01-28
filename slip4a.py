#Write a Python Program to Check if given number is prime or not. Also find factorial of the given number using user defined function.

def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter a number:"))
if prime(n):
    print("Prime")
    print("Factorial:",fact(n))
else:
    print("Not Prime")
    print("Factorial:",fact(n))

