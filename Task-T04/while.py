"""

Practical task 1
Follow these steps:
● Create a file called while.py.
● Write a program that continually asks the user to enter a number. (Done)
● When the user enters “-1”, the program should stop requesting the user
to enter a number. Please be aware that 0 is not a valid input. (Done)
○ Hint: think about how you might exit the loop if -1 is entered.
● The program must then calculate the average of the valid numbers
entered, excluding the -1 and 0. (Done)
● Use a while loop to achieve the continuous prompting and number
collection. (Done)
Be sure to place files for submission inside your task folder and click "Request review" on
your dashboard.



"""


# Ask user input a number



# Looping until user input is -1

user_input = 1
vaild_count = 0
total = 0
average = 0

while user_input != -1:
    user_input = int(input("Please enter a number: "))
    if user_input == -1:
        average = total / vaild_count
        print(f"Total valid numbers entered: {vaild_count}. The average is: {average}")
        break
    elif user_input == 0:
        print("Invalid input. Please enter a valid number.")
    else:
        vaild_count += 1
        total += user_input


"""
Option 2 , using a list to store the input value

user_input = 1
input_collection = []

while user_input != -1:
    user_input = int(input("Please enter a number: "))
    if user_input == -1:
        vaild_count = len(input_collection)
        total = sum(input_collection)
        average = total / vaild_count
        print(f"Total valid numbers entered: {vaild_count}. The average is: {average}")
        break
    elif user_input == 0:
        print("Invalid input. Please enter a valid number.")
    else:
        input_collection.append(user_input)



"""