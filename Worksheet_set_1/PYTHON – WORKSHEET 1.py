#!/usr/bin/env python
# coding: utf-8

# In[7]:


#11. Write a python program to find the factorial of a number.


num = int(input("Enter a number= "))

def factorial(n):
    if n < 0:
        return 
    elif n == 0:
        return 1 
    else:
        return n * factorial(n - 1)

result = factorial(num)
print(f"The factorial of {num} is: {result}")


# In[8]:


#12. Write a python program to find whether a number is prime or composite.

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 11
print(is_prime(n))


# In[9]:


#13. Write a python program to check whether a given string is palindrome or not.

def is_palindrome(s):
    
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

input_string = input("Enter a string to check if it is a palindrome: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


# In[10]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.

import math

def calculate_third_side(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))

third_side = calculate_third_side(side1, side2)
print(f"The length of the hypotenuse is: {third_side}")


# In[ ]:


#15. Write a python program to print the frequency of each of the characters present in a given string

def character_frequency(s):
    frequency = {}
    for char in s:
        char = char.lower()
        if char.isalnum():
            if char in frequency:
                frequency[char] += 1  # Increment count if character already exists
            else:
                frequency[char] = 1   # Initialize count to 1 if it's the first occurrence

    return frequency

input_string = input("Enter a string to count character frequencies: ")

freq = character_frequency(input_string)

print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")

