#program to implement 2D lists in python

class1=["1", "2", "3", "4"] #for class 1 with roll no.s
class2=["5", "6", "7", "8"] #for class 2 with roll no.s
class3=["9", "10", "11", "12"] # for class 3 with roll no.s

school=[class1, class2, class3]

print(school)
print(school[1])
print(school[2][1]) #prints the value of the 2nd index of the 3rd list
print("The school has ",school[0]+school[1] + school[2])


