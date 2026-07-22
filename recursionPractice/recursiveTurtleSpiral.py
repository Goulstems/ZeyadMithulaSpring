import turtle

def draw_spiral(t, length):
    # Base case: stop recursion when length is very small
    if length <= 5:
        return

    # Draw one segment
    t.forward(length)
    t.right(30)

    # Recursive call with a smaller length
    draw_spiral(t, length - 5)

#######################################################################

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.title("Basic Recursive Turtle Design (Moved Up)")

t = turtle.Turtle()
t.speed("fastest")
t.pensize(2)
t.color("blue")

start_length = 120

# Reposition turtle: centered-ish in X and moved upward in Y
t.penup()
t.goto(-start_length / 2, start_length)   # moved upward from start_length/2
t.setheading(0)                            # face right
t.pendown()

draw_spiral(t, start_length)

t.hideturtle()
screen.exitonclick()