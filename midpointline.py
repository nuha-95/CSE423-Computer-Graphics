from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w=500
h=600


    
def findzone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx >= 0 and dy >= 0:
        if abs(dx) >= abs(dy):
            return 0
        else:
            return 1
    elif dx < 0 and dy >= 0:
        if abs(dx) >= abs(dy):
            return 3
        else:
            return 2
    elif dx < 0 and dy < 0:
        if abs(dx) >= abs(dy):
            return 4
        else:
            return 5
    elif dx >= 0 and dy < 0:
        if abs(dx) >= abs(dy):
            return 7
        else:
            return 6
    
    

def convertTozero(X, Y, z):
    if z == 0:
        return X, Y
    elif z == 1:
        return Y, X
    elif z == 2:
        return Y, -X
    elif z == 3:
        return -X, Y
    elif z == 4:
        return -X, -Y
    elif z == 5:
        return -Y, -X
    elif z == 6:
        return -Y, X
    elif z == 7:
        return X, -Y



def originalzone(X,Y,z):
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


def midpoint(a,b,z):
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x_lst = []
    y_lst = []

    X = x1
    Y = y1
    
    glBegin(GL_POINTS)
    while X <= x2:
        x_t,y_t=originalzone(X,Y,z)
        glVertex2f(x_t, y_t)
        x_lst.append(x_t)
        y_lst.append(y_t)

        if d > 0:
            d += incNE
            Y += 1 if y2 > y1 else -1
        else:
            d += incE

        X += 1
        #draw_points(X,Y)
    glEnd()
    return x_lst, y_lst


        
def drawline(x1,y1,x2,y2):
    
    z=findzone(x1,y1,x2,y2)
    a=convertTozero(x1,y1,z)
    b=convertTozero(x2,y2,z)
    midpoint(a,b,z)


# def display():
#     #//clear the display
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glClearColor(0,0,0,0);	#//color black
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     #//load the correct matrix -- MODEL-VIEW matrix
#     glMatrixMode(GL_MODELVIEW)
#     #//initialize the matrix
#     glLoadIdentity()
#     gluOrtho2D(0, 500, 0, 600)

#     glMatrixMode(GL_MODELVIEW)

    
#     glColor3f(255, 255, 0)
#     #drawline(95, 150, 405, 150)
#     drawline(405, 150, 95, 150)
#     drawline(95, 150, 250, 220)
#     drawline(405, 150, 250, 220)
    
    
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
# glutInitWindowSize(w, h)
# glutInitWindowPosition(0, 0)
# glutCreateWindow(b"Lab2_Task1")
# glClearColor(0.0, 0.0, 0.0, 1.0)
# glutDisplayFunc(display)


# glutMainLoop()