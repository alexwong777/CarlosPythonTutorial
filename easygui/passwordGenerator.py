import easygui as g
import random
import turtle as t
import string
g.msgbox("Please click [OK] to generate password")

fruits=['banana','lemon','apple','kiwi','orange','strawberry','mango','starfruit','grape']
password=''
for i in range(2):
  password+=random.choice(fruits)+str(random.randrange(-100,100))+random.choice(string.punctuation)

g.msgbox('Your password is:'+ password)

t.setup(width=400,height=400)
t.title('Password Generator')
t.penup()
t.goto(-100,0)
t.write('Your password is:')
t.fillcolor("red")
t.begin_fill()
t.goto(-120,20)
t.circle(20)
t.end_fill()
t.goto(-100,-50)
t.write(password)

t.pendown()
t.pencolor("blue")
t.forward(100)
t.penup()

t.done()
