import turtle
from turtle import *

def poligono(tam, lado):
    resp = "Polígono" if lado >= 3 else "Não polígono"
    print(resp)

    ang = 360 / lado

    print('Por questões de memória vamos impor um limite de lado de até 20 lados')
    x = turtle.Turtle()
    if lado >= 3 or lado <= 20:
        for i in range(lado):
            x.forward(tam)
            x.left(ang)
    tela = turtle.Screen()
    tela.bgcolor('green')
    tela.exitonclick()

poligono(50, 20)
