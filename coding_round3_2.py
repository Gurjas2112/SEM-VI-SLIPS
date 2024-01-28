#Write a Program for palindrome pattern printing in a half diamond with 'n' number of
#lines
#Example:INPUT:Enter n:7
#OUTPUT-
#*
#* 1 *
#* 1 2 1 *
#* 1 2 3 2 1 *
#* 1 2 1 *
#* 1 *
#*

def print_palindrome_pattern(n):
    # Upper half of the diamond
    for i in range(1, 4):
        # Print spaces before the numbers
        print("*", end=" ")

        # Print numbers in increasing order
        for j in range(1, i):
            print(j, end=" ")

        # Print numbers in decreasing order
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Print spaces after the numbers
        print("*")

    # Lower half of the diamond
    for i in range(4 - 1, 0, -1):
        # Print spaces before the numbers
        print("*", end=" ")

        # Print numbers in increasing order
        for j in range(1, i):
            print(j, end=" ")

        # Print numbers in decreasing order
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Print spaces after the numbers
        print("*")

# Get user input for the number of lines
n = int(input("Enter n: "))

# Print palindrome pattern
print_palindrome_pattern(n)


