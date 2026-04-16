import pgzrun

from pgzero.builtins import *
import pgzero.screen
screen : pgzero.screen.Screen
 
import os
os.environ["SDL_VIDEO_CENTERED"] = "1" 



WIDTH = 800
HEIGHT = 600

game_done = False

all_briks = []


music.play("start")

for x in range(0, 800 , 100):
    for y in range(0, 80, 30):
        brick2 = Actor("brick2",anchor = ["left","top"])
        brick2.pos = [x,y]
        all_briks.append(brick2)

for x in range(0, 800 , 100):
    for y in range(30, 80, 30):
        brick1 = Actor("brick1",anchor = ["left","top"])
        brick1.pos = [x,y] 
        all_briks.append(brick1)
       



msg = Actor("big_finish", anchor = ["left","top"])
msg.pos = [0,0]
player = Actor("player")
player.pos = [400,550] 

lives3 = Actor("lives3", anchor = ["left","bottom"])
lives3.pos = [10,610]
lives2 = Actor("lives2", anchor = ["left","bottom"])
lives2.pos = [10,610]
lives1 = Actor("lives1", anchor = ["left","bottom"])
lives1.pos = [10,610]
all_lives = [lives3,lives2,lives1]


ball = Actor("ball2")
ball.pos = [400,300]

ball_speed = [5,5]

def no_lives_left():
    screen.clear()
    game_over = Actor("gameover", anchor = ["left","top"])
    game_over.pos = [0,0]
    game_over.draw()
    global ball_speed 
    ball_speed = [0,0]
    player.pos = [400,550]
    
    

def draw():
    screen.clear()
    screen.fill("violetred3")
    
    for brick in all_briks:
        brick.draw()

    if len(all_lives) > 0 :
        all_lives[0].draw()
    elif len(all_lives) == 0:
            screen.clear()
            no_lives_left()
            
    player.draw() 
    ball.draw()
    if ball.bottom > HEIGHT: 
        on_key_down(keyboard.SPACE)

    if game_done:
        msg.draw()

def update():
    if len(all_briks) == 0:
            global game_finished
            game_finished = True
            return
    
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.right > WIDTH or ball.left < 0:
        invert_horizontal_speed()
        sounds.sfx_hurt.play()

    if ball.top < 0:
        invert_vertical_speed()
        sounds.sfx_hurt.play()
        
    
    if ball.bottom > HEIGHT: 
        
        sounds.sfx_disappear.play()
        ball.pos = [400,300]
        
        if len(all_lives) > 0:
            all_lives.pop(0)
            music.play("restart")
        else:
            no_lives_left()
            music.play("game_over")
    
        

    if ball.colliderect(player):
        invert_vertical_speed()
        sounds.sfx_throw.play()
        
    
    to_delet = []
    
    for brick in reversed(all_briks):
        if ball.colliderect(brick):
            to_delet.append(brick)
            invert_vertical_speed()
            sounds.sfx_bump.play()
            break
            
               
    for brick in to_delet:
        all_briks.remove(brick)
        break
    



def invert_horizontal_speed():
    ball_speed[0] *= -1

def invert_vertical_speed():
    ball_speed[1] *= -1


def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]] 

def on_key_down(key):
    global ball_speed
    if key == keyboard.SPACE:
        ball.pos = [400, 300]
        ball_speed = [-6,6]
        

pgzrun.go()