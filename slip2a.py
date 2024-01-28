#Write a program to print whether a given number is Palindrome or not.

def palindrome(number):
    temp=number
    rev=0
    while(number>0):
        rem=number%10
        rev=rev*10+rem
        number=number//10
    if(temp==rev):
        print("Palindrome")
    else:
        print("Not Palindrome")

number=int(input("Enter a number:"))
palindrome(number)
