# # name = "Eunyul"
# # print(name)
# # "Hello"
# # print("Hello")
# # "Hello world"
# # print("Hello","World")
# # print("Hello")
# # print("World")
# # print("Because I could not stop for death, He kindly stopped for me; The carriage held but just ourselves And Immortality")
# # print("'Hello'")
# # print('"Hello World"')


import turtle
import time
import random

import turtle
import time
import random

delay= 0.1
score = 0
high_score = 0
wn=turtle.Screen()
wn.title("snakegame exyx")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)
head=turtle.Turtle()
head.speed(1)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.shape("yellow")
food.penup()
food.goto(0,100)
segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
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
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

# wn.mainloop()

# Define the game world
world = [[" " for _ in range(10)] for _ in range(10)]

# Player starting position
player_x, player_y = 5, 5

# Game loop
while True:
    # Display the game world
    for row in world:
        print(" ".join(row))
    
    # Player input
    action = input("Move (W/A/S/D), Place block (P), Quit (Q): ").upper()
    
    # Quit the game
    if action == "Q":
        print("Thanks for playing!")
        break
    
    # Move the player
    if action == "W" and player_y > 0:
        player_y -= 1
    elif action == "A" and player_x > 0:
        player_x -= 1
    elif action == "S" and player_y < 9:
        player_y += 1
    elif action == "D" and player_x < 9:
        player_x += 1
    
    # Place a block
    if action == "P":
        world[player_y][player_x] = "X"






