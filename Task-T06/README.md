Task 1 - Holiday 

Objective:
+ Learn how to create a method/function; it reduce the duplicate code, we can reuse the code by calling the method. 

Task Details:
+ 1. Create a Python file called holiday.py. 
+ 2. Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car rental cost.
+ 3. First, get the following user inputs: 
+ + ○ city_flight: The city they will be flying to (you can create some options
for them. Remember, each city will have different flight costs).
+ + ○ num_nights: The number of nights they will be staying at a hotel.
+ + ○ rental_days: The number of days for which they will be hiring a car.
+ 4. Next, create the following four functions:
+ + ○ hotel_cost(): This function will take num_nights as an argument and
return a total cost for the hotel stay (you can choose the price per night
charged at the hotel). (Done)
+ + ○ plane_cost(): This function will take city_flight as an argument and
return a cost for the flight. Hint: use if/else statements in the function to
retrieve a price based on the chosen city. [Done]
+ + ○ car_rental(): This function will take rental_days as an argument and
return the total cost of the car rental (you can choose the daily rental
cost). (done)
+ + ○ holiday_cost(): This function takes three arguments: num_nights,
city_flight, and rental_days. Using these three arguments, call the
hotel_cost(), plane_cost(), and car_rental() functions with their
respective arguments, and finally return the total cost for the holiday.
+ 5. Print out all the details about the holiday in a way that is easy to read.
Try running your program with different combinations of input to show its
compatibility with different options.
