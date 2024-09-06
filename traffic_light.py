#Import Turtle and Time module
from turtle import *
import time as tm

#Set Screen
getscreen()
bgcolor("black")
pencolor("white")
speed(0)

#Get Red Light
def redlight():
    second = 1
    while second < 11:
        pu()
        goto(-60,310)
        pd()
        color("black","grey")
        begin_fill()
        for r in range(2):
            fd(120)
            lt(90)
            fd(60)
            lt(90)
        goto(0,310)
        write(second, align="center")
        end_fill()
        pu()
        goto(0,160)
        pd()
        color("red","red")
        begin_fill()
        circle(60)
        end_fill()
        tm.sleep(1)
        undo()
        second += 1
        
#Get Orange Light    
def orangelight():
    second = 1
    while second < 6:
        pu()
        goto(-60,310)
        pd()
        color("black","grey")
        begin_fill()
        for r in range(2):
            fd(120)
            lt(90)
            fd(60)
            lt(90)
        goto(0,310)
        write(second, align="center")
        end_fill()
        pu()
        goto(0,20)
        pd()
        color("orange","orange")
        begin_fill()
        circle(60)
        end_fill()
        tm.sleep(1)
        undo()
        second += 1
        
#Get Green Light
def greenlight():
    second = 1
    while second < 6:
        pu()
        goto(-60,310)
        pd()
        color("black","grey")
        begin_fill()
        for r in range(2):
            fd(120)
            lt(90)
            fd(60)
            lt(90)
        goto(0,310)
        write(second, align="center")
        end_fill()
        pu()
        goto(0,-120)
        pd()
        color("green","green")
        begin_fill()
        circle(60)
        end_fill()
        tm.sleep(1)
        undo()
        second += 1

#Draw structure of traffic light        
def draw_structure():
    pencolor("black")
    pu()
    goto(-175,-600)
    pd()
    fillcolor("darkgrey")
    begin_fill()
    for i in range(2):
        forward(350)
        right(90)
        fd(80)
        rt(90)
    end_fill()
    pu()
    goto(-20,-600)
    pd()
    fillcolor("blue")
    begin_fill()
    for j in range(2):
        forward(40)
        lt(90)
        forward(400)
        lt(90)
    end_fill()
    pu()
    goto(100,-200)
    pd()
    pencolor("white")
    fillcolor("black")
    begin_fill()
    for x in range(2):
        lt(90)
        forward(600)
        lt(90)
        forward(200)
    end_fill()
    pu()
    goto(0,160)
    pd()
    pencolor("red")
    circle(60)
    pu()
    goto(0,20)
    pd()
    pencolor("orange")
    circle(60)
    pu()
    goto(0,-120)
    pd()
    pencolor("green")
    circle(60)

draw_structure()

#Looping and Calling
while True:
    ht()
    redlight()
    orangelight()
    greenlight()
    

mainloop()