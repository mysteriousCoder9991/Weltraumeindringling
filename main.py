'''
AIM : TO DEVELOP A BASIC FIGHTING GAME USING PYTHON
DEVELOPED BY : RAHUL DHAR
VERSION : 1.01.19.07.2019(BASIC CODE)
'''
#To import the basic packages
import turtle
import os
import math
import playsound

#To set up the basic game window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Weltraumeindringling: A Space Invader 's game developed  by Rahul")
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
turtle.mainloop

#To set the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
#To set the speed of the player
playerspeed=15

#To set the enemy turtle
enemy=turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

#To set the enemyspeed 
enemyspeed = 2

c=0#To calcluate the player's score

#Create player bullet 
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#To set the bullet speed
bulletspeed=20
#There are two states of the bullet
#"ready":When the bullet is not fired and its ready to be fired
#"fired":When the bullet is fired and cannot be fired again immediately
bulletstate="ready"

#Function to move the player left
def move_left():
	x = player.xcor()
	x-=playerspeed
	if x < -280:
		x = -280
	player.setx(x)

#Function to move the player right
def move_right():
	x = player.xcor()
	x = x+playerspeed
	if x > 280:
		x=280
	player.setx(x)

#Function to fire the bullet
def fire_bullet():
	global bulletstate
	if bulletstate == "ready":#To check if the bullet is ready or not
		bulletstate = "fire"# To fire the bullet
		x=player.xcor()
		y=player.ycor()
		bullet.setposition(x,y+10)
		bullet.showturtle()
		#playsound.playsound('Shotgun.wav')

#To check whether there is collision between the game objects
def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 25:
		return  True
	else:
		return False
choice=0

#To create keyboard binding
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#The main loop which will go for an infinite time untill the game is over
while True:
	#To get the coordinate of the enemy
	x = enemy.xcor()
	x += enemyspeed 
	enemy.setx(x)
	
	#Conditons to move the enemy sideway and then downwards on the screen
	if enemy.xcor()>280:
		y = enemy.ycor()
		y -= 40
		enemyspeed *= -1
		enemy.sety(y)

	if enemy.xcor()<-280:
		y = enemy.ycor()
		y -= 40
		enemyspeed *= -1
		enemy.sety(y)
	
	#Move the bullet from the player
	if bulletstate == "fire":
		y = bullet.ycor()
		y = bulletspeed + y
		bullet.sety(y)

	#Check to see the bullet is on the screen or not
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate ="ready"

	#Check for collision between the bullet and the enemy
	if isCollision(bullet,enemy):
		bullet.hideturtle()
		bulletstate="ready"
		bullet.setposition(0, -400)
		enemy.setposition(-200, 250)
		c=c+1

	#Check if the player and the enemy has collided and if yes then exit from the game
	if isCollision(player,enemy):
		player.hideturtle()
		enemy.hideturtle()
		playsound.playsound('gameOver.wav')
		print("\nYou have scored : ",c)
		for i in range (1,1000000):
			c=0
		exit()