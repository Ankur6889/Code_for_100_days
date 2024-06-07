
class Point:
    
    def __init__(self,x,y):
        self.x_cordinate = x 
        self.y_cordinate = y
    
    def falls_in_rectangle(self,rectangle):
        if rectangle.bottom_left_corner.x_cordinate < self.x_cordinate < rectangle.top_right_corner.x_cordinate \
            and rectangle.bottom_left_corner.y_cordinate < self.y_cordinate < rectangle.top_right_corner.y_cordinate:
            print("Yes !! the point falls in rectangle")
        else: 
            print("Sorry !! the point does not fall in ractangle")
    