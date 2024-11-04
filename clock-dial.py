# A clock dial

import turtle
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(620,620)
screen.title('A Clock dial made by Saksham Aggarwal')
screen.bgcolor('black')
clr=['red','green','blue','yellow','purple']
trtl.pensize(4)
trtl.shape('turtle')
trtl.penup()
trtl.pencolor('red')
m=0
for i in range(12):
      m=m+1
      trtl.penup()
      trtl.setheading(-30*i+60)
      trtl.forward(150)
      trtl.pendown()
      trtl.forward(25)
      trtl.penup()
      trtl.forward(20)
      trtl.write(str(m),align="center",font=("Arial", 12, "normal"))
      if m==12:
        m=0
      trtl.home()
      trtl.home()



