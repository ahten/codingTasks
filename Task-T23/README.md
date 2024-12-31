Task 1: SQL injection

Objective
+ Understanding the logic of SQL injection. Study how to do the injection. 

Task Details
+ ● Open up your task folder for this task. You will see many different files.
However, the only files that you will need to modify are input1.txt and
input2.txt.
+ ● input1.txt and input2.txt are inputs to input1.py and input2.py,
respectively. These files, input1.py and input2.py, create a SQL table
called Student and populate it with entries. Then, they perform their
respective tasks.
+ + ○ input1.txt: This file searches the database for a student with a
particular first_name.
+ + ○ input2.txt: This file logs a user onto the system. The two fields
required for login are the email address and student number.
+ ● However, these Python files have been set up for failure: You can use the
input files to inject your own SQL code! Modify the input files in the
following manner:
+ ○ input1.txt: Inject SQL code to delete all entries from the database.
+ ○ input2.txt: Inject SQL code to log yourself into the account using
the email address “wimbledon@strange.com”. Do this without
specifying the student ID.


---

Task 2: How to prevent SQL injection

Objective:
+ Learn how to enhance the code to prevent the SQL injection

Task Details
+ ● Create two new Python scripts: safe_input1.py and safe_input2.py. Copy
the code from input1.py and input2.py, and place each copied program
into its own respective new file.
+ ● Now modify the Python code to use prepared statements and ensure
that your SQL injections do not work.

