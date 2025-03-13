"""Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
Print the final price after applying the discount, or if no discount was applied, print the original price."""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_applied = price * (discount_percent / 100)
        return price - discount_applied
    else:
        return price

price = float(input("Enter the original price of item: "))
discount_percent = float(input("Enter the discount: "))

final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
    print(f"The final price of item after applying discount is: {final_price}.")
else:
    print(f'No discount was applied, final price of item is: {final_price}')
  
