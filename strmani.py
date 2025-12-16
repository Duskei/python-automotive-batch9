#this code implements the string formatting and string manipulation
#example 1
name= "Alice"
age = 30

print(f"Hello {name}! you are {age} years old")

#example 2
item_price= 19.99
item_count=5
total_cost= item_price * item_count
print(f"Your total amount is {total_cost:.2f} for {item_count} items.")

#example 3
#expression specifier for '=' for debugging
bugs= 'roaches'
count= 13
print(f"Debugging {bugs=} {count=}")