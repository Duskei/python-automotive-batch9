# Create an empty list to store the 20 names
students = []

print("--- Enter each student's full name ---")

#Collect 20 names from the user
for i in range(1, 5):
    name = input(f"Enter name for student {i}: ")
    students.append(name) #adding that name to the list

# To find matches we use a dictionary "names" to store the key value pairs {FirstName: Surname}
# where key-> FirstName value-> Surname
names= {} 
# We use a set to make sure we print a duplicate only ONCE
already_present = set()

# Loop through the list to find matches
for full_name in students:
    # seperates the first name from the surname and stores in the list called parts
    parts = full_name.split(" ", 1) 
    
    # Check if there is a first and last name
    if len(parts) == 2:
        first = parts[0]
        last = parts[1]
        
        # If the first name is NOT in our storage, add it
        if first not in names:
            names[first] = last
        
        # If the first name IS in storage, check if the surname is different
        else:
            old_surname = names[first]
            if last != old_surname and first not in already_present:
                print(f"Match found: {first} {old_surname} and {first} {last}")
                # Add to reported set so we don't print this name again
                already_present.add(first)
    else:
        print("Missing surname. Enter full name")
