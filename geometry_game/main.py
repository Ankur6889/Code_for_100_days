import random 
from point_class import Point
from rectangle_class import Rectangle

# Generating Random points 
point1 = Point(random.randint(0,9),random.randint(0,9))
point2 = Point(random.randint(10,20),random.randint(10,20))

rectangle = Rectangle(point1,point2)
rectangle.rectangle_cordinate()

x = int(input("Enter the x co-ordinate :"))
y = int(input("Enter the y co-ordinate :"))

point = Point(x,y)
point.falls_in_rectangle(rectangle)
