"""
Juego: Pacman
Programador 1: Misael Chavez Ramos
Programador 2: Rodrigo García Estrada

Fecha: 11 / mayo / 2022
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#Variables para las funciones futuras.
writer = Turtle(visible=True)
finish = Turtle(visible=True)
GameOver = {'YouWin' : 0, 'Message': 'YOU WIN', 'stop': 'YOU LOSE'}


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    #Tras tener las 64 casillas liberadas se soltara el mensaje
    if GameOver['YouWin'] == 32:
        finish.goto(0, 210)
        finish.color("black")
        finish.undo()
        finish.write(GameOver['Message'], font=('Arial', 55, 'normal'))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Se cambio la posicion en X para que estubieran lo más centrado posibles.
        goto(x+10, y)
        color('black')
        write(tiles[mark],font=('Arial', 30, 'normal'))

    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
