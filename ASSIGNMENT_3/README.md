# Python Math Programs

This repository contains two Python programs demonstrating basic mathematical operations: factorial calculation using recursion and calculations using the `math` module.  

---

## Program 1: Factorial Calculation Using Recursion

### Description
This program calculates the factorial of a non-negative integer using a recursive function. Factorial of a number `n` is the product of all positive integers less than or equal to `n`.

### How it Works
1. The program prompts the user to enter a number.
2. It checks if the number is negative. If yes, it returns an error message.
3. If the number is 0 or 1, it returns 1.
4. Otherwise, it recursively calculates the factorial by multiplying the number with the factorial of `(number - 1)`.

### Example
Enter a number: 5
120


---

## Program 2: Using the Math Module for Calculations

### Description
This program demonstrates the use of Python’s `math` module to perform basic mathematical calculations: square root, natural logarithm, and sine of a number.

### How it Works
1. The program prompts the user to enter a number.
2. It uses functions from the `math` module to calculate:
   - Square root (`math.sqrt`)
   - Natural logarithm (`math.log`)
   - Sine in radians (`math.sin`)
3. The results are displayed to the user.

### Example
Enter the number: 9
Square root : 3.0
Logarithm : 2.1972245773362196
Sine: 0.4121184852417566


---

## Requirements
- Python 3.x
- No additional libraries needed besides the built-in `math` module

---

## Author
[Kajal Dangi]

