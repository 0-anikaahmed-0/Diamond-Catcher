from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

dx = 0
dy = 0
d = 0
y = 0
incE = 0
incNE = 0

zone0_x1 = 0
zone0_x2 = 0
zone0_y1 = 0
zone0_y2 = 0

array = []

zone0 = False
zone1 = False
zone2 = False
zone3 = False
zone4 = False
zone5 = False
zone6 = False
zone7 = False

pause = False
click = 0 
x_move = 0
y_move = 0
bar_x = 0
score = 0
score_flag = False
game_over = False
r, g, b = 0, 0, 0
speed = 1

def draw_points(x, y, colour):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(colour[0], colour[1], colour[2])
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
    glutPostRedisplay()
    


def draw_line(x1, y1, x2, y2, colour):
    global dx, dy, d, y, incE, incNE, zone0_x1, zone0_x2, zone0_y1, zone0_y2, zone0, zone1, zone2, zone3, zone4, zone5, zone6, zone7, array

    array = []
    dx = x2 - x1
    dy = y2 - y1

    if dy == 0:
        if x1 < x2:
            for x in range(x1, x2+ 1):
                draw_points(x, y1, colour)
        else:
            for x in range(x2, x1+ 1):
                draw_points(x, y1, colour)
    elif dx == 0:
        if y1 < y2:
            for y in range(y1, y2+ 1):
                draw_points(x1, y, colour)
        else:
            for y in range(y2, y1+ 1):
                draw_points(x1, y, colour)

    else:
        if dx > 0:
            if dy > 0:
                if abs(dx) > abs(dy): #Zone 0

                    zone0 = True           
                    zone0_x1 = x1
                    zone0_x2 = x2
                    zone0_y1 = y1
                    zone0_y2 = y2
                else:     
                    zone1 = True            #Zone 1
                    zone0_x1 = y1
                    zone0_x2 = y2
                    zone0_y1 = x1
                    zone0_y2 = x2
            else:
                if abs(dx) > abs(dy): #Zone 7
                    zone7 = True 
                    zone0_x1 = x1
                    zone0_x2 = x2
                    zone0_y1 = -y1
                    zone0_y2 = -y2
                else:       
                    zone6 = True         #Zone 6
                    zone0_x1 = -y1
                    zone0_x2 = -y2
                    zone0_y1 = x1
                    zone0_y2 = x2
        else:
            if dy > 0:                 
                if abs(dx) > abs(dy): 
                    zone3 = True  #Zone 3
                    zone0_x1 = y1
                    zone0_x2 = y2
                    zone0_y1 = -x1
                    zone0_y2 = -x2
                else:  
                    zone2 = True                # Zone 2
                    zone0_x1 = y1
                    zone0_x2 = y2
                    zone0_y1 = -x1
                    zone0_y2 = -x2                

            else: 
                if abs(dx) > abs(dy):
                    zone4 = True   #Zone 4
                    zone0_x1 = -x1
                    zone0_x2 = -x2
                    zone0_y1 = -y1
                    zone0_y2 = -y2
                else:  
                    zone5 = True                 #Zone 5
                    zone0_x1 = -y1
                    zone0_x2 = -y2
                    zone0_y1 = -x1
                    zone0_y2 = -x2

        dx_new = zone0_x2 - zone0_x1
        dy_new = zone0_y2 - zone0_y1
        d = 2 * dy_new - dx_new
        incE = 2 * dy_new
        incNE = 2 * (dy_new -dx_new)
        y = zone0_y1
        for x in range(zone0_x1, zone0_x2+ 1):
            array.append((x,y))
            if d > 0:
                d += incNE
                y += 1
            else:
                d += incE

        for a, b in array:

            if zone0:
                x, y = a, b
            elif zone1:
                x, y = b, a
            elif zone2:
                x, y = -b, a
            elif zone3:
                x, y = -a, b
            elif zone4:
                x, y = -a, -b
            elif zone5:
                x, y = -b, -a
            elif zone6:
                x, y = b, -a
            elif zone7:
                x, y = a, -b
            
            draw_points(x,y, colour)

    
    zone0, zone1, zone2, zone3, zone4, zone5, zone6, zone7 = False, False, False, False, False, False, False, False
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global pause, click, game_over, score, speed, y_move
    if button == GLUT_RIGHT_BUTTON:
        if (state == GLUT_DOWN):
            if (235 <= x <= 265) and (440 <= (500-y) <= 490):
                if click % 2 == 0:
                    pause = False
                else:
                    pause = True
                click += 1

            if (440 <= x <= 490) and (440 <= (500-y) <= 490):
                print("Goodbye! Score:", score)
                glutLeaveMainLoop()

            if (10 <= x <= 70) and (440 <= (500 -y) <= 490):
                game_over = False
                pause = False
                score = 0
                speed = 1
                y_move = 498
                print("Starting over!")

def specialKeyListener(key, x, y):
    global bar_x
    if pause == False and game_over == False:
        if key == GLUT_KEY_LEFT:
            bar_x = bar_x - 10 - math.ceil(speed * 4)     
            if bar_x <= -191:
                bar_x = -190
        if key == GLUT_KEY_RIGHT:
            bar_x = bar_x + 10 + math.ceil(speed * 4) 

            if bar_x >= 191:
                bar_x = 190
    
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global x_move, y_move, score, score_flag, game_over, r, g, b, speed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) 
 
    if game_over != True:

        if pause == False:
            if y_move  >= 490:
                x_move = random.randint(-170, 260)
                r = random.random()
                g = random.random()
                b = random.random()
            if score_flag:
                y_move = 498
                score_flag = False
            else:
                y_move =  (y_move - math.floor(speed)) % 500

            draw_line(180 + x_move, 20 + y_move, 200 + x_move, 40 + y_move, (r, g, b)) #Drawing the diamond
            draw_line(200 + x_move, 40 + y_move, 220 + x_move, 20 + y_move, (r, g, b))
            draw_line(220 + x_move, 20 + y_move, 200 + x_move,  y_move, (r, g, b))
            draw_line(200 + x_move, y_move, 180 + x_move, 20 + y_move, (r, g, b))

            if y_move <=25 and ((200 + x_move) >= (190 + bar_x) and (200 + x_move) <= (310 + bar_x)):  
                score += 1
                print("Score: ", score)
                score_flag = True
                speed += 0.5
            elif y_move <= 5:
                print("Game Over! Score:", score)
                game_over = True
                speed = 0
        else:
            draw_line(180 + x_move, 20 + y_move, 200 + x_move, 40 + y_move, (r, g, b)) #Drawing the diamond
            draw_line(200 + x_move, 40 + y_move, 220 + x_move, 20 + y_move, (r, g, b))
            draw_line(220 + x_move, 20 + y_move, 200 + x_move,  y_move, (r, g, b))
            draw_line(200 + x_move, y_move, 180 + x_move, 20 + y_move, (r, g, b))

        
        draw_line(190 + bar_x, 25, 310 + bar_x, 25, (1.0, 1.0, 1.0)) # Drawing the bar
        draw_line(210 + bar_x, 5, 290 + bar_x, 5, (1.0, 1.0, 1.0))
        draw_line(190 + bar_x, 25, 210 + bar_x, 5, (1.0, 1.0, 1.0))
        draw_line(310 + bar_x, 25, 290 + bar_x, 5, (1.0, 1.0, 1.0))

    else:
        draw_line(190 + bar_x, 25, 310 + bar_x, 25, (1.0, 0.0, 0.0)) # Drawing the bar ### CHANGE COLOUR
        draw_line(210 + bar_x, 5, 290 + bar_x, 5, (1.0, 0.0, 0.0))
        draw_line(190 + bar_x, 25, 210 + bar_x, 5, (1.0, 0.0, 0.0))
        draw_line(310 + bar_x, 25, 290 + bar_x, 5, (1.0, 0.0, 0.0))

    draw_line(440, 490, 490, 440, (1.0, 0.0, 0.0)) #Drawing the cross
    draw_line(440, 440, 490, 490, (1.0, 0.0, 0.0))

    draw_line(10, 465, 70, 465, (0.27, 0.79, 0.79))   #Drawing the arrow
    draw_line(10, 465, 35, 440, (0.27, 0.79, 0.79))
    draw_line(10, 465, 35, 490, (0.27, 0.79, 0.79))
        
    if pause == False or game_over == True:
        draw_line(235, 440, 235, 490, (0.82, 0.5, 0.22))
        draw_line(265, 490, 265, 440, (0.82, 0.5, 0.22))
    else:
        draw_line(240, 440, 240, 490, (0.82, 0.5, 0.22))
        draw_line(240, 440, 270, 465, (0.82, 0.5, 0.22))
        draw_line(240, 490, 270, 465, (0.82, 0.5, 0.22))


    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()