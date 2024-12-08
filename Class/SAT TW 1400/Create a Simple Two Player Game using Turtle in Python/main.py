import turtle, random

def isInScreen(win, turtle) :
    left = -win.window_width() / 2
    right = win.window_width() / 2
    top = win.window_height() / 2
    bottom = -win.window_height() / 2

    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()

    stillIn = True

    if turtle_x > right or turtle_x < left :
        stillIn = False
    if turtle_y > top or turtle_y < bottom :
        stillIn = False

    return stillIn

def samePosition(Red, Blue) :
    if Red.pos() == Blue.pos() :
        return False
    else :
        return True

# Main program
wn = turtle.Screen()

red = turtle.Turtle()
red.pencolor('red')
red.pensize(5)
red.shape('turtle')
pos = red.pos()

blue = turtle.Turtle()
blue.pencolor('blue')
blue.pensize(5)
blue.shape('turtle')
blue.hideturtle()
blue.penup()
blue.goto(pos[0]+50, pos[1])
blue.showturtle()
blue.pendown()

blue_s = True
red_s = True

while blue_s and red_s and samePosition(red, blue) :
    red_choice = random.randrange(0, 2)
    red_angle = 90
    if red_choice == 0 :
        red.left(red_angle)
    else :
        red.right(red_angle)

    blue_choice = random.randrange(0, 2)
    blue_angle = 90
    if blue_choice == 0 :
        blue.left(blue_angle)
    else :
        blue.right(blue_angle)

    red.forward(50)
    blue.forward(50)

    red_s = isInScreen(wn, red)
    blue_s = isInScreen(wn, blue)

red.pencolor('black')
blue.pencolor('black')

if red_s == True and blue_s == False :
    red.write('Red Win!', True, align='center', font=('arial', 15, 'bold'))
elif red_s == False and blue_s == True :
    red.write('Blue Win!', True, align='center', font=('arial', 15, 'bold'))
else :
    red.write('Draw!', True, align='center', font=('arial', 15, 'bold'))
    blue.write('Draw!', True, align='center', font=('arial', 15, 'bold'))

wn.exitonclick()
