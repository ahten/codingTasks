"""

● Create a new Python file in your folder for this task, and call it
hello_world.py.
● First, provide pseudocode as comments in your Python file, outlining
how you will solve this problem (you’ll need to read the rest of this
practical task first, of course).
● Now, inside your hello_world.py file, write Python code to take in a user’s
name using input() and then print out (output) the name.
● Use the same input and output approach to take in a user’s age and
print it out.
● Finally, print the string “Hello World!” on a new line. Note: The new line
will happen by default if you use a separate print statement to the one
you used immediately above to print out the age. This is because each
print statement automatically inserts an “enter”, or newline instruction,
at the end.
Be sure to place files for submission inside your task folder and click "Request
review" on your dashboard.


"""
"""
# Outline the steps to solve this problem

1. Take user's name as input using input() function.
2. Take user's age as input using input() function , and catch the error if the input is not a number.
3. Print the user's name using the print() function.
4. Print the user's age using the print() function.
5. Print the string "Hello World!" using the print() function.

# Code implementation

"""


# Taking user's name and age as input using input() function
name = input("Please enter your name: ")

#catch errors if the input is not a number
try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Age must be a number. Please input again")
    exit()

# Printing the user's name and age using formatted strings
print(f"Hello, {name}!")
print(f"Your age is {age}.")
print("Hello World!")


