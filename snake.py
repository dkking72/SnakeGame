#Snake By @Deep Kalathiya

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @D.K.KING")
wn.bgcolor("sky blue")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

snake = []

# Score Board
sb = turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Score: 0  High Score: 0", align="center", font=("Viner Hand ITC", 24, "normal"))

# Functions
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
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the snake
        for segment in snake:
            segment.goto(1000, 1000)
        
        # Clear the snake list
        snake.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        sb.clear()
        sb.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Viner Hand ITC", 24, "normal")) 

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("navy blue")
        new_segment.penup()
        snake.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        sb.clear()
        sb.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Viner Hand ITC", 24, "normal")) 

    # Move the end snake first in reverse order
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(snake) > 0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x,y)
    move()    

    # Check for head collision with the body snake
    for segment in snake:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the snake
            for segment in snake:
                segment.goto(1000, 1000)
        
            # Clear the snake list
            snake.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            sb.clear()
            sb.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Viner Hand ITC", 24, "normal"))

    time.sleep(delay)
wn.mainloop()