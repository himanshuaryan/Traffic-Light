#Import Turtle and Time module
from turtle import *
import time as tm

#Goto function
def go_to(x, y):
    pu()
    goto(x,y)
    pd()

#Draw Polygon and color it
def polygon(sides, length, width,pencolor='black',fillcolor='white'):
    color(pencolor,fillcolor)
    begin_fill()
    if length != width:
        for i in range(sides//2):
            fd(width)
            lt(360/sides)
            fd(length)
            lt(360/sides)
    end_fill()
    
#blinking light
def blink(x,y,radius,fillcolor,sleep_count):
    go_to(x,y)
    color(fillcolor,fillcolor)
    begin_fill()
    circle(radius)
    end_fill()
    tm.sleep(sleep_count)
    
#Show Lights
def show_lights():
    second = 1
    timer = 1
    #Red Light
    while second < 11:
        go_to(-60,310)
        polygon(4,60,120,'black','grey')
        goto(0,310)
        write(timer, align="center")
        blink(0,160,60,"red",1)
        undo()
        second += 1
        timer += 1
        if second > 10:
            timer = 1
            break
    #Orange Light    
    while second < 16:
        go_to(-60,310)
        polygon(4,60,120,'black','grey')
        goto(0,310)
        write(timer, align="center")
        blink(0,20,60,"orange",1)
        undo()
        second += 1
        timer += 1
        if second > 15:
            timer = 1
            break
    #Green Light
    while second < 21:
        go_to(-60,310)
        polygon(4,60,120,'black','grey')
        goto(0,310)
        write(timer, align="center")
        blink(0,-120,60,"green",1)
        undo()
        second += 1
        timer += 1
        if second > 20:
            timer = 1
            break

#Draw structure of traffic light        
def draw_structure():
    go_to(175,-600)
    polygon(4,-80,-350,'black','darkgrey')
    go_to(-20,-600)
    polygon(4,400,40,'black','blue')
    go_to(-100,-200)
    polygon(4,600,200,'white','black')
    go_to(0,160)
    pencolor("red")
    circle(60)
    go_to(0,20)
    pencolor("orange")
    circle(60)
    go_to(0,-120)
    pencolor("green")
    circle(60)

def main():
    #Set Screen
    getscreen()
    bgcolor("skyblue")
    pencolor("white")
    speed(0)
    tracer(2,10)
     
    draw_structure()
    #Looping and Calling
    while True:
        ht()
        show_lights()
        update()
    
if __name__=='__main__':
    main()
