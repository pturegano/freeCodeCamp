class Rectangle:
    def __init__(self, width, height = 0):
        self.width = width
        self.height = height
        if self.height == 0:
            self.height = width
       
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self): 
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return  (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height
    def get_amount_inside(self, shape):
        ret_width = self.width // shape.width
        ret_height = self.height // shape.height
        return ret_width * ret_height

    def __str__(self):
        return "Rectangle(width=%d, height=%d)" % (self.width, self.height)

class Square(Rectangle):
    def __init(self, side, height = 0):
        self.side = side
        self.height = side
        self.width = side
        super(Square,self).__init__(side,side)
        #self.width = self.height = self.side = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    def __str__(self):
        return "Square(side=%d)" % (self.width)
