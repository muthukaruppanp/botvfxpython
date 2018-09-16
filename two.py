#!/usr/bin/env python
pixels = [['#' for x in range(2*16+9)] for y in range(2*16+9)]
def circle(xc,yc,inner,outer):

    xo = outer;
    xi = inner;
    y = 0;
    erro = 1 - xo;
    erri = 1 - xi;

    while(xo >= y):
        xLine(xc + xi, xc + xo, yc + y)
        yLine(xc + y,  yc + xi, yc + xo)
        xLine(xc - xo, xc - xi, yc + y)
        yLine(xc - y,  yc + xi, yc + xo)
        xLine(xc - xo, xc - xi, yc - y)
        yLine(xc - y,  yc - xo, yc - xi)
        xLine(xc + xi, xc + xo, yc - y)
        yLine(xc + y,  yc - xo, yc - xi)
        y += 1
        if (erro <= 0):
            erro += 2 * y + 1
        else:
            xo -= 1
            erro += 2 * (y - xo + 1)
        if (y > inner):
            xi = y
        else:
            if (erri < 0):
                erri += 2 * y + 1
            else:
                xi -= 1
                erri += 2 * (y - xi + 1)
    print('\n'.join([''.join([v for v in row]) for row in pixels]))

def xLine(x1,x2,y):
    while (x1 <= x2):
        pixels[x1][y] = '.'
        x1 += 1

def yLine(x,y1,y2):
    while (y1 <= y2):
        pixels[x][y1] = '.'
        y1 += 1

if __name__ == "__main__":
    circle(20,20,16,18)
