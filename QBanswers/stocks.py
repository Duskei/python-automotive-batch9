
class stocks:
    def __init__(self,price):
        self.price = list(price) 
    
    def stock_prices(self):
        max_prof = 0
        for i in range(len(self.price)-1):
            for k in range(i+1, len(self.price)):
                prof = self.price[k] - self.price[i]
                if prof > max_prof:
                    max_prof = prof
        return max_prof

    def avg_volatiles(self):
        total_diff = 0
        for j in range(len(self.price)-1):
            total_diff += abs(self.price[j] - self.price[j+1])
        return total_diff / (len(self.price)-1)

price = list(map(int, input().split()))
stock = stocks(price)
print("max profit is:", stock.stock_prices())
print(f"volatility index is: {stock.avg_volatiles():.2f}")