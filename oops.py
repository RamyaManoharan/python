# print('Hello World')
# for i in range(10):
#     print(i)
from datetime import datetime
class Employee():
    bonus = 5000
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary
    
    def applyHike(self):
        self.salary=self.salary*1.04
        return self.salary

    @classmethod
    def setBonus(cls, amount):
        cls.bonus = amount

    @staticmethod
    def isworkingDay():
        day = datetime.now().strftime('%w')
        if day=='0' or day =='6':
            return False
        else:
            return True
    
    def __str__(self):
        return self.name

    def __add__(self,other):
        return self.salary + other.salary

class Developer(Employee):
    def __init__(self, name, salary, stack):
        self.stack = stack
        super().__init__(name, salary)
    
    def getStack(self):
        return self.stack
        
if __name__ == "__main__":
    dev1 = Developer('q',123323,'python')
    print(dev1.getStack())
    print(dev1.getSalary())

    print(getattr(dev1,'salary'))
    setattr(dev1,'salary',1000)
    print(getattr(dev1,'salary'))
    delattr(dev1,'salary')
    print(dev1.__dict__)
    print(hasattr(dev1,'name'))
    emp1 = Employee('John',15000)
    emp2 = Employee('Ben',250000)

    print(emp1)
    print(emp2)
    print(emp1+emp2)

    print(emp1.salary)
    print(emp2.salary)
    print(Employee.getSalary(emp1))

    print(Employee.isworkingDay())
