#this code is to check if a given number is an armstrong number
#armstrong number is:
#number= sum of cubes of individual digits
num= int(input("Enter a number: "))
d_num= num
soc=0
while(num != 0):
    digit= num % 10
    soc= soc+ (digit ** 3)
    num= num//10
if(soc == d_num):
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
    
