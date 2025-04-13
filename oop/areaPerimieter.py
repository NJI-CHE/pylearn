#import the math module to access mathematical function such as pi
import math

#Define a class called Circle torepresent circle
class Circle:
    #Initialise the Circle object with a given radius
    def __init__(self, radius):
        self.radius  = radius

    #Calculate Area
    def CalAreas(self):
        return math.pi*self.radius**2
    
    #Calculate the perimeter
    def calPerimeter(self):
        return 2 * math.pi *self.radius
    


#Prompt user to input the radius
radius = float(input("INput the radius of the circle: "))

#Create a circle object with the provide radius
circle = Circle(radius)

#Calculate the area of the circle using calAreas
area = circle.CalAreas()

#Calculate perimeter using calPerimeter
perimeter = circle.calPerimeter()


#Display the areas and perimeter
print("Area of the circle: ", area)
print("Perimeter of the circle: ", perimeter)
