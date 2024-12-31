"""

Follow these steps:
● Imagine you are running a café. Create a new Python file in your folder
called cafe.py.
● Create a list called menu, which should contain at least four items sold in
the café.
● Next, create a dictionary called stock, which should contain the stock
value for each item on your menu.
● Create another dictionary called price, which should contain the prices for
each item on your menu.
● Next, calculate the worth of the total_stock in the café. You will need to
remember to loop through the appropriate dictionaries and lists to do
this.
Tip: When you loop through the menu list, the “items” can be set as keys
to access the corresponding “stock” and “price” values. Each item_value is
calculated by multiplying the stock value by the price value. For example:
item_value = (stock[item] * price[item])
● Finally, print out the result of your calculation

"""


# create a list called menu
menu = ["americano", "tea", "espresso", "cappuccino"]
# create a dictionary called stock
stock = {"americano": 40, "tea": 30, "espresso": 20, "cappuccino": 10}
# create a dictionary called price
price = {"americano": 2.5, "tea": 2, "espresso": 3, "cappuccino": 3.5}
# calculate the worth of the total_stock in the cafe
total_value= 0
for item in menu:   
    item_value = (stock[item] * price[item])
    total_value += item_value
# print the result
print(total_value)

# Output: 255. 