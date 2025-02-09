# module
'''
import turtle

tr = turtle.Turtle() # object : instance of class

tr.pensize(5)

tr.color('blue')
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(45)

tr.color('black')
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(45)

tr.color('red')
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(45)

tr.color('yellow')
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(45)

tr.color('green')
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(45)
'''
import turtle

sc = turtle.Screen()
pen = turtle.Turtle()

# list / tuple / set / dictionary
color = ['indigo', 'violet', 'blue', 'green', 'yellow', 'orange', 'red']

def draw(col, rad, pos) :
  pen.color(col)
  pen.circle(rad, -180)
  pen.up()
  pen.setpos(pos, 0)
  pen.down()
  pen.right(180)

sc.setup(600, 600)
sc.bgcolor('black')

pen.width(10)
pen.speed(7)
pen.right(90)

for i in range(7) :
  draw(color[i], 10*(i+8), -10*(i+1))

pen.hideturtle()
