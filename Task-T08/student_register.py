"""
Follow these steps:
● Create a file called student_register.py.
● Write a program that allows a user to register students for an exam venue.
● First, ask the user how many students are registering.
● Create a for loop that runs for that number of students.
● Each time the loop runs the program should ask the user to enter the
next student ID number.
● Write each of the ID numbers to a text file called reg_form.txt.
● Include a dotted line after each student ID because this document will be
used as an attendance register, which the students will sign when they
arrive at the exam venue.

"""

#ask the user how many students are registering
num_students = int(input("How many students are registering: "))


with open("reg_form.txt", "w") as file:
    file.write("Registration Form\n")
    file.write("-------------------------------------------\n")
    file.write("Student ID" +"\t"+ "| Register Time |" + "\t" + "Signature | " + "\n")

# create a for loop that runs for that number of students
for i in range(num_students):
    # each time the loop runs the program should ask the user to enter the next student ID number
    student_id = input("Enter the student ID number: ")
    # write each of the ID numbers to a text file called reg_form.txt
    with open("reg_form.txt", "a") as file:
        file.write(student_id + "\n")
    # include a dotted line after each student ID because this document will be used as an attendance register
    with open("reg_form.txt", "a") as file:
        file.write("......................................\n") 
