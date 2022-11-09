class StockSpanner:
    """
        
        100 [80 [[60 70] 60 75]  85]
         1    1   1  2    1  4   6
      
    """
    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        res = 1
        
        while self.stocks and self.stocks[-1][0] <= price:
            res += self.stocks.pop()[1]
        self.stocks.append((price, res))
        
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)