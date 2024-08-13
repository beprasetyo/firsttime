#turtle
import turtle
#set up the turtle screen
window = turtle.Screen()
window.bgcolor("white")

#create turtle object
artist = turtle.Turtle()
artist.shape("turtle")
artist.color("black")
artist.speed(5) #adjust speed as needed

#function to draw a spiral
def draw_spiral(side,lenght,angle):
    for _ in range(side):
        artist.forward(lenght)
        artist.right(angle)

#number side in spiral
num_sides = 36

#lenght of each side
side_lenght = 200

#angle which the turtle turn
turn_angle = 60

#drawing the spiral
draw_spiral(num_sides,side_lenght,turn_angle)

#close the turtle graphic windows
window.exitonclick()