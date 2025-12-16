#this code implements all the string manipulation 
#%s is used for converting any datatype into string
# %.2f is used to get the result upto 2 decimal places 
# %d is used for integers

product= "laptop"
price= 45000
discount= 1000.25
total_cost= price- discount
print(f"The price of a %s is Rs.%d. But with a discount it is Rs.%.2f" %(product,price,total_cost))
print("\n")

#grocery list
fruits= 5
costs= 11.34
total= costs * fruits
print(f"Your total amount is %f" %total)
