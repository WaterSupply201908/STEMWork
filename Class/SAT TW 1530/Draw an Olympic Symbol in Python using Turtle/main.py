'''
import turtle

tr = turtle.Turtle()

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

while True :
  tr.hideturtle()
  tr.color('brown')
  tr.penup()
  tr.goto(-200, 110)
  tr.pendown()
  tr.write('Olympic Symbol', font=('Arial', 35, 'bold'))

  tr.color('blue')
  tr.penup()
  tr.goto(-150, -150)
  tr.pendown()
  tr.write('STEM Work', font=('Courier', 40, 'bold'))
'''

import random

choice = random.randint(0, 1)

if choice == 0 :
  print('Heads')
else :
  print('Tails')
