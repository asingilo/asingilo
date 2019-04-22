import turtle
import  random

score = 0
live = 10

wn = turtle.Screen()
wn.title("เกม ")
wn.bgcolor("red")
wn.bgpic("bg.png")
wn.setup(width=800,height=600)
wn.tracer(0)

wn.register_shape("pk.gif")
wn.register_shape("1.gif")
wn.register_shape("2.gif")

player = turtle.Turtle()
player.speed(0)
player.shape("pk.gif")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction = "stop"

players2 = []


#player2
for _ in range(5):
    player2 = turtle.Turtle()
    player2.speed(0)
    player2.shape("1.gif")
    player2.color("black")
    player2.penup()
    player2.goto(0,250)
    player2.speed =random.randint(1,2)
    players2.append(player2)

#badball
badballs = []


for _ in range(5):
    badball = turtle.Turtle()
    badball.speed(0)
    badball.shape("2.gif")
    badball.color("white")
    badball.penup()
    badball.goto(-100,250)
    badball.speed =random.randint(1,4)
    badballs.append(badball)

#pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("score: {} live: {}".format(score,live),align="center")


def go_left():
    player.direction = "Left"
    
def go_right():
    player.direction = "Right"
    
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")



while True:
    
    wn.update()
    
    if player.direction =="Left":
        x = player.xcor()
        x -= +0.5
        player.setx(x)

    if player.direction =="Right":
        x = player.xcor()
        x += +0.5
        player.setx(x)

#moveplayer
    for player2 in players2:
        y = player2.ycor()
        y-= player2.speed
        player2.sety(y)    

#random
        if  y < -300:
            x = random.randint(-390,390)
            y = random.randint(300,400)
            player2.goto(x,y)

        if player2.distance(player) < 20:
            x = random.randint(-390,390)
            y = random.randint(300,400)
            player2.goto(x,y)   
            score +=1
            pen.clear()
            pen.write("score: {} live: {}".format(score,live),align="center")
#movebad
    for badball in badballs:
        y = badball.ycor()
        y-= badball.speed
        badball.sety(y)    

#random
        if  y < -300:
            x = random.randint(-390,390)
            y = random.randint(300,400)
            badball.goto(x,y)

        if badball.distance(player) < 10:
            x = random.randint(-390,390)
            y = random.randint(300,400)
            badball.goto(x,y)
            score -=1
            live -=1
            pen.clear()
            pen.write("score: {} live: {}".format(score,live),align="center")

wn.mainloop()