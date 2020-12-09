class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height

  def __str__(self):
      return "Rectangle(width={}, height={})".format(self.width, self.height)

  def set_width(self,width):
    self.width= int(width)
  
  def set_height(self,height):
    self.height=int(height)

  def get_area(self):
    return self.height*self.width

  def get_perimeter(self):
    return (self.height+self.width)*2

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    shape=""
    if self.height>50 or self.width>50:
      return "Too big for picture."
    for i in range(self.height):
      shape+='*'*self.width+'\n'
    return shape
  
  def get_amount_inside(self,anothershape):
    num=self.get_area()//anothershape.get_area()
    return num

class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side,side)
  
  def set_side(self,side):
    self.width=int(side)
    self.height=int(side)

  def set_height(self,height):
    self.set_side(height)

  def set_width(self,width):
    self.set_side(width)

  def __str__(self):
    return "Square(side={})".format(self.height)
