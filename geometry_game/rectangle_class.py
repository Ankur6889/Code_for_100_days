from point_class import Point
import random 

class Rectangle:
    
    def __init__(self,blc,trc):
        self.bottom_left_corner = blc
        self.top_right_corner = trc 
    
    def area_of_rectangle(self):
        return ((self.top_right_corner.x_cordinate - self.bottom_left_corner.x_cordinate)*(self.top_right_corner.y_cordinate - self.bottom_left_corner.y_cordinate))
    
    def rectangle_cordinate(self):
        print(f"Bottom Left ({self.bottom_left_corner.x_cordinate},{self.bottom_left_corner.y_cordinate}) and Top Right ({self.top_right_corner.x_cordinate},{self.top_right_corner.y_cordinate})")
    
    @staticmethod
    def get_random_rectangle():
        point1 = Point(random.randint(0,200),random.randint(0,200))
        point2 = Point(random.randint(100,400),random.randint(100,400))
        return Rectangle(point1,point2)
        
    def visualize_rectangle(self):
        import turtle 
        myturtle = turtle.Turtle() # create an instance of turtle 
        myturtle.penup() # in order to sort the problem below we turn off the pen of the turtle 
        myturtle.goto(self.bottom_left_corner.x_cordinate,self.bottom_left_corner.y_cordinate) # move turtle to certain co-ordinate but this will create a line from the current position of the turtle to the given position
        myturtle.pendown() # This will again turn on the pen
        myturtle.forward(self.top_right_corner.x_cordinate - self.bottom_left_corner.x_cordinate) # moved turtle 100 from centre 
        myturtle.left(90) # turned turtle 90 degree towards left 
        myturtle.forward(self.top_right_corner.y_cordinate-self.bottom_left_corner.y_cordinate) # again moved turtle 200 from its position 
        myturtle.left(90)
        myturtle.forward(self.top_right_corner.x_cordinate - self.bottom_left_corner.x_cordinate)
        myturtle.left(90)
        myturtle.forward(self.top_right_corner.y_cordinate - self.bottom_left_corner.y_cordinate)
        turtle.done()
