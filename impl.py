#following is a calculator code that uses 

def calc(num1, num2, ch):
    if(ch==1):
        return num1 + num2
    elif(ch == 2):
        return abs(num1- num2)
    elif(ch==3):
        return num1 * num2
    elif(ch==4):
        if(num2 != 0):
            return num1/num2
        else:
            print("Wrong input")
    else:
        print("Wrong choice.")

#function to check the score in a subject 
def checkscore(a):
    if(a>=60):
        print("passed in physics")
    else:
        print("failed in physics")

num1= int(input("enter num1: "))
num2= int(input("enter num2: "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

ch= int(input("enter choice of operation: "))
print("result is: ",calc(num1, num2, ch)) # calling the calc function

score=int(input("Enter score in physics: "))
checkscore(score) # calling the checkscore function