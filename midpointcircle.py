from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



w=600
h=600

radius=5

val=100


circle_centers = []

animate=False

freeze=False

def zone(X,Y,z):
    if z == 0:
        return X, Y
    elif z == 1:
        return Y, X
    elif z == 2:
        return -Y, X
    elif z == 3:
        return -X, Y
    elif z == 4:
        return -X, -Y
    elif z == 5:
        return -Y, -X
    elif z == 6:
        return Y, -X
    elif z == 7:
        return X, -Y


def midpoint_circle(x_center,y_center,r):
    x = 0
    y = r
    d = 1 - r
    glBegin(GL_POINTS)
    while x <= y:
        for z in range(8):
            x_c, y_c = zone(x, y, z)
            x_c += x_center
            y_c += y_center
            glVertex2f(x_c, y_c)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    glEnd()