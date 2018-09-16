#!/usr/bin/env python
class Drawcircle:

    def __init__(self, radius, thickness):
      self.radius = radius
      self.thickness = thickness
      self.center = radius+thickness+1
      self.outercircle = radius+(thickness-1)
      self.pixels = [['#' for x in range(2*radius+thickness*2+3)] for y in range(2*radius+thickness*2+3)]

    def circle(self):
        xc = self.center
        yc = self.center
        xo = self.outercircle;
        xi = self.radius;
        y = 0;
        erro = 1 - xo;
        erri = 1 - xi;

        while(xo >= y):
            self.xLine(xc + xi, xc + xo, yc + y)
            self.yLine(xc + y,  yc + xi, yc + xo)
            self.xLine(xc - xo, xc - xi, yc + y)
            self.yLine(xc - y,  yc + xi, yc + xo)
            self.xLine(xc - xo, xc - xi, yc - y)
            self.yLine(xc - y,  yc - xo, yc - xi)
            self.xLine(xc + xi, xc + xo, yc - y)
            self.yLine(xc + y,  yc - xo, yc - xi)
            y += 1
            if (erro <= 0):
                erro += 2 * y + 1
            else:
                xo -= 1
                erro += 2 * (y - xo + 1)
            if (y > self.radius):
                xi = y
            else:
                if (erri < 0):
                    erri += 2 * y + 1
                else:
                    xi -= 1
                    erri += 2 * (y - xi + 1)
        print('\n'.join([''.join([v for v in row]) for row in self.pixels]))

    def xLine(self,x1,x2,y):
        while (x1 <= x2):
            self.pixels[x1][y] = '.'
            x1 += 1

    def yLine(self,x,y1,y2):
        while (y1 <= y2):
            self.pixels[x][y1] = '.'
            y1 += 1
class Square:

    def __init__(self, dots, length):
      self.dots = dots
      self.length = length

    def printsquare(self):
        for i in range(self.length):
            print('#'*((self.dots*self.length)+self.length+1))
            for j in range(self.dots):
                print('#'+self.length*(self.dots*'.'+'#'))
        print('#'*((self.dots*self.length)+self.length+1))

if __name__ == "__main__":
    userinput = input('Do you want print circle or square (1-circle,2-square): ')
    if(userinput == 1):
        radius = input('Enter the radius of the circle: ')
        thickness = input('Enter the thickness of the circle: ')
        circle = Drawcircle(radius,thickness)
        circle.circle()
    elif(userinput == 2):
        dot = input('Enter square value: ')
        square = Square(dot,dot)
        square.printsquare()
