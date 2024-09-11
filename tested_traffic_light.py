#Import Turtle and Time module
from turtle import *
import time as tm


#Goto function
def go_to(x, y):
    pu()
    goto(x, y)
    pd()


#Draw Polygon and color it
def polygon(sides, length, width, pencolor='black', fillcolor='white'):
    color(pencolor, fillcolor)
    begin_fill()
    if length != width:
        for i in range(sides // 2):
            fd(width)
            lt(360 / sides)
            fd(length)
            lt(360 / sides)
    end_fill()


def screen(show):
    go_to(-30, 255)
    polygon(4, 30, 60, 'black', 'grey')
    goto(0, 255)
    write(show, align="center", font=("ds-digital", 12, "bold"))


#blinking light
def blink(x, y, radius, fillcolor, sleep_count):
    go_to(x, y - 100)
    color(fillcolor, fillcolor)
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
        screen(timer)
        blink(0, 280, 30, "red", 1)
        undo()
        second += 1
        timer += 1
        if second > 10:
            timer = 1
            break
    #Orange Light
    while second < 16:
        screen(timer)
        blink(0, 200, 30, "orange", 1)
        undo()
        second += 1
        timer += 1
        if second > 15:
            timer = 1
            break
    #Green Light
    while second < 21:
        screen(timer)
        blink(0, 120, 30, "green", 1)
        undo()
        second += 1
        timer += 1
        if second > 20:
            timer = 1
            break


#Draw structure of traffic light
def draw_structure():
    go_to(100, -200)
    polygon(4, -40, -200, 'black', 'darkgrey')
    go_to(-10, -200)
    polygon(4, 200, 20, 'black', 'blue')
    go_to(-50, 0)
    polygon(4, 300, 100, 'white', 'black')
    go_to(0, 180)
    pencolor("red")
    circle(30)
    go_to(0, 100)
    pencolor("orange")
    circle(30)
    go_to(0, 20)
    pencolor("green")
    circle(30)


def main():
    #Set Screen
    screensize(200, 700)
    getscreen()
    title("Traffic Light by @himanshuaryan")
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


if __name__ == '__main__':
    main()
