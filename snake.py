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
  def __init__(self, screen, x, y):
    super().__init__()
    self.ht
    self.speed(0)
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
    if self.heading()!=-90:
      self.setheading(90)

  def down(self):
    if self.heading()!=90:
      self.setheading(270)

  def left(self):
    if self.heading()!=0:
      self.setheading(180)

  def right(self):
    if self.heading()!=180:
      self.setheading(0)

  def move(self):
    self.forward(20)
    if self.xcor() > 230 or self.xcor() < -225 or self.ycor() > 230 or self.ycor() < -228:
      self.die()
    
    
  def die(self):
    self.ht()
    self.alive = False

class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("yellow")
    self.penup()
    self.shape("square")
    self.st()

  def move(self, other):
    self.goto(other.xcor(), other.ycor())

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

def update():
  global body, player, apple
  if player.alive:
    for i in range(len(body)-1, 0, -1):
      body[i].move(body[i-1])
    player.move()   
    # for j in range(3, len(body)):
    #   if player.distance(j) < 20:
    #     player.die()
    if player.distance(apple) < 30:
      apple.relocate()
      body.append(Segment(body[-1]))
      
  screen.ontimer(update, 120)

#########################################################
screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
screen.onkey(update, "space")

playing_area()

player = Head(screen, -100, 0)
body = [player]
apple = Apple()

# apple.ht()
# yertle = Turtle()
# yertle.ht()
# yertle.penup()
# yertle.goto(-125, -25)
# yertle.color("red")
# yertle.speed(0)
# yertle.write("You died", font=("Arial", 50, "normal"))

screen.exitonclick()