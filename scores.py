#code to take marks of two subjects and check if the student has passed of not
def checkscore(score1, score2):
    if(score1>=60 and score2>= 60):
        print("passed in all subjects")
    elif(score1>=60 or score2>=60):
        print("passed in 1 subject")
    else:
        print("failed in all subjects")


name= input("Enter your name: ")
score1=int(input("Enter score in sub1: "))
score2=int(input("Enter score in sub2: "))
checkscore(score1, score2) # calling the checkscore function