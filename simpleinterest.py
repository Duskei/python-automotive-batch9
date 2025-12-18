#code to find out the simple interest by importing the operations from another file
from calc import add,mul,div

p=float(input("enter the principle amount: "))
r=float(input("enter the rate: "))
t=float(input("enter the time: "))
value= mul(p,r,t)
SI=div(value,100)
print("The simple interest is: ", SI)
amount= add(SI,p)
print("The final amount is: ", amount)