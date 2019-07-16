class book():
    def __init__(self, orderNo, bookTitle, Quantity, pricePerItem):
        self.orderNo = orderNo
        self.bookTitle = bookTitle
        self.Quantity = Quantity
        self.pricePerItem = pricePerItem
    
    def display(self):
        tup = (self.bookTitle,self.Quantity*self.pricePerItem)
        return tup

b1 = book(12354,'Computer Programming',5,449)
b2 = book(12355,'Programming for beginners',8,649)
b3 = book(12356,'Computer Basics',3,179)

print(b1.display())
print(b2.display())
print(b3.display())