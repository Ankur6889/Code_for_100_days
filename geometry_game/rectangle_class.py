from point_class import Point

class Rectangle:
    
    def __init__(self,blc,trc):
        self.bottom_left_corner = blc
        self.top_right_corner = trc 
    
    def area_of_rectangle(self):
        return ((self.top_right_corner.x_cordinate - self.bottom_left_corner.x_cordinate)*(self.top_right_corner.y_cordinate - self.bottom_left_corner.y_cordinate))
    
    def rectangle_cordinate(self):
        print(f"Bottom Left ({self.bottom_left_corner.x_cordinate},{self.bottom_left_corner.y_cordinate}) and Top Right ({self.top_right_corner.x_cordinate},{self.top_right_corner.y_cordinate})")
    