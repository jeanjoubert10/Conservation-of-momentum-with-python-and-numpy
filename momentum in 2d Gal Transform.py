# momentum conservation in collisions using python 3 and Turtle
# Jean Joubert 5 April 2020

import turtle
import random
import time
import math


def momentum(aMass, bMass, aVel, bVel):
    
    GalTransform = -bVel
    aVel += GalTransform
    bVel += GalTransform
    V1 = aVel
    

    aVel = ((aMass-bMass)/(aMass+bMass))*V1
    bVel = ((2*aMass)/(aMass+bMass))*V1
    

    aVel -= GalTransform
    bVel -= GalTransform

    return (aVel, bVel)



win = turtle.Screen()
win.title('Conservation of Momentum using Galilean Transformation')
win.setup(800,500)
win.bgcolor('black')
win.tracer(0)

pen = turtle.Pen()
pen.color('green')
pen.up()
pen.hideturtle()
pen.goto(0,-220)


class Ball(turtle.Turtle):
    def __init__(self, mass, xvelocity, yvelocity, xpos, nr, penpos, color):
        super().__init__(shape = 'circle')
        self.mass = mass
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.nr = nr
        self.xpos = xpos
        self.penpos = penpos
        self.list = ['red', 'blue', 'green', 'cyan', 'yellow']
        self.c = color
        self.color(self.c)
        self.up()
        self.shapesize(mass/2)
        self.radius = mass*4
        self.goto(xpos,0)
        self.bounce = 'ready'
        self.xmom = self.xvelocity*self.mass
        self.ymom = self.yvelocity*self.mass

        self.pen = turtle.Pen()
        self.pen.color(self.c)
        self.pen.up()
        self.pen.hideturtle()
        self.pen.goto(penpos,150)
        self.pen.write(f"Mass: {self.mass} kg\nVx = {self.xvelocity:.2f}\nVy = {self.yvelocity:.2f}\nMomentumX = {self.xmom:.2f}\nMomentumY = {self.ymom:.2f}",
                       align = 'left', font = ('Courier', 14, 'normal'))

    def move(self):
        self.goto(self.xcor()+self.xvelocity, self.ycor()+self.yvelocity)

        if self.xcor()>400-self.radius or self.xcor()<-400+self.radius:
            self.xvelocity *= -1
            self.ymom = self.yvelocity*self.mass
            self.xmom = self.xvelocity*self.mass
            self.bounce = 'ready'
            self.pen.clear()
            
            self.pen.write(f"Mass: {self.mass} kg\nVx = {self.xvelocity:.2f}\nVy = {self.yvelocity:.2f}\nMomentumX = {self.xmom:.2f}\nMomentumY = {self.ymom:.2f}",
                align = 'left', font = ('Courier', 14, 'normal'))
            

        if self.ycor()>250-self.radius or self.ycor()<= -250+self.radius:
            self.yvelocity *= -1
            self.ymom = self.yvelocity*self.mass
            self.xmom = self.xvelocity*self.mass
            self.bounce = 'ready'
            self.pen.clear()
            
            self.pen.write(f"Mass: {self.mass} kg\nVx = {self.xvelocity:.2f}\nVy = {self.yvelocity:.2f}\nMomentumX = {self.xmom:.2f}\nMomentumY = {self.ymom:.2f}",
                align = 'left', font = ('Courier', 14, 'normal'))
            


obj = []
# Ball(mass, xvel,yvel, xpos, number)
ball1 = Ball(3, 5, -4, 200, 1,-370, 'red')
ball2 = Ball(6, 4,-3,-200, 2, -70, 'blue')
ball3 = Ball(12, 4, 3, 3, 3, 230, 'yellow')
obj.append(ball1)
obj.append(ball2)
obj.append(ball3)

count = 0
totalMomentumX = 0
totalMomentumY = 0

for i in range(3):
    totalMomentumX += obj[i].xmom
    totalMomentumY += obj[i].ymom

pen.write(f"Total momentum X: {totalMomentumX:.2f}, total momentum Y: {totalMomentumY:.2f}", align = 'center',
          font=('Courier',14,'normal'))
    
time.sleep(3)
while True:
    count += 1
    time.sleep(0.01)
   
    for i in obj:
        if i.bounce == 'wait' and count%20 == 0:
            i.bounce = 'ready'
        i.move()

        for j in range(len(obj)):
            if i.nr != obj[j].nr:
                
                if i.xcor()+i.radius>= obj[j].xcor()-obj[j].radius and i.xcor()-i.radius<= obj[j].xcor()+obj[j].radius:
                    if i.ycor()+i.radius >= obj[j].ycor()-obj[j].radius and i.ycor()-i.radius<= obj[j].ycor()+obj[j].radius:
                        if i.bounce=='ready' or obj[j].bounce == 'ready':
                            values = momentum(i.mass, obj[j].mass,i.xvelocity, obj[j].xvelocity)
                    
                            i.xvelocity=values[0]
                            i.bounce = 'wait'
                            obj[j].xvelocity = values[1]
                            obj[j].bounce = 'wait'
                        
                            values = momentum(i.mass, obj[j].mass, i.yvelocity, obj[j].yvelocity)
                            i.yvelocity = values[0]
                            obj[j].yvelocity = values[1]
                            i.xmom = i.xvelocity*i.mass
                            obj[j].xmom = obj[j].xvelocity*obj[j].mass
                            i.ymom = i.yvelocity*i.mass
                            obj[j].ymom = obj[j].yvelocity*obj[j].mass

                            i.pen.clear()
                            i.pen.write(f"Mass: {i.mass} kg\nVx = {i.xvelocity:.2f}\nVy = {i.yvelocity:.2f}\nMomentumX = {i.xmom:.2f}\nMomentumY = {i.ymom:.2f}",
                       align = 'left', font = ('Courier', 14, 'normal'))
                            obj[j].pen.clear()
                            obj[j].pen.write(f"Mass: {obj[j].mass} kg\nVx = {obj[j].xvelocity:.2f}\nVy = {obj[j].yvelocity:.2f}\nMomentumX = {obj[j].xmom:.2f}\nMomentumY = {obj[j].ymom:.2f}",
                       align = 'left', font = ('Courier', 14, 'normal'))
    win.update()
    totalMomentumX = 0
    totalMomentumY = 0
    

    for i in range(3):
        totalMomentumX += obj[i].xmom
        totalMomentumY += obj[i].ymom
    tot = math.sqrt(totalMomentumX*totalMomentumX + totalMomentumY*totalMomentumY)
    pen.clear()
    pen.write(f"Total momentum X: {totalMomentumX:.2f}, total momentum Y: {totalMomentumY:.2f}\n\t|P| = {tot:.2f} Bouncing off walls changes total P", align = 'center',
          font=('Courier',14,'normal'))
                           
                        



