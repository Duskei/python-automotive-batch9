y=str(3.5)
print(y)

#using range for a sequence of events in calculate program

#following is a calculator code that uses a user defined function

def calc(num1, num2, ch):
    if(ch==1):
        return num1 + num2
    elif(ch == 2):
        return abs(num1- num2)
    elif(ch==3):
        i=range(num2)
        mul=0
        for j in i:
            mul= mul+ num1 
        return mul
    elif(ch==4):
        div=0
        if(num2 != 0):
            k=range(num2)
            for l in k:
                div= div-num2
            return div
        else:
            print("Wrong input")
    else:
        print("Wrong choice.")

num1= int(input("enter num1: "))
num2= int(input("enter num2: "))
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
ch= int(input("enter choice of operation: "))
print("result is: ",calc(num1, num2, ch))

# calling the calc function
calc(num1, num2, ch) 