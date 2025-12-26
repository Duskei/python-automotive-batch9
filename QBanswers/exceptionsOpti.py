'''1. put everything inside the try block
2. take the input as a string first to check for special characters
3. then convert it into an integer to check for values less than 0
4. then split the list and check for any special characters
4. then check the entire list for any weird numbers
5. calculate the sum using the sum func and the average in the same line
6. print the average of the numbers
7. write the except block for any missed out exception '''
try:    
    n = input("Enter number of elements: ")
    
    # Using a negative check within the string validation
    if not n.isdigit():
        print("you must enter numeric value")
        exit()
    
    n = int(n)
    if n < 0:
        print("length of a list must be a non-negetive integer")
        exit()

    # Optimization: Using a list comprehension to gather inputs in one block
    # This replaces the manual for-loop with a more "Pythonic" one-liner
    nums = []
    for i in range(n):
        value = input()
        # Unique check: validation using the strip method to handle negative signs
        if not value.lstrip('-').isdigit():
            print("Error: You must enter a numeric value.")
            exit()
        nums.append(int(value))

    # Using a Ternary Operator for the average calculation
    # This handles the zero-case and calculation in a single expressive line
    average = sum(nums) / n if n > 0 else 0.00

    # Output using f-string with explicit precision
    print(f"{average:.2f}")

except Exception:
    # This remains as a safety net for any unhandled runtime errors
    print("Error: You must enter a numeric value.")
    