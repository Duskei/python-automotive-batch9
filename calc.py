#Code for importing the functions into another code

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return abs(num1- num2)
def mul(num1, num2, num3):
    return num1 * num2 *num3
    #for i in num2:
    #   product= product+i
     #   return product
def div(num1, num2):       
    if(num2 != 0):
        return num1/num2
    else:
        print("Wrong input")

#num1= int(input())
#num2= int(input())
#num3= int(input())