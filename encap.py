class Mobile:
    def __init__(self):
        self._maxPrice = 9999
    def getPrice(self):
        print(self._maxPrice)
    def setPrice(self,price):
        self._maxPrice = price
class Developer(Employee):
    def __init__(self, stack):
        self.stack = stack
    
    def getStack(self):
        return self.stack
        
mobile = Mobile()
# print(mobile.maxPrice)
mobile.getPrice()
mobile.setPrice(10999)
mobile.getPrice()