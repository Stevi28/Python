# -*- coding: utf-8 -*-
"""prime_numbers.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BVx3DsRMiorFdc1KJXb3gk4ZsjSDrvcT
"""

# Function to check if a number is prime

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

# List to store prime numbers

prime_numbers = []

# Find prime numbers between 1 to 250

for num in range(1, 251):
  if is_prime(num):
    prime_numbers.append(num)

# Write prime numbers to results.txt file

with open('results.txt', 'w') as file:
  for prime in prime_numbers:
    file.write(str(prime) + '\n')

print('Prime numbers between 1 to 250 have been written to results.txt ')