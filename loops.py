#code to implement while and for loops

while True:
    name= input("Enter your name: ")
    if name != "":
        break

phone_no= "123-456-7890"
for i in phone_no:
    if i == '-':
        continue
    print(i, end= " ")

for i in range (1,22):
    if i%2 == 0: 
        pass
    print(i)