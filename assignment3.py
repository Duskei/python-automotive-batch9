# ---------------------------------------------
# MARKS VALIDATION SYSTEM
# Team 6 Presentation Code
# ---------------------------------------------

# Tuple to store fixed subject names
subjects = (
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer Science",
    "English"
)

# Dictionary to store subject-wise marks
marks_dictionary = {}  # key=subject, value=marks

# List to store marks separately for calculations
marks_list = []        # will hold marks to calculate total, average, etc.

# Variables for calculations
total_marks = 0        # sum of all marks
average_marks = 0      # average of marks
highest_marks = 0      # highest mark
lowest_marks = 100     # lowest mark initialized to max possible

# Header for display
print("===================================")
print("       MARKS VALIDATION SYSTEM")
print("===================================")

# Loop to take marks input for each subject
for subject in subjects:
    valid_input = False   # flag to check if input is valid

    # Loop until a valid mark is entered
    while valid_input == False:
        marks = float(input(f"Enter marks for {subject} (0 to 100): "))  # take input

        # Validation check: marks must be between 0 and 100
        if marks >= 0 and marks <= 100:
            # Store valid marks in dictionary and list
            marks_dictionary[subject] = marks
            marks_list.append(marks)

            # Add marks to total
            total_marks = total_marks + marks

            # Update highest marks if current mark is greater
            if marks > highest_marks:
                highest_marks = marks

            # Update lowest marks if current mark is smaller
            if marks < lowest_marks:
                lowest_marks = marks

            valid_input = True   # mark input as valid to exit loop
        else:
            # Display error message for invalid input
            print("Invalid marks! Please enter values between 0 and 100.")

# Calculate average marks
average_marks = total_marks / len(marks_list)

# Pass or Fail decision based on average
if average_marks >= 40:
    result_status = "PASS"
else:
    result_status = "FAIL"

# Grade calculation based on average marks
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "F"

# ---------------------------------------------
# OUTPUT SECTION
# ---------------------------------------------

print("\n===================================")
print("           MARKS REPORT")
print("===================================")

# Display subject-wise marks
for subject in subjects:
    print(f"{subject:<20} : {marks_dictionary[subject]}")  
    # <20 ensures the subject name takes 20 spaces, aligned nicely

print("-----------------------------------")
print("Total Marks     :", total_marks)                 # display total
print("Average Marks   :", round(average_marks, 2))    # display average rounded to 2 decimals
print("Highest Marks   :", highest_marks)             # display highest marks
print("Lowest Marks    :", lowest_marks)              # display lowest marks
print("Result Status   :", result_status)             # display pass/fail
print("Grade Obtained  :", grade)                      # display grade
print("===================================")

print("\nProgram executed successfully.")  # final message
print("Presented by Team 6")                # team info