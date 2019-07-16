from oops import Employee
print(__name__)

emp3 = Employee('q',45000)
print(emp3.salary)
print(emp3.isworkingDay())
Employee.setBonus(15000)
print(emp3.bonus)