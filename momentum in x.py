# momentum in python 3 using nympy and turtle modules
# Jean Joubert 5 April 2020

import numpy as np
import turtle
import random
import time

# This small function is the heart of the program
# The rest of the code is simply for visualization
def momentum(aMass, bMass, aVel, bVel):

    aMom = aMass*aVel
    bMom = bMass*bVel

    a = np.array([[aMass, bMass],[1,-1]])
    b = np.array([aMom+bMom,bVel-aVel])

    x = np.linalg.solve(a,b)
    #print(x)
    return x


win = turtle.Screen()
win.title('Conservation of Momentum using numpy')
win.setup(1000,500)
win.bgcolor('black')
win.tracer(0)

pen = turtle.Pen()
pen.color('red')
pen.up()
pen.goto(0,200)
pen.hideturtle()


class Ball(turtle.Turtle):
    def __init__(self, mass, velocity, xpos, nr):
        super().__init__(shape = 'circle')
        self.mass = mass
        self.velocity = velocity
        self.nr = nr
        self.xpos = xpos
        self.list = ['red', 'blue', 'green', 'cyan', 'yellow']
        self.color(random.choice(self.list))
        self.up()
        self.shapesize(mass/2)
        self.radius = mass*5
        self.goto(xpos,0)
        self.bounce = 'ready'

    def move(self):
        self.goto(self.xcor()+self.velocity, self.ycor())

        if self.xcor()>500-self.radius or self.xcor()<-500+self.radius:
            self.velocity *= -1
            self.bounce = 'ready'


obj = []
ball1 = Ball(5, 6, -200, 1)
ball2 = Ball(4, -5, 200, 2)
obj.append(ball1)
obj.append(ball2)

count = 0

pen.write(f"A: Mass: {ball1.mass}, velocity: {ball1.velocity:.2f}, B Mass: {ball2.mass}, velocity: {ball2.velocity:.2f}\n \
          Momentum A: {ball1.mass*ball1.velocity:.2f}       Momentum B: {ball2.mass*ball2.velocity:.2f}", align='center', \
          font=("Courier", 12, "normal"))
time.sleep(3)
while True:
    time.sleep(0.01)
    count += 1
    win.update()
   
    for i in obj:
        if i.bounce == 'wait' and count%20 == 0:
            i.bounce = 'ready'
        i.move()

        for j in range(len(obj)):
            if i.nr != obj[j].nr:
                
                if i.xcor()+i.radius>= obj[j].xcor()-obj[j].radius and i.xcor()-i.radius<= obj[j].xcor()+obj[j].radius:
                    if i.bounce=='ready' and obj[j].bounce == 'ready':
                        values = momentum(i.mass, obj[j].mass,i.velocity, obj[j].velocity)
                    
                        i.velocity=values[0]
                        i.bounce = 'wait'
                        obj[j].velocity = values[1]
                        obj[j].bounce = 'wait'
                        pen.clear()
                        pen.write(f"A: Mass: {ball1.mass}, velocity: {ball1.velocity:.2f}, B Mass: {ball2.mass}, velocity: {ball2.velocity:.2f}\n \
          Momentum A: {ball1.mass*ball1.velocity:.2f}       Momentum B: {ball2.mass*ball2.velocity:.2f}", align='center', \
          font=("Courier", 12, "normal"))
                        #print(f"Velocity A = {i.velocity}, B = {obj[j].velocity}")



