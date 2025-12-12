
num1= int(input("numberm for Q!= "))
a= int(input("number 1 for Q2= "))
b= int(input("number 2 for Q2= "))
c= int(input("number 3 for Q2= "))
num3= int(input("number for Q3= "))
#Q1-> number is odd or even
if(num1%2==0):
    print("Even")
else: 
    print("odd")

#Q2-> greatest of 3 numbers entered by the user
if(a>b & a> c):
    print("a is greatest")
elif(b>c & b>a):
    print("b is greatest")
else:
    print("c is greatest")

#Q3-> number is divisible by 7
if(num3 % 7 ==0):
    print("number is divisible by 7")
else:
    print("Number is not divisible by 7")
