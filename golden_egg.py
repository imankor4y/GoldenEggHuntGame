import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Golden Egg by Group 14")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

golden_egg = turtle.Turtle()
golden_egg.speed(0)
golden_egg.shape("circle")
golden_egg.color("red")
golden_egg.penup()
golden_egg.goto(0,100)


board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.hideturtle()
board.goto(0,260)
board.write("Score: 0 High Score: 0", align="center", font=("Courier",20,"normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
        
wn.listen()
wn.onkeypress(go_down, "s")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()
    if head.xcor()>360 or head.xcor()<-380 or head.ycor()>290 or head.ycor()<-270:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        score = 0
        delay = 0.1
        board.clear()
        board.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",20, "normal"))
    if head.distance(golden_egg) < 20:
        x = random.randint(-340, 340)
        y = random.randint(-280, 290)
        golden_egg.goto(x,y)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        board.clear()
        board.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    move()
    time.sleep(delay)
wn.mainloop()