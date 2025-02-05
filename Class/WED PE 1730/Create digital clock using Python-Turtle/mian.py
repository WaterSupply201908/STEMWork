# Digital Clock

import turtle, time, datetime as dt, random

# Main Program
if __name__ == '__main__' :
    t = turtle.Turtle() # for display time
    t1 = turtle.Turtle() # for display rectangle box

    # Create screen
    s = turtle.Screen()

    # Set background color
    #s.bgcolor("green")
    s.bgcolor('#ffffff')
    color = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#00ffff', '#ff00ff']

    # Obtain current hour/minute/second from system
    sec = dt.datetime.now().second
    min = dt.datetime.now().minute
    hr = dt.datetime.now().hour

    t1.pensize(3)
    t1.color('black')
    t1.penup()
    t1.goto(-20, 0)
    t1.pendown()

    # Hide the turtles
    t.hideturtle()
    t1.hideturtle()

    # Create reactangle box
    for i in range(2) :
        t1.forward(400)
        t1.left(90)
        t1.forward(125)
        t1.left(90)

    while True :
        t.clear()

        s.bgcolor(random.choice(color))

        # Dislay time
        t.write(str(hr).zfill(2)+':'+str(min).zfill(2)+':'+str(sec).zfill(2), font=('Arial Narrow', 64, 'bold'))
        time.sleep(1)
        sec += 1

        if sec == 60 :
            sec = 0
            min += 1

        if min == 60 :
            min = 0
            hr += 1

        if hr == 24 :
            hr = 0
