#defining class and initializing init method
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        
    #calculating average and grade methods
    def calculate_average(self):
        if self.marks != 0:
            avg = sum(self.marks) / len(self.marks)
            return avg
        else:
            return 0
        
    #grade determination method
    def calculate_grade(self):
        avg = self.calculate_average() #calling the average method
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"
        
    #displaying student report method   
    def display_details(self):
        print("\n--- Student Report Card ---")
        print(f"ID:      {self.student_id}")
        print(f"Name:    {self.name}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade:   {self.calculate_grade()}")
        print("---------------------------")

#getting user input and creating object
def get_student_input():
    print("Welcome to the Student Management System")
    
    
    #Get marks as a list
    marks_list = []
    #checking for valid input
    try:
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        num_subjects = int(input("How many subjects? "))
        for i in range(num_subjects):
            mark = int(input(f"Enter mark for subject {i+1}: "))
            marks_list.append(mark)
            
        #Creating object and display
        new_student = Student(id, name, marks_list)
        new_student.display_details()
        
    except ValueError:
        print("Invalid input! Please enter proper details")
    finally:
        print("Thank you for using the Student Management System")

#calling the function to execute
get_student_input()