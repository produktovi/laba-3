class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Ellip(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        print (3.14 *self.side1 * self.side2)
    def perimeter(self):
        print (2 * 3.14 * (((self.side1**2 + self.side2**2) / 2)*((self.side1**2 + self.side2**2) / 2)))
        
class Squar(Shape):
    def __init__(self, side1):
        self.side1 = side1
    def area(self):
        print (self.side1 * self.side1)
    def perimeter(self):
        print (self.side1 *4)
        
class Trapez(Shape):
    def __init__(self, lowside, upside, side1, side2, height):
        self.lowside = lowside
        self.upside = upside
        self.side1 = side1
        self.side2 = side2
        self.height = height
    
    def area(self):
        # (a + b) * h / 2 
        print (1/2*(self.lowside+self.upside))
    def perimeter(self):
        print (self.lowside+self.upside+self.side1+self.side2)
        

ellip = Ellip(3,5)
squar = Squar(7)
trapez = Trapez(3,5,4,5,6)

ellip.area()
ellip.perimeter()

squar.area()
squar.perimeter()

trapez.area()
trapez.perimeter()
