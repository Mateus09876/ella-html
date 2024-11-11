import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Configuración de la tortuga
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(3)

# Dibujar el corazón
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Escribir el mensaje
pen.penup()
pen.goto(-70, -70)
pen.color("black")
pen.write("¿Quieres ser mi novia?", font=("Arial", 18, "bold"))
pen.hideturtle()

# Mantener la ventana abierta
turtle.done()
