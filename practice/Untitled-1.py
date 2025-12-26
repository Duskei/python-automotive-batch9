try:
    n= input("enter the length of the list: ")

    if not n.isdigit():
        print("You must enter a numeric value")
        exit()
    n= int(n)
    if n < 0:
        print("Length of a list must be a non-negetive integer")
        exit()
    nums=[]
    for i in range(n):
        value= input()
        if not value.lstrip('-').isdigit():
            print("You must enter a numeric value")
            exit()
        nums.append(int(value))
    
    avg= sum(nums)/ n if n > 0 else 0.00
    print(f"average is: {avg: .2f}")
except Exception:
    print("enter valid input only")
    