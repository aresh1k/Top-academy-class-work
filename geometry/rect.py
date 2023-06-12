class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)


__author__ = "Roman"

if __name__ == '__main__':
    r1 = Rectangle(10, 20)
    print("Class Rectangle", r1.get_perimetr())
    print(__name__)     # __main__
    print(__author__)
