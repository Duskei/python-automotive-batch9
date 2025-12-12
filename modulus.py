#code to implement modulus operation 

num= int(input("Enter a number: "))
m= int(input("Enter another number: "))

if(m==0):
    print("Wrong input: ")  
else: 
    mod_res= num%m
print("The output is: ", mod_res)