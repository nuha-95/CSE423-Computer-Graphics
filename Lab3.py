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


def timer(value):
    global radius, animate, circle_centers, val
    if animate==True and freeze==False:
        for r in circle_centers:
            r[2] += 1
    glutTimerFunc(val, timer, 0)
    glutPostRedisplay()

def mouselistener(button,state,x,y):
    global animate, circle_centers, radius, freeze
    c_y=h-y

    if button == GLUT_RIGHT_BUTTON and state==GLUT_DOWN:

        animate=True
        if freeze==False:
            circle_centers.append([x, c_y, radius])
        
        
    glutPostRedisplay()

def special_keys(key,x,y):
    global val
    if  key==GLUT_KEY_LEFT and freeze==False:
        if val>=5:
            val-=10
        val=100
    if  key==GLUT_KEY_RIGHT and freeze==False:
        val+=10

def keyboardlistener(key,x,y):
    global freeze
    if ord(key)==32:
        if freeze==True:
            freeze=False
        else:
            freeze=True

def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 600)

    glMatrixMode(GL_MODELVIEW)
    global radius, animate, circle_centers
    
    
    if animate==True:

    
        for center_x, center_y, rad in circle_centers:
            if center_x - rad <= 0 or center_x + rad >= w or center_y - rad <= 0 or center_y + rad >= h:
                circle_centers.remove([center_x, center_y,rad])
            else:
                glColor3f(255, 255, 0)
                midpoint_circle(center_x,center_y,rad)

    glutSwapBuffers()
    


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(w, h)
glutInitWindowPosition(250, 250)
glutCreateWindow(b"Lab3")
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutMouseFunc(mouselistener)
glutKeyboardFunc(keyboardlistener)
glutSpecialFunc(special_keys)
glutTimerFunc(val, timer, 0)
glutMainLoop()