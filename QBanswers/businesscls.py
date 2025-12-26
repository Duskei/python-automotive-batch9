class BusinessUtility:
    def calculate_margin(self, revenue,cost):
        self.revenue= revenue
        self.cost= cost
        if revenue <=0:
            return 0.0
        else:
            return ((revenue-cost)/revenue)*100 #regular_margin

class SeasonalBusinessUtility(BusinessUtility):
    def calculate_margin(self,revenue,cost):
        regular_margin= super().calculate_margin(revenue,cost)
        seasonal_margin= regular_margin + 10
        return seasonal_margin
    

class ProfitabilityChecker:
    def check_profitsbility(self, regular_margin):
        if regular_margin >= 10:
            print("Business is profitable")
        else:
            print("Business is not profitable")

#taking user input
revenue= float(input("Revenue: "))
cost= float(input("Cost: "))

bu= BusinessUtility()
sbu= SeasonalBusinessUtility()
checker= ProfitabilityChecker()

rm= bu.calculate_margin(revenue,cost) #regular margine
sm= sbu.calculate_margin(revenue,cost) #seasonal margin

print(f"Regular Margin: {rm:.2f}%")
print(f"Seasonal Margin: {sm:.2f}%")

checker.check_profitsbility(rm)
