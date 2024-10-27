import pgzrun,random
WIDTH=500
HEIGHT=500
TITLE=("shooting game")
alien=Actor("alien")

message=""

def draw():
    screen.clear()
    screen.fill("red")
    alien.draw()
    screen.draw.text(message,(alien.x,alien.y))

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        alien.x=random.randint(50,WIDTH-50)
        alien.y=random.randint(50,HEIGHT-50)
        message="Good shot!"
    else:
        message="Try again"






































pgzrun.go()