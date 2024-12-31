"""
Follow these steps:
● Create a new Python file called numbers.py.
● Ask the user to enter three different integers.
● Then print out:
○ The sum of all the numbers
○ The first number minus the second number
○ The third number multiplied by the first number
○ The sum of all three numbers divided by the third number
Be sure to place files for submission inside your task folder and click "Request
review" on your dashboard

"""

# Ask the user to enter three different integers


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#print the results

#print the sum of all the numbers
print(f"The sum of all numbers is: {num1}+{num2}+{num3}=", num1 + num2 + num3)

#print the first number minus the second number
print(f"The first number minus the second number is:{num1}-{num2}=", num1 - num2)

#print the third number multiplied by the first number
print(f"The third number multiplied by the first number is:{num3}x{num1}=", num3 * num1)

#print the sum of all three numbers divided by the third number
print(f"The sum of all three numbers divided by the third number is:({num1}+{num2}+{num3})/{num3}=", (num1 + num2 + num3) / num3)