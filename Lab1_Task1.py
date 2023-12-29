from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

import random

w,h=500,500

p1,p2,p3=0,0,0
p4,p5,p6=1,1,1



def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def background():
    glBegin(GL_QUADS)
    glVertex2f(0, 0)#bottom left
    glVertex2f(500, 0)#bottom right
    glVertex2f(500, 500)#top right
    glVertex2f(0, 500)#top left
    glEnd()

def house():
    glBegin(GL_QUADS)
    glVertex2f(100, 10)#bottom left
    glVertex2f(400, 10)#bottom right
    glVertex2f(400, 150)#top right
    glVertex2f(100, 150)#top left
    glEnd()    

def window1():
    glBegin(GL_QUADS)
    glVertex2f(350, 100)#bottom left
    glVertex2f(380, 100)#bottom right
    glVertex2f(380, 120)#top right
    glVertex2f(350, 120)#top left
    glEnd()

def window2():
    glBegin(GL_QUADS)
    glVertex2f(350, 78)#bottom left
    glVertex2f(380, 78)#bottom right
    glVertex2f(380, 98)#top right
    glVertex2f(350, 98)#top left
    glEnd()

def window3():
    glBegin(GL_QUADS)
    glVertex2f(318, 100)#bottom left
    glVertex2f(348, 100)#bottom right
    glVertex2f(348, 120)#top right
    glVertex2f(318, 120)#top left
    glEnd()

def window4():
    glBegin(GL_QUADS)
    glVertex2f(318, 78)#bottom left
    glVertex2f(348, 78)#bottom right
    glVertex2f(348, 98)#top right
    glVertex2f(318, 98)#top left
    glEnd()

def door():
    glBegin(GL_QUADS)
    glVertex2f(150, 10)#bottom left
    glVertex2f(200, 10)#bottom right
    glVertex2f(200, 98)#top right
    glVertex2f(150, 98)#top left
    glEnd()

def roof():
    glBegin(GL_TRIANGLES)
    glVertex2f(95, 150)#bottom left
    glVertex2f(405, 150)#bottom right
    glVertex2f(250, 220)#top 
  
    glEnd()  

# Raindrop class
class Raindrop:
    def __init__(self):
        self.x = random.uniform(-500, 500)
        self.y = random.uniform(220, 500)
        self.speed = random.uniform(2, 5)
        self.bend=0.0

    def fall(self):
        self.y -= self.speed
        if self.y < 150:
            self.y = 500
            self.x = random.uniform(-500, 500)
        self.x+=self.bend

# Create a list of raindrops
raindrops = [Raindrop() for _ in range(1000)]


bending_factor=0.0

def draw_rain():
    glBegin(GL_LINES)
    for drop in raindrops:
        glColor3f(p4, p5, p6) 
        glVertex2f(drop.x, drop.y)
        glVertex2f(drop.x, drop.y + 10)  # Adjust the length of raindrops
        drop.fall()
    glEnd()

# def rain():
#     x=random.uniform(0,500)
#     y=random.uniform(220,500)
#     glLineWidth(1)
#     glBegin(GL_LINES)
#     glVertex2f(x,y)
#     glVertex2f(x,y+1)
#     glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # gluPerspective(60, 1, 1, 100)
    # glTranslatef(0, -5, -20)
    iterate()
    #colorchange(p1,p2,p3)
    #glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(p1, p2, p3) 

    #call the draw methods here
    background()
    #house base
    glColor3f(0, 0, 255)
    house()
    #windows
    glColor3f(p1, p2, p3)
    window1()
    glColor3f(p1, p2, p3)
    window2()
    glColor3f(p1, p2, p3)
    window3()
    glColor3f(p1, p2, p3)
    window4()
    #door
    glColor3f(255,140,0)
    door()
    #roof
    glColor3f(255,140,0)
    roof()
    glColor3f(0,0,0)
    draw_points(158,50)
    #rain
    # for _ in range(100):
    #     glColor3f(p4,p5,p6)
    #     rain()
    for drop in raindrops:
        drop.bend=bending_factor
    draw_rain()

    glutSwapBuffers()








def special_keys(key, x, y):
    
    global p1,p2,p3,p4,p5,p6
    global bending_factor
    if key==GLUT_KEY_UP:
        p1+=0.4
        p2+=0.4
        p3+=0.4
        p4-=0.4
        p5-=0.4
        p6-=0.4
        #glColor3f(p1,p2,p3)
        print("background color changed towards lighter shade")
        print("rain color changed towards darker shade")
    if key== GLUT_KEY_DOWN:		#// up arrow key
        p1-= 0.4
        p2-= 0.4
        p3-= 0.4
        p4+=0.4
        p5+=0.4
        p6+=0.4
        #glColor3f(p1,p2,p3)
        print("background color changed towards darker shade")
        print("rain color changed towards lighter shade")
    if key==GLUT_KEY_LEFT:
        for drop in raindrops:
            drop.x-=1
            bending_factor-=0.001
    if key==GLUT_KEY_RIGHT:
        for drop in raindrops:
            drop.x+=1
            bending_factor+=0.001
    glutPostRedisplay()


def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global bending_factor
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
            for drop in raindrops:
                drop.x-=1
                bending_factor-=0.001
            #c_X, c_y = convert_coordinate(x,y)
            
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            for drop in raindrops:
                drop.x+=1
                bending_factor+=0.001

    glutPostRedisplay()



def keyboardListener(key, x, y):

    global bending_factor
    if key==b'l':
        for drop in raindrops:
            drop.x-=1
            bending_factor-=0.001
    if key==b'r':
        for drop in raindrops:
            drop.x+=1
            bending_factor==0.001
    

    glutPostRedisplay()

    
def animate():
    draw_rain()
    glutPostRedisplay()   



glutInit()



glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(w, h) #window size
glutInitWindowPosition(250, 250)
wind = glutCreateWindow(b"Task1") #window name
glutDisplayFunc(showScreen)

glutIdleFunc(animate)
glutSpecialFunc(special_keys)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)




glutMainLoop()

