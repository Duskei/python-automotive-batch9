# code to implement a simple to-do list in python

print("To get the max, min of two numbers or swap them as per user choice")
print(" 1. get max \n 2. get min \n 3. swap the numbers ")

#takes the input from the user using the input function
a,b= map(int, input("enter two numbers: ").split(","))

#takes input of the user's choice
ch= int(input("Enter your choice: "))
if(ch==1):
    print("Max number is: ", max(a,b))
elif(ch==2):
    print("Min number is: ", min(a,b))
elif(ch==3):
    a,b= b,a # swaps the numbers
    print("After swapping:", a, " ", b)
else:
    print("Wrong choice.")