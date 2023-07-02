import turtle as t
playerAdcore=0
playerBscore= 0

window=t.Screen()
window.title("Pong game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)



#creting left paddle 
leftPaddle=t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350,0)



#creating the right paddle

rightPaddle=t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350,0)

#creatign ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()

ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2
#creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score", align="center", font=('Arial', 24, 'normal'))
#moving the left paddle

def leftpaddleup():
    y=leftPaddle.ycor()
    y=y+90
    leftPaddle.sety(y)

def leftpaddledown():
    y=leftPaddle.ycor()
    y=y-90
    leftPaddle.sety(y)



#moving the left paddle
def rightpaddleup():
    y=rightPaddle.ycor()
    y=y+90
    rightPaddle.sety(y)



def rightpaddledown():
    y=rightPaddle.ycor()
    y=y-90
    rightPaddle.sety(y)


#Assign the key to play the game 
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    #moving th ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #settingup border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection= ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection= ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection= ballxdirection
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("player A:{} player B:{}".format(playerAscore,playerBscore),align='center', font=('Arial'))


    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection= ballxdirection*-1
        playerBscore=playerBscore+1
        pen.clear()
        pen.write("player A:{} player B:{}".format(playerAscore,playerBscore),align='center', font=('Arial'))
    


    #handling the Collision

    if (ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<rightPaddle.ycor()+40 and ball.ycor()>rightPaddle.ycor()-40):
        ball.setx(340)
        ballxdirection=ballxdirection*-1

    if (ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor()<leftPaddle.ycor()+40 and ball.ycor()>leftPaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1




































