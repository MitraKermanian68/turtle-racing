import turtle
import time
import random


WIDTH, HEITHT = 500, 500
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "black", "brown"]



def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2/10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a number...Try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a valid number of racers..!")

def race(colors):
    turtles = creat_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEITHT//2 - 10:
                return colors[turtles.index(racer)]


def creat_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx, -HEITHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEITHT)
    screen.title("Turtle Racing Game")  

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(winner, "is the winner!")
time.sleep(5)






