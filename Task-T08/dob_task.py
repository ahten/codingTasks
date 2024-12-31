"""
Create a new Python file in the folder for this task, and call it dob_task.py.
● In your Python file, write a program that reads the data from the text file
provided (DOB.txt) and prints it out in two different sections: one for
names and another for birthdates, as shown in the format displayed
below:
Name
Orville Wright
Rogelio Holloway
Marjorie Figueroa
... etc.
Birthdate
21 July 1988
13 September 1988
9 October 1988
... etc.
Before submitting your task, test your program to ensure that it correctly reads
DOB.txt and outputs the data in the required format. This step verifies that the
file references are correct and that Python can access DOB.txt from the same
folder. You may need to move the DOB.txt file to the same directory as your
dob_task.py file to ensure proper access.
Note: Remember to ensure that the text folder is in the appropriate file directory
or Python won’t be able to find it when running your program. Get this right first
by running the example files, and then do the task.
Be sure to place files for submission inside your task folder and click ‘Request
review’ on your dashboard.




"""

# Name
with open("DOB.txt") as f:
    for line in f:
        print(line.strip().split()[0] + " " + line.strip().split()[1])
    print("\n") 

# Birthdate
with open("DOB.txt") as f:
    for line in f:
        print(line.strip().split()[2] + " " + line.strip().split()[3] + " " + line.strip().split()[4])
    print("\n") 