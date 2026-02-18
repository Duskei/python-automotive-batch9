import re

#parent class
class Students:
    def __init__(self):
        # Taking input from the user and splitting by commas or spaces
        user_input = input("Enter student IDs (e.g., std_001, std_002): ")
        # Clean the input into a list of strings
        self.student_ids = [s.strip() for s in re.split(r'[,\s]+', user_input) if s]
        #splits and check for extra spaces and removes them
        #.strip() removes accidental extra spaces

#child class
class Qualifying(Students): #inherits from Students(parent class)
    def __init__(self):  
        super().__init__() #super() is used to call the init constructor from the parent class
        #two lists to store student ids
        self.q1 = []  # even
        self.q2 = []  # odd
# ---------------------------------------------2---------------------------------------------
    def sort_students(self):
        for sid in self.student_ids:
            # here re.search is to find the first location of the numeric part
            match = re.search(r'\d+', sid) #\d+ matches digits that include [0-9], '+' means one or more digits
            if match:
                num = int(match.group()) # .group() is used to get the actual string
                # Condition: Even goes to q1, Odd goes to q2
                if num % 2 == 0:
                    self.q1.append(sid)
                else:
                    self.q2.append(sid)
# ---------------------------------------------3---------------------------------------------
    def display_results(self):
        print("\n--- Qualifying Results ---")
        print(f"Q1 (Even IDs - Allowed to participate first): {self.q1}")
        print(f"Q2 (Odd IDs - Participating later): {self.q2}")

# Execution
qualifier = Qualifying()
#This creates an object named qualifier of the *Qualifying class.*

qualifier.sort_students()
#Calls the sort_students() method
#This method:
#Goes through each student ID entered by the user
#Extracts the number part using regex

qualifier.display_results()
#Displays the final result:
#Students allowed in Q1 (Even IDs)
#Students allowed in Q2 (Odd IDs)

# Example Input: std_001, std_002, std_003, std_004, std_005, std_006, std_007, std_008, std_009, std_010