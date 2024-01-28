#!/bin/bash

# Prompting the user to enter two integers
echo "Enter the first integer:"
read num1

echo "Enter the second integer:"
read num2

# Calculating modulus and multiplication
modulus=$((num1 % num2))  # Calculate the modulus of num1 and num2
multiplication=$((num1 * num2))  # Calculate the multiplication of num1 and num2

# Displaying the results
echo "The modulus of $num1 and $num2 is $modulus."
echo "The multiplication of $num1 and $num2 is $multiplication."
