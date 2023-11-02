import turtle
import time
import random

marcador = 0
marcador_alto = 0
#creamos la pantalla, se le asigna un tamaño en pixeles, se cambia color y titulo
s = turtle.Screen()
s.setup(650,650)
s.bgcolor("black")
s.title("proyecto 2")


#creamos la serpiente
serpiente = turtle.Turtle()
serpiente.speed(2)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.color("green")

#se usara mas adelante, al iniciar no se movera hasta que presione una tecla
serpiente.direction = "stop"

#creamos la comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.speed(0)
comida.goto(120,120)


#creamos una lista donde se agregara el cuerpo de la serpiente
cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.hideturtle()
texto.color("white")
texto.penup()
texto.goto(0, 280)
#metodo para mostrar mensajes sin que la tortuga lo tenga que dibujar
texto.write(f"Marcador:{marcador} \t Marcamos mas alto:{marcador_alto}", align="center", font="verdana")

#definimos una funcion que cambie en que direccion se mueve la serpiente
def arriba():
    serpiente.direction = "up"
def abajo():
    serpiente.direction = "down"
def derecha():
    serpiente.direction = "right"
def izquierda():
    serpiente.direction = "left"

#definimos cuanto se mueve en cada direccion
def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)    
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)

#ponemos la pantalla del juego en modo de "escucha"
s.listen()

#hacemos que el modo escucha llame a la funcion al presionar la tecla definida luego de la coma
s.onkeypress(arriba, "w")
s.onkeypress(abajo, "s")
s.onkeypress(derecha, "d")
s.onkeypress(izquierda, "a")


#configuraremos el movimiento de la serpiente
while True:
    s.update()
    
    #creamos los bordes de nuestro juego
    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop'    
        cuerpo.clear()
        
        marcador = 0
        texto.clear()
        texto.write(f"Marcador:{marcador} \t Marcamos mas alto:{marcador_alto}", align="center", font="verdana")
    
    #creamos un retraso en el movimiento de la serpiente
    time.sleep(0.1)
    if serpiente.distance(comida) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        comida.goto(x,y)
        #creamos lo que sera la nueva parte creada cuando se cumple el if
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)
        
        marcador += 10
        texto.clear()
        texto.write(f"Marcador:{marcador} \t Marcamos mas alto:{marcador_alto}", align="center", font="verdana")
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write(f"Marcador:{marcador} \t Marcamos mas alto:{marcador_alto}", align="center", font="verdana")

    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)
        
    #la pieza 0 del cuerpo sigempre seguira de cerca a la cabeza de la serpiente y el resto la seguira a ella
    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)   
         
    #creamos un bucle infinito que evalue la proximidad de la serpiente con el cuerpo y que pasa si se aproxima
      
    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"
            marcador = 0
            texto.clear()
            texto.write(f"Marcador:{marcador} \t Marcamos mas alto:{marcador_alto}", align="center", font="verdana")




turtle.done()