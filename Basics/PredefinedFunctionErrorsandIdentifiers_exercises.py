"""
PYTHON FUNDAMENTALS
Pre-defined Functions, print(), Modules, Errors, and Identifiers
===============================================================

Goal:
    Build a strong foundation for Python interviews and practical coding.

How to use this file:
    1. Read each section.
    2. Run the examples.
    3. Try the exercises yourself first.
    4. Check the solutions at the end.

IMPORTANT:
    This file intentionally stays focused on the current topic.
"""

# =============================================================================
# 1. PRE-DEFINED FUNCTIONS
# =============================================================================

"""
A pre-defined function is a function that already exists and can be used.

For this topic, two important categories are:

1. Built-in functions
   Available directly in Python.
   Examples: print(), input(), len(), type(), int(), str()

2. Functions from modules
   A module contains reusable Python code.
   Examples: math.sqrt(), math.factorial()
"""

print("\n--- 1. BUILT-IN FUNCTIONS ---")

name = "Ihsan"

print(name)          # Display output
print(len(name))     # Count characters
print(type(name))    # Show data type


# input() always returns user input as a string.
# Uncomment to test:
# user_name = input("Enter your name: ")
# print("Hello,", user_name)


# =============================================================================
# 2. THE print() FUNCTION
# =============================================================================

"""
Basic syntax:

    print(*objects, sep=' ', end='\n')

Key arguments:

sep:
    Controls the separator between multiple values.
    Default: one space

end:
    Controls what is printed after the output.
    Default: newline (\n)
"""

print("\n--- 2. PRINT FUNCTION ---")

# Default behavior
print("Hello")
print("Ihsan")

# Multiple values: default separator is a space
print("Hello", "Ihsan")

# Change the separator
print("Hello", "Ihsan", sep="@@")
print(2026, 8, 24, sep="-")

# Change the ending character
print("Hello", end=" ")
print("Ihsan")

# A practical example
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")


# =============================================================================
# 3. FUNCTIONS DEFINED IN MODULES
# =============================================================================

"""
A module is a Python file containing reusable code.

The math module provides mathematical functions.

Common import styles:

    import math
    from math import sqrt
    import math as m

For readability in professional code, avoid wildcard imports:
    from math import *
"""

print("\n--- 3. MODULE FUNCTIONS ---")

import math

print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120
print(math.ceil(4.2))      # 5

# Another import style:
from math import sqrt

print(sqrt(25))            # 5.0

# Alias:
import math as m
print(m.pi)


# =============================================================================
# 4. FUNCTION ARGUMENTS AND RETURN VALUES
# =============================================================================

"""
This is important for understanding pre-defined functions.

Arguments:
    Values passed into a function.

Return value:
    The value produced by a function.

Example:
    math.sqrt(16)

    sqrt -> function
    16   -> argument
    4.0  -> return value

Some functions, such as print(), are mainly used for side effects
(displaying output) and return None.
"""

print("\n--- 4. ARGUMENTS AND RETURN VALUES ---")

result = math.sqrt(81)
print("Square root:", result)

print_result = print("print() returns:", print("Hello"))
# The inner print displays Hello.
# The outer print shows that print() returns None.


# =============================================================================
# 5. ERRORS IN PYTHON
# =============================================================================

"""
For this topic, focus on two major categories:

1. Syntax Errors
2. Runtime Errors (Exceptions)

Important interview point:
    Not every invalid-looking statement is a SyntaxError.
    Python may successfully parse code and fail only during execution.
"""


# -----------------------------------------------------------------------------
# 5.1 SYNTAX ERROR
# -----------------------------------------------------------------------------

"""
A SyntaxError occurs when Python code breaks the language grammar.

Python cannot correctly parse the program.

Example:

    if 5 > 2
        print("Hello")

The colon after the condition is missing.

The example is commented out because a SyntaxError would stop this file
from running.
"""

# if 5 > 2
#     print("Hello")


# -----------------------------------------------------------------------------
# 5.2 RUNTIME ERRORS / EXCEPTIONS
# -----------------------------------------------------------------------------

"""
A runtime error occurs while the program is executing.

Common exceptions for beginners:

    ZeroDivisionError
    NameError
    TypeError
    ValueError
    IndexError
    KeyError
"""

print("\n--- 5. RUNTIME ERRORS ---")

# ZeroDivisionError
# a = 5
# b = 0
# print(a / b)

# NameError
# prn("Hello")

# IMPORTANT CORRECTION:
# prn("Hello") is NOT a SyntaxError.
# It is a NameError because Python can parse the statement,
# but the name 'prn' is not defined.

# ValueError
# number = int("hello")

# TypeError
# print("Age: " + 20)

# IndexError
# values = [10, 20]
# print(values[5])


# =============================================================================
# 6. BASIC EXCEPTION HANDLING
# =============================================================================

"""
Understanding exceptions is useful even at this introductory stage.

Use try/except when an operation may fail at runtime.

Do not use a broad except just to hide every problem.
Catch the specific exception when possible.
"""

print("\n--- 6. EXCEPTION HANDLING ---")

try:
    number = 10
    divisor = 2
    print(number / divisor)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# =============================================================================
# 7. IDENTIFIERS
# =============================================================================

"""
Identifiers are names used to identify Python objects such as:

    variables
    functions
    classes
    modules

Examples:

    student_name
    calculate_total
    Employee
"""


# Valid identifiers
student_name = "Ihsan"
age2 = 20
_private_value = 100
TOTAL_SCORE = 100

print("\n--- 7. IDENTIFIERS ---")
print(student_name, age2, _private_value, TOTAL_SCORE)


"""
Rules for identifiers:

1. Must start with a letter or underscore (_).
2. Cannot start with a number.
3. Can contain letters, numbers, and underscores.
4. Cannot contain spaces.
5. Cannot use special characters such as @, #, or $.
6. Cannot use Python keywords.
7. Identifiers are case-sensitive.

Examples:

    age       -> valid
    age2      -> valid
    _age      -> valid
    2age      -> invalid
    student-name -> invalid
    class     -> invalid because it is a keyword
"""


# Invalid examples -- kept as comments so this file can run.
# 2age = 20
# student-name = "Ihsan"
# class = "Python"


# =============================================================================
# 8. IDENTIFIER NAMING CONVENTIONS
# =============================================================================

"""
Professional Python naming conventions:

Variables and functions:
    snake_case

Classes:
    PascalCase

Constants:
    UPPER_CASE

Private/internal convention:
    _single_leading_underscore

Examples:
"""

student_age = 22


def calculate_total(price, quantity):
    return price * quantity


class StudentRecord:
    pass


MAX_CONNECTIONS = 100


# Avoid unclear names:
x = 100

# Prefer meaningful names:
total_price = 100


# Avoid overwriting built-in function names:
# list = [1, 2, 3]       # Bad practice
# str = "Hello"          # Bad practice
# print = "Something"    # Bad practice


# =============================================================================
# 9. QUICK INTERVIEW CHECK
# =============================================================================

print("\n--- 9. QUICK INTERVIEW CHECK ---")

questions_and_answers = [
    (
        "Q1. What are the two main types of pre-defined functions covered here?",
        "Built-in functions and functions imported from modules."
    ),
    (
        "Q2. What is the default value of sep in print()?",
        "A single space."
    ),
    (
        "Q3. What is the default value of end in print()?",
        "A newline character (\\n)."
    ),
    (
        "Q4. What does math.sqrt(16) return?",
        "4.0"
    ),
    (
        "Q5. What is the difference between a SyntaxError and a runtime exception?",
        "A SyntaxError prevents Python from parsing/running the program correctly. "
        "A runtime exception occurs while executing code."
    ),
    (
        'Q6. What error does prn("Hello") produce?',
        "NameError, because prn is not defined."
    ),
    (
        "Q7. Can an identifier start with a number?",
        "No."
    ),
    (
        "Q8. Are age and Age the same identifier?",
        "No. Python is case-sensitive."
    ),
    (
        "Q9. Why should you avoid naming a variable list?",
        "It overwrites/shadows the built-in list name in the current scope."
    ),
    (
        "Q10. What is a function argument?",
        "A value passed to a function."
    ),
    (
        "Q11. What is a return value?",
        "The value produced by a function."
    ),
]

for question, answer in questions_and_answers:
    print(question)
    print("Answer:", answer)
    print()


# =============================================================================
# 10. PRACTICAL EXERCISES
# =============================================================================

"""
Try these without looking at the solutions first.
"""


# Exercise 1
# Print your first name and last name on the same line using end.
#
# Expected idea:
# Ihsan Qureshi


# Exercise 2
# Print the values 10, 20, and 30 separated by " | ".
#
# Expected output:
# 10 | 20 | 30


# Exercise 3
# Import the math module and calculate the square root of 144.


# Exercise 4
# Import only factorial from the math module and calculate factorial(6).


# Exercise 5
# Which of these are valid identifiers?
#
# user_name
# 2users
# _score
# total-price
# True
#
# Write your answers in comments.


# Exercise 6
# Predict the output:
#
# print("Python", "Developer", sep="-", end="!")
# print(" Ready")
#
# Then run it to verify.


# Exercise 7
# Identify the error type:
#
# a = 10
# b = 0
# print(a / b)


# Exercise 8
# Identify the error type:
#
# print(unknown_variable)


# Exercise 9
# Write a try/except block that safely handles division by zero.


# Exercise 10 - Practical mini task
# Create a small program that:
# 1. Imports math.
# 2. Stores a number.
# 3. Prints its square root.
# 4. Prints the result with a custom message.
#
# Example:
# Input number: 49
# Output: Square root of 49 is 7.0


# =============================================================================
# 11. EXERCISE SOLUTIONS
# =============================================================================

print("\n--- 11. EXERCISE SOLUTIONS ---")

# Solution 1
print("Ihsan", end=" ")
print("Qureshi")

# Solution 2
print(10, 20, 30, sep=" | ")

# Solution 3
print(math.sqrt(144))

# Solution 4
from math import factorial
print(factorial(6))

# Solution 5
# user_name    -> valid
# 2users       -> invalid
# _score       -> valid
# total-price  -> invalid
# True         -> invalid (keyword/reserved literal)

# Solution 6
print("Python", "Developer", sep="-", end="!")
print(" Ready")
# Output: Python-Developer! Ready

# Solution 7
# ZeroDivisionError

# Solution 8
# NameError

# Solution 9
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")

# Solution 10
number = 49
square_root = math.sqrt(number)
print(f"Square root of {number} is {square_root}")


# =============================================================================
# 12. JOB-READINESS CHECKLIST FOR THIS TOPIC
# =============================================================================

"""
For interviews and production-quality beginner Python code, make sure you can:

[ ] Explain built-in functions vs module functions.
[ ] Use print(), input(), len(), type(), int(), and str().
[ ] Explain sep and end without memorizing blindly.
[ ] Import modules using import and from ... import ...
[ ] Explain arguments and return values.
[ ] Distinguish SyntaxError from runtime exceptions.
[ ] Recognize common exceptions such as NameError and ZeroDivisionError.
[ ] Write a simple try/except for a specific exception.
[ ] Apply identifier rules correctly.
[ ] Use meaningful snake_case variable and function names.
[ ] Avoid shadowing important built-in names.

TOP-COMPANY INTERVIEW TIP:
Do not only memorize definitions. Be able to:
    1. Predict code output.
    2. Identify the error and explain WHY it occurs.
    3. Fix the code.
    4. Write a small example from scratch.
"""
