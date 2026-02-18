#substring = slicing
myStr= "abcdef ghijkl"
sub1= myStr[0:6] # from the beginning to the 7th index of the string
print(sub1)
sub2= myStr[7:] # from the 7th element till the end of the string
print(sub2)
sub3= myStr[:5] # first 6 elements
print(sub3)
sub4= myStr[10] # 10th element of the string - index starts from 0
print(sub4)
sub5= myStr[-5] # gives the last 5 elements  
print(sub5)

if 'a' in myStr:
    print("a is there")
    
word= myStr.split(" ")
print({word}) # comma ',' seperated values

print(myStr + 'm') # string in python is immutable 
#hence this string will no longer exit and a new string will be created