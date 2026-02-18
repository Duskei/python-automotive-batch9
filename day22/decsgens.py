# below is the cpde for decorators
print("Here is example for Decorators:")
def make_shout(func):
    def wrapper():
        # 1. Get the original result from the function
        original_result = func()
        
        # 2. Modify that result (make it uppercase)
        modified_result = original_result.upper()
        
        # 3. Return the modified version
        return modified_result
    return wrapper

@make_shout #decorating the function
def get_status():
    return "engine is running smoothly" 

print(get_status()) 
# Output: ENGINE IS RUNNING SMOOTHLY
print("\n")
print("Here is example for Generators:")
#below is the code for generators
def count_up_to(max_number):
    count = 1
    while count <= max_number:
        yield count  # Pause here and give the value
        count += 1   # Resume from here when asked again

# Create the generator object
counter = count_up_to(3)

print(next(counter)) # Output: 1
print(next(counter)) # Output: 2
print(next(counter)) # Output: 3