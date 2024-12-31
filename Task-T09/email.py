"""

In this task, we’re going to be creating an email simulator using OOP. Follow the
instructions and complete the logic to fulfil the program requirements below in
email.py.
● Open the file called email.py.
● Create an email class and initialise a constructor that takes in three
arguments:
○ email_address – the email address of the sender.
○ Subject_line – the subject line of the email.
○ email_content – the contents of the email.
● Inside the constructor, initialise the following instance variables:
○ email_address
○ subject_line
○ email_content
○ has_been_read (initialised to “False”).
● The email class should also contain the following instance method to edit
the values of the email objects:
○ Implement an instance method called mark_as_read() that sets the
has_been_read instance variable to “True”.
● Initialise an empty variable called inbox of type list to store and access the
email objects.
○ Note: You can have a list of objects




Create the following functions to add functionality to your email simulator:
○ populate_inbox() – A function that creates an email object with the
email address, subject line, and contents, and stores it in the inbox
list.
Note: At program start-up, this function should be used to populate
your inbox with three sample email objects for further use in your
program. This function does not need to be included as a menu
option for the user.
○ list_emails() – A function that loops through the inbox and prints
each email’s subject_line and a corresponding number. For
example, if there are three emails in the Inbox:
0 Welcome to HyperionDev!
1 Great work on the bootcamp!
2 Your excellent marks!
This function can be used to list the messages when the user
chooses to read, mark them as spam, and delete an email.
Tip: Use the enumerate() function for this.
○ read_email() – A function that displays a selected email, together
with the email_address, subject_line, and email_content, and then
sets its has_been_read instance variable to True.
For this, allow the user to input an index, such that read_email(i)
prints the email stored at position i in the inbox list. Following the
example above, an index of 0 will print the email with the subject
line “Welcome to HyperionDev!”
● Your task is to build out the class, methods, lists, and functions to get
everything working. Fill in the rest of the logic for what should happen
when the user chooses to:
1. Read an email
2. View unread emails
3. Quit application
Note: Menu option 2 does not require a function. Access the corresponding
class variable to retrieve the subject_line only.
● Keep the readability of print outputs in mind and take the initiative to
communicate with the user, making it clear to them what is being viewed
and what has been executed.
For example: print(f"\nEmail from {email.email_address} marked as
read.\n")


"""

#email class constructor
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  

    def mark_as_read(self):
        self.has_been_read = True



#populate_inbox function for creating email objects
def populate_inbox():
    inbox = [
        Email("oscar1@oscar.com ", "Email Subject 1", "This is a email content1"),
        Email("oscar2@oscar.com ", "Email Subject 2", "This is a email content2"),
        Email("oscar3@oscar.com ", "Email Subject 3", "This is a email content3"),
        Email("oscar4@oscar.com ", "Email Subject 4", "This is a email content4"),
        Email("oscar5@oscar.com ", "Email Subject 5", "This is a email content5")
    ]
    return inbox

#initialize an emapty variable called inbox
inbox = populate_inbox()

#list_emails function
def list_emails(inbox):
    print("-----------Listing emails-----------")
    print("-No.------Subject------Read---------")
    for i, email in enumerate(inbox):
        print(f"{i} {email.subject_line} {email.has_been_read}")
    print("------------------------------------")

#list unread emails
def list_unread_emails(inbox):
    print("-----------Listing emails-----------")
    print("-No.------Subject------Read---------")
    for i, email in enumerate(inbox):
        if email.has_been_read == False:
            print(f"{i} {email.subject_line} {email.has_been_read}")
    print("------------------------------------")

#read_email function
def read_email(inbox):
    index = int(input("Enter the index of the email to read: "))
    email = inbox[index]
    print(f"\nEmail from {email.email_address} marked as read.\n")
    email.mark_as_read()
    print(f"Subject line: {email.subject_line}\nEmail content: {email.email_content}\n")
    

#main function
def main():
    inbox = populate_inbox()
    #list the emails
    list_emails(inbox)
    while True:
        print("-----------Menu-----------")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        print("-------------------------")
        print("Please enter your choice (1,2,3): ")
        choice = input("Enter your choice: ")
        if choice == "1":
            list_emails(inbox)
            read_email(inbox)
        elif choice == "2":
            list_unread_emails(inbox)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


main()



