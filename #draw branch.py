#draw branch
import turtle
def draw_branch(branch_lenght, t):
    if branch_lenght > 5:
        #draw the main branch
        t.forward(branch_lenght)
        #right subtree
        t.right(20)
        draw_branch(branch_lenght - 15,t)
        t.left(40)
        draw_branch(branch_lenght - 15, t)
        t.right(20)
        t.backward(branch_lenght)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    fractal_tree = turtle.Turtle()
    fractal_tree.speed(5)
    fractal_tree.color("green")
    fractal_tree.left(90)
    fractal_tree.penup()
    fractal_tree.setpos(0,-200)
    fractal_tree.pendown()
    #draw_branch(100, fractal_tree)
    window.exitonclick()

#if __name_=="_main":
main()