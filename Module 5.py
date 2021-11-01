# Roberto Roman
# 10/30/21

#Problem 1:

for x in range (100):     #Here we place range which we defined 1 thru 100
    print ("Hello World")  #The x

#Problem 2:
numbers = [12,10,32,3,66,17,42,99,20]
for i in numbers:
    print (i)
for i in numbers:
    sqr = i * i  # Algorithm to get square
    print ("Square of", i, "is",sqr )
#Prints quares which in this case will print
#numbers and its square

#Problem 3:

import turtle
#Defined
sides = int(input("Number of sides in polygon?"))
length = int(input("Length of the sides in polygon?"))
line_c = (input("Color of polygon?"))
shape_c = (input("Fill color of polygon?"))

wn = turtle.Screen()
alex = turtle.Turtle()

# Under we start to develop the drawing
alex.begin_fill()

for i in range(sides):
   alex.fillcolor(shape_c)
   alex.pencolor(line_c)
   alex.pensize(5)
   alex.forward(length)
   alex.left(360/sides)
alex.end_fill()

wn.exitonclick()

#Problem 4:
for i in range(0, 50):   #Ranges 1 thru 50
    if i % 3 == 0:     #Statement for three
        print (i," Is divisible by three")
    elif i % 5 == 0:   #Statement for five
        print (i, " Is divisible by five")
    else:
        print (i)


    if i % 3 == 0 and i % 5 == 0:
        print (i, "Is divisible by both")
#Problem 5:
import turtle
rm = turtle.Screen()
rob = turtle.Turtle()
colors = ["red", "blue", "green", "gray", "orange", "black"]

rob.begin_fill()
for i in range(240):
    rob.forward(2+i/4)
    rob.left(30-i/12)
    rob.color(colors[i%6])
    rob.speed (40)
rob.end_fill
rm.exitonclick()
