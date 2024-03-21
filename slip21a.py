#Write a program to print whether a given number is Armstrong or not.  

def armstrong(n):
    temp = n
    sum = 0
    while n > 0:
        r = n % 10
        sum = sum + r ** 3
        n = n // 10
    if temp == sum:
        return True
    else:
        return False

n = input("Enter a number: ")
result = armstrong(int(n))
if result:
    print("Armstrong")
else:
    print("Not Armstrong")
