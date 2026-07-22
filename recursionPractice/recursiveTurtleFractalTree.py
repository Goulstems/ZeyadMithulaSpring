import turtle

def tree(t, length):
    if length < 10:   # base case
        return
    t.forward(length)

    t.left(30)
    tree(t, length * 0.7)

    t.right(60)
    tree(t, length * 0.7)

    t.left(30)
    t.backward(length)  # backtrack

screen = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.speed("fastest")
t.penup(); t.goto(0, -250); t.pendown()

tree(t, 100)

t.hideturtle()
screen.exitonclick()