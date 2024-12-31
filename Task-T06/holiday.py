"""
1. Create a Python file called holiday.py. (Done)
2. Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car rental cost.
3. First, get the following user inputs: (Done)
○ city_flight: The city they will be flying to (you can create some options
for them. Remember, each city will have different flight costs).
○ num_nights: The number of nights they will be staying at a hotel.
○ rental_days: The number of days for which they will be hiring a car.
4. Next, create the following four functions:
○ hotel_cost(): This function will take num_nights as an argument and
return a total cost for the hotel stay (you can choose the price per night
charged at the hotel). (Done)
○ plane_cost(): This function will take city_flight as an argument and
return a cost for the flight. Hint: use if/else statements in the function to
retrieve a price based on the chosen city. [Done]
○ car_rental(): This function will take rental_days as an argument and
return the total cost of the car rental (you can choose the daily rental
cost). (done)
○ holiday_cost(): This function takes three arguments: num_nights,
city_flight, and rental_days. Using these three arguments, call the
hotel_cost(), plane_cost(), and car_rental() functions with their
respective arguments, and finally return the total cost for the holiday.
5. Print out all the details about the holiday in a way that is easy to read.
Try running your program with different combinations of input to show its
compatibility with different options.
Be sure to place files for submission inside your task folder and click "Request review"
on your dashboard.
11


"""

#ask user for the city_flight

#define the cost of each city ( prefer us list instead of if-elif to get the cost, to reduce the code)
city = [1,60,300,30], [2,70,400,25], [3,80,800,10], [4,100,1000,8] # [option][hotal cost][plane cost]

#greeking the user
print("Welcome to the Holiday Cost Calculator")

#ask the user to select the city
print("Please select the city you will be flying to, input 1 = London, 2 = Paris, 3 = Shanghai, 4 = Bangkok")

city_flight = int(input("Enter the city you will be flying to: "))

#error catching for invalid input and not integer

while city_flight < 1 or city_flight > 4 or not isinstance(city_flight, int):
    print("Invalid input. Please enter a number between 1 and 4.")
    city_flight = int(input("Enter the city you will be flying to: "))

#ask the user to input the number of nights they will be staying at a hotel

num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))

#error catching for invalid input and not integer

while num_nights < 1 or not isinstance(num_nights, int):
    print("Invalid input. Please enter a number greater than 0.")
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))

#ask the user to input the number of days they will be hiring a car

rental_days = int(input("Enter the number of days you will be hiring a car: "))

#error catching for invalid input and not integer

while rental_days < 1 or not isinstance(rental_days, int):
    print("Invalid input. Please enter a number greater than 0.")
    rental_days = int(input("Enter the number of days you will be hiring a car: "))

#create a functon to calculate the total cost of the hotel

def hotel_cost(location, num_nights):
    #get the cost of the hotel based on the location, from the city list.
    cost = city[location-1][1]
    #calculate the total cost of the hotel
    total_cost = cost * num_nights
    return total_cost

#create a function to calculate the plane cost

def plane_cost(location):
    #get the cost of the plane based on the location, from the city list.
    cost = city[location-1][2]
    #calculate the total cost of the plane
    total_cost = cost
    return total_cost

#create a function to calculate the car rental cost

def car_rental(rental_days,location):
    #calculate the total cost of the car rental
    total_cost = rental_days * city[location-1][3]
    return total_cost

#create a function to calculate the total cost of the holiday

def holiday_cost(num_nights, city_flight, rental_days):
    #calculate the total cost of the holiday
    total_cost = hotel_cost(city_flight, num_nights) + plane_cost(city_flight) + car_rental(rental_days,city_flight)
    return total_cost

#print out all the details about the holiday

print("The hotel cost is: ", hotel_cost(city_flight, num_nights))
print("The plane cost is: ", plane_cost(city_flight))
print("The car rental cost is: ", car_rental(rental_days,city_flight))
print("The total cost of the holiday is: ", holiday_cost(num_nights, city_flight, rental_days))