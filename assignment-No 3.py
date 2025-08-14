def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent/100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

#No2- Get the user input
original_price= float(input("Enter original price of item:"))
discount_percent = float(input("Enter discount percentage:"))

final_price= calculate_discount(original_price, discount_percent)
print("The final price of this item is:", final_price)