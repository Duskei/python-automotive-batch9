#code to implement division operation
a= int(input("Enter a number: ")) # asking the user to input a number
b= int(input("Enter another number: ")) # asking the user to input a number

#checking error conditions
if(b==0):
    print("Wrong input")
else: 
    res= a/b

print("The result is: " ,res)


