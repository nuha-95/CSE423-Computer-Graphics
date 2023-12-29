from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
animation=True
points = []

w,h=500,500
blink=False
speed=0.0001
def generate_random_point(x, y):
    color = (random.random(), random.random(), random.random())
    direction = (random.choice([-1, 1]), random.choice([-1, 1]))
    points.append({'x': x, 'y': y, 'color': color, 'direction': direction})

def draw_point(x, y, color):
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(*color)
    glVertex2f(x, y)
    glEnd()

# def convert_coordinate(x,y):
#     global w, h
#     a = x - (w/2)
#     b = (h/2) - y 
#     return a,b

def mouselistener(button, state, x, y):
    global blink
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        #c_x,c_y=convert_coordinate(x,y)
        generate_random_point((x / 250) - 1, 1 - (y / 250))
        #generate_random_point(c_x,c_y)
        glutPostRedisplay()
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        blink=True
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
            blink=False
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if animation==True:
        for point in points:

            if blink==True:
                t_c=(0,0,0)
            if blink==False:
                t_c=point['color']
            draw_point(point['x'], point['y'], t_c)   

        glutSwapBuffers()

def animate():
    if animation==True:
        global speed

        for point in points:
            point['x'] += point['direction'][0] * speed
            point['y'] += point['direction'][1] * speed
            
        glutPostRedisplay()    
 
def special_keys(key,x,y):
    global speed
    if  key==GLUT_KEY_UP:
        speed*=2
    if  key==GLUT_KEY_DOWN:
        speed/=2
 
def keyboardlistener(key,x,y):
    global animation
    if ord(key)==32:
        animation=False


def keyboard_up(key,x,y):
    global animation
    if ord(key)==32:
        animation=True



    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Task2")
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)

glutIdleFunc(animate)
    
glutKeyboardFunc(keyboardlistener)
glutKeyboardUpFunc(keyboard_up)
glutSpecialFunc(special_keys)
glutMouseFunc(mouselistener)
glutMainLoop()