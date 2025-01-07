import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Square Drawing with Turtle")
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.pensize(3)
pen.speed(2)

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move forward by 100 units
    pen.left(90)      # Turn left by 90 degrees

# Finish the drawing
pen.hideturtle()
screen.mainloop()
