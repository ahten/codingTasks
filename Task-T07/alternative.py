"""

Follow these steps:
● Create a file called alternative.py.
● Write a program that reads in a string and makes each alternate
character into an uppercase character and each other alternate character
a lowercase character.
E.g.: The string “Hello World” would become “HeLlO WoRlD”
● Now, try starting with the same string but making each alternative word
lowercase and uppercase.


"""

# function for alternating uppercase and lowercase
def alternative(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string

# taking input from user
string = input("Enter a string: ")

# printing the output
print(alternative(string))


# function for alternating lowercase and uppercase in words
def alternative_words(string):
    new_string = ""
    words = string.split()
    #print(words)

    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return " ".join(words)

# taking input from user
string = input("Enter a string: ")

# printing the output
print(alternative_words(string))
