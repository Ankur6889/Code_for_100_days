import random 
from point_class import Point
from rectangle_class import Rectangle

rectangle = Rectangle.get_random_rectangle()
rectangle.rectangle_cordinate()

x = int(input("Enter the x co-ordinate :"))
y = int(input("Enter the y co-ordinate :"))

point = Point(x,y)
point.falls_in_rectangle(rectangle)

rectangle.visualize_rectangle()