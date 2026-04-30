from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('green')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body, x, y):
    super().__init__()
    self.ht
    self.speed(25)
    self.color("blue")
    self.penup()
    self.goto(x, y)
    self.setheading(90)
    self.shape("square")
    self.alive = True
    self.st()
    screen.onkeypress(self.up, "w")
    screen.onkeypress(self.down, "s")
    screen.onkeypress(self.left, "a")
    screen.onkeypress(self.right, "d")

  def up(self):
    self.setheading(90)

  def down(self):
    self.setheading(270)

  def left(self):
    self.setheading(180)

  def right(self):
    self.setheading(0)

  def move(self):
    self.forward(4)
    if self.xcor() > 230 or self.xcor() < -225 or self.ycor() > 230 or self.ycor() < -228:
      self.die()
    
  def die(self):
    self.ht()
    self.alive = False

class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color('red')
    self.shape('circle')
    self.penup()
    self.relocate()
    self.showturtle()

  def relocate(self):
    self.penup()
    x = random.randint(-220, 220)
    y = random.randint(-220, 220)
    self.goto(x, y)

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
playing_area()
body = [Head]
player = Head(screen, body, -100, 0)
apple = Apple()

while player.alive:
  player.move()
  if player.distance(apple) < 20:
    apple.relocate()

apple.ht()
yertle = Turtle()
yertle.ht()
yertle.penup()
yertle.goto(-125, -25)
yertle.color("red")
yertle.speed(0)
yertle.write("You died", font=("Arial", 50, "normal"))

screen.exitonclick()