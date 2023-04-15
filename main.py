import turtle

win = turtle.Screen()
win.setup(width=1200, height=800)
win.bgcolor('black')
win.tracer(0)
win.title('My_Ping_Pong')

# racket
racket_left = turtle.Turtle()
racket_left.color('white')
racket_left.speed(0)
racket_left.penup()
racket_left.goto(-500, 0)
racket_left.shape('square')
racket_left.shapesize(stretch_len=1, stretch_wid=4)
racket_left.dx = 0
racket_left.dy = 0

racket_right = turtle.Turtle()
racket_right.color('white')
racket_right.speed(0)
racket_right.penup()
racket_right.goto(500, 0)
racket_right.shape('square')
racket_right.shapesize(stretch_len=1, stretch_wid=4)
racket_right.dx = 0
racket_right.dy = 0

# ball
ball = turtle.Turtle()
ball.color('white')
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.shape('circle')
ball.dx = 0.3
ball.dy = 0.3

# Total Score
total_score = turtle.Turtle()
total_score.speed(0)
total_score.shape('square')
total_score.color('white')
total_score.penup()
total_score.hideturtle()
total_score.goto(0, 350)
total_score.write('Player A: 0  Player B: 0', align='center', font=('Verdana', 20, 'normal'))
score_a = 0
score_b = 0

# function
def racket_left_up():
    y = racket_left.ycor()
    y += 60
    racket_left.sety(y)

def racket_left_down():
    y = racket_left.ycor()
    y -= 60
    racket_left.sety(y)

def racket_right_up():
    y = racket_right.ycor()
    y += 60
    racket_right.sety(y)

def racket_right_down():
    y = racket_right.ycor()
    y -= 60
    racket_right.sety(y) 

# keyboard
win.listen()
win.onkeypress(racket_left_up, 'w')
win.onkeypress(racket_left_down, 's')
win.onkeypress(racket_right_up, 'Up')
win.onkeypress(racket_right_down, 'Down')

while True:
    win.update()

    # move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 395:
        ball.sety(395)
        ball.dy *= -1

    if ball.ycor() < -395:
        ball.sety(-395)
        ball.dy *= -1

    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        total_score.clear()
        total_score.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Verdana', 20, 'normal'))

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        total_score.clear()
        total_score.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Verdana', 20, 'normal'))

    if racket_left.ycor() > 360:
        racket_left.sety(360)
        racket_left.dy *= -1

    if racket_left.ycor() < -360:
        racket_left.sety(-360)
        racket_left.dy *= -1

    if racket_right.ycor() > 360:
        racket_right.sety(360)
        racket_right.dy *= -1

    if racket_right.ycor() < -360:
        racket_right.sety(-360)
        racket_right.dy *= -1

    if ball.xcor() > 485 and ball.ycor() < racket_right.ycor() + 50 and ball.ycor() > racket_right.ycor() -50:
        ball.dx *= -1
    
    if ball.xcor() < -485 and ball.ycor() < racket_left.ycor() + 50 and ball.ycor() > racket_left.ycor() - 50:
        ball.dx *= -1

