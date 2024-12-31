"""
Follow these steps:
● Create a new Python file for this task and call it manipulation.py. (Done)
● Ask the user to enter a sentence using the input() function. Save the user’s
response in a variable called str_manip. (Done)
● Explore the string methods in here to help you solve the problem below:
● Using this string value, write the code to do the following:
○ Calculate and display the length of str_manip.
○ Find the last letter in str_manip sentence. Replace every occurrence [Done]
of this letter in str_manip with ‘@’. (Done)
■ e.g. if str_manip = “This is a bunch of words”, the output would
be: “Thi@ i@ a bunch of word@”
○ Print the last three characters in str_manip backwards.
■ e.g. if str_manip = “This is a bunch of words”, the output would
be: “sdr”. (done)
○ Create a five-letter word that is made up of the first three characters
and the last two characters in str_manip. (Done)
■ e.g. if str_manip = “This is a bunch of words”, the output would
be: “Thids”.
Be sure to place files for submission inside your task folder and click "Request
review" on your dashboard.


"""

str_manip = input("Please enter a sentence: ")

# Calculate and display the length of str_manip


# Find the last letter in str_manip sentence and replace every occurrence of this letter in str_manip with '@'

last_letter = str_manip[-1]

# Print the last letter of the sentence
print ('The last letter of the sentence is:', last_letter)

#Print the new sentence after replacing the last letter with '@'
new_str_manip = str_manip.replace(last_letter, '@')

print ('The modified sentence is:', new_str_manip)

# Print the last three characters in str_manip backwards

print ('The last three characters in str_manip backwards are:', str_manip[-1:-4:-1])


#Create a five-letter word that is made up of the first three characters and the last two characters in str_manip

five_letter_word = str_manip[:3] + str_manip[-2:]

print ('The five-letter word is:', five_letter_word)
