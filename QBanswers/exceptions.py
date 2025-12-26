try:    
    n= input("Enter number of elements: ")
    if not n.isdigit():
        print("you must enter numeric value")
        exit()
    n=int(n)
    if n<0:
        print("length of a list must be a non-negetive integer")
        exit()
    nums=[]
    for i in range(n):
        value = input()
        if not value.lstrip('-').isdigit():
            print("Error: You must enter a numeric value.")
            exit()
        nums.append(int(value))
    # Calculate average
    if n == 0:
        average = 0.00
    else:
        average = sum(nums) / n

    # Print result
    print(f"{average:.2f}")

except Exception:
    print("Error: You must enter a numeric value.")



                    
        