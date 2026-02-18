books= 10
prices= 500
book_name= "Intermezzo"
book_price= 600
print(f"The price of %s is %d" %(book_name, book_price))

total_price= books * prices
discount= 0.25*total_price
amount= total_price - discount
print(f"Your total is %d. Discount added is %.2f" %(total_price,discount))
print(f"New amount is :%.f" %amount)