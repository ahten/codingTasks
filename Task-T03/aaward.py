"""
Follow these steps:
● Create a new Python file in this folder called award.py.
● Design a program that determines the award a person competing in a
triathlon will receive.
● Your program should read in user input for the times (in minutes) for all
three events of a triathlon, namely swimming, cycling, and running, and
then calculate and display the total time taken to complete the triathlon.
● The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.
Display the award that the participant will receive based on the following
criteria:


"""


# Get the value of each event from the user. 
swim_time = int(input("Enter swimming time (in minutes): "))
cycle_time = int(input("Enter cycling time (in minutes): "))
run_time = int(input("Enter running time (in minutes): "))

# Calculate total time
total_time = swim_time + cycle_time + run_time


# Display total time
print(f"Total time: {total_time} minutes")


# Determine award based on total time
if total_time <= 100:
    award = "Honorary Colours"
elif total_time <= 105:
    award = "Honorary Half Colours"
elif total_time <= 110:
    award = "Honorary scroll"
else:
    award = "No Award"

# Display total time and award
print(f"You got the {award} award!")