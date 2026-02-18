#program to calculate the compound interest for the senior citizen
#the rate of interest is given already 8 years

#created a class name as SeniorCitizenCI

class SeniorCitizenCI:

    # Constructor
    def __init__(self, name, age, principal, time):
        self.name = name
        self.age = age
        self.principal = principal
        self.time = time
        self.rate = 8   # 8% per annum

    #show error message if user enters 0
    def validate_all(self):
        if self.principal <= 0 or self.time <= 0:
            raise ValueError("Principal and time must be positive values")
        if self.age < 60:
            raise ValueError("Interest applicable only for senior citizens")

    # Calculate compound interest
    def calculate_ci(self):
        return (self.principal * self.rate * self.time) / 100

    # Display interest
    def show_interest(self):
        try:
            self.validate_all()
            ci = self.calculate_ci()
            #Takes input from user
            print("\n----- ACCOUNT DETAILS -----")
            print("Account Holder Name:", self.name)
            print("Age:", self.age)
            print("Principal Amount:", self.principal)
            print("Time Period:", self.time, "years")
            print("Rate of Interest:", self.rate, "%")
            print("Compound Interest:", ci)

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Thank you! Visit again")


# -------- MAIN PROGRAM --------
try:
    name = input("Enter account holder name: ")
    age = int(input("Enter age: "))
    principal = float(input("Enter principal amount: "))
    time = int(input("Enter time period (years): "))

    account = SeniorCitizenCI(name, age, principal, time)
    account.show_interest()

except ValueError as e:
    print("Error: Invalid input! Please enter numeric values only.")