"""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

Sample output:
The output should look like the sample below (where bold text represents user input).
This uses f-string formatting to set the currency to 2 decimal places.

"""

total_price = 0
item_number = int(input("Number of items: "))

# validate the user input number cannot be negative
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items: "))

# add up the total price and display each item price
for item in range(item_number):
    item_price = float(input("Price of item:"))
    total_price += item_price

# if total price is over 100, apply 10% discount
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {item_number} items is ${total_price: .2f} ")
