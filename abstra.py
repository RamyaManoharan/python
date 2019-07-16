from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass
class Circle(Shape):
    def getArea(self):
        return math.pi * 5 * 5
circle = Circle()
print(circle.getArea())