import turtle 

myturtle = turtle.Turtle() # create an instance of turtle 
myturtle.penup() # in order to sort the problem below we turn off the pen of the turtle 
myturtle.goto(50,75) # move turtle to certain co-ordinate but this will create a line from the current position of the turtle to the given position
myturtle.pendown() # This will again turn on the pen
myturtle.forward(100) # moved turtle 100 from centre 
myturtle.left(90) # turned turtle 90 degree towards left 
myturtle.forward(200) # again moved turtle 200 from its position 
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
turtle.done()
