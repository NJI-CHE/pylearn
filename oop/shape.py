# Python program that calculates area and perimeter based om
#various shapes

import math



class Shape:
    def calculate_area(self):
        pass

    #placeholder method for calculating area to be implemenrted in 
    #derived class
    def calculate_perimeter(self):
        pass

    #Placeholder method for calculating perimiter

# we now create derived classes
#Derived class called a circle  which inheris from the parent class
class Circle(Shape):
    #initilize the circle object with given radius
    def __init__(self, radius):
        self.radius = radius

    #calculate and return the area of the circle
    def calculate_area(self):
        return math.pi*self.radius**2
    
    #calculate and return perimeter
    def calculate_perimeter(self):
        return 2*math.pi * self.radius
    

#Derived class called rectangle which inherits from shape class
class Rectangle(Shape):
    #Initilaise the rectangle object

    def __init__(self, length, width):
        self.length = length
        self.width = width

    #Calculate and return area
    def calculate_area(self):
        return self.length * self.width
    
    #Calculate and return perimeter
    def calculate_perimeter(self):
        return 2 * (self.length  + self.width)
    
#Derived triangle class
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    #calculate and return area
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    #calculate and retun perimeter
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
#Example usage
#create a circle object with a given radius and calculate its areas
#perimeter
r = 7
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimiter = circle.calculate_perimeter()

print("Radius of the Circle: ",r )
print("Circle Area: ", circle_area)
print("Circle Perimeter: ", circle_perimiter)
        
        