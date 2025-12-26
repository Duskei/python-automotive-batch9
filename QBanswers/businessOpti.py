class BusinessUtility:
    def calculate_margin(self, revenue, cost):
        # Storing for record-keeping, but utilizing a ternary for the calculation
        self.revenue = revenue
        self.cost = cost
        
        # Unique approach: Using a single-line conditional expression
        return ((revenue - cost) / revenue) * 100 if revenue > 0 else 0.0

class SeasonalBusinessUtility(BusinessUtility):
    def calculate_margin(self, revenue, cost):
        # Using a shorthand assignment to combine the base logic and the boost
        seasonal_margin = super().calculate_margin(revenue, cost) + 10
        return seasonal_margin

class ProfitabilityChecker:
    def check_profitsbility(self, regular_margin):
        # Unique approach: Using a status variable and a single print statement
        status = "is profitable" if regular_margin >= 10 else "is not profitable"
        print(f"Business {status}")

# Input handling with a descriptive prompt
revenue = float(input("Enter Total Revenue: "))
cost = float(input("Enter Total Cost: "))

# Object instantiation
bu = BusinessUtility()
sbu = SeasonalBusinessUtility()
checker = ProfitabilityChecker()

# Calculation execution
rm = bu.calculate_margin(revenue, cost)
sm = sbu.calculate_margin(revenue, cost)

# Unique formatting: Using a multi-line f-string for a cleaner output dashboard
print(
    f"\n--- Financial Summary ---\n"
    f"Regular Margin:  {rm:>8.2f}%\n"
    f"Seasonal Margin: {sm:>8.2f}%\n"
    f"-------------------------"
)

# Logic check
checker.check_profitsbility(rm)