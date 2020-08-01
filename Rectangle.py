class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def get_area(self):
        return int(self.l) * int(self.b)
    def get_peri(self):
        return (2 * (int(self.l)+int(self.b)))
    def get_length(self):
        print (self.l)

r = Rectangle(10,20)
print (r.get_area())
print (r.get_peri())


r2 = Rectangle(20,2)
print (r2.get_area())
print (r2.get_peri())
r.get_length()
