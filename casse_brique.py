import pgzrun

WIDTH = 800
HEIGHT = 600


all_briks = []


for x in range(0, 800 , 100):
    for y in range(0, 7 * 30 , 30):
        brick = Actor("brick",anchor = ["left","top"])
        brick.pos = [x,y] # je definis la position de anchor selon ce que j'ai mis plus haut dans les paramètres de Actor.
        all_briks.append(brick)


player = Actor("player")
player.pos = [400,550] #liste de 2 éléments

ball = Actor("ball")
ball.pos = [400,500]

ball_speed = [3,-3]

def draw():
    screen.clear()
    screen.fill("violetred3")
    for brick in all_briks:
        brick.draw()

    player.draw() # je le dessine après sinon il sera caché par ce que je dessine ensuite. Bah oui logique enfaing
    ball.draw()

def update():
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.right > WIDTH or ball.left < 0:
        invert_horizontal_speed()
    if ball.top < 0 or ball.bottom > HEIGHT :
        invert_vertical_speed()

    if ball.colliderect(player):
        invert_vertical_speed()
    
    to_delet = []
    
    for brick in all_briks:
        if ball.colliderect(brick):
            to_delet.append(brick)
            invert_vertical_speed()
    
    for brick in to_delet:
        all_briks.remove(brick)

def invert_horizontal_speed():
    ball_speed[0] *= -1

def invert_vertical_speed():
    ball_speed[1] *= -1


def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]] #index de pos = 0 #PQ POS[0]?? Il vient d'où?



pgzrun.go()
