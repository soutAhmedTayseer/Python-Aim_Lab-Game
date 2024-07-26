import pgzrun
from random import randint
import time
import pygame
background =Actor("background")
ball1=Actor("ball1")
ball2=Actor("ball2")
ball3=Actor("ball3")
ball4=Actor("ball4")
HEIGHT=600
WIDTH=900
score=0
Level=1
timer = 0
Win = 700
start_time = time.time()
game_over=False
def draw ():
    screen.clear()
    
    background.draw()
    
    ball1.draw()
    
    ball2.draw()
    
    ball3.draw()
    
    ball4.draw()
    
    
    screen.draw.text("Score: "+str(score) ,color="yellow", topleft=(420,10))
    
    screen.draw.text("Level: "+str(int(score/100+1)) ,color="yellow", topleft=(800,10))
    
    screen.draw.text(str(40-timer) ,color="yellow", topleft=(10,10),fontsize=30)
    
    if score == 100:
       ball1._surf = pygame.transform.scale(ball1._surf, (40, 40))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (40, 40))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (40, 40))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (40, 40))
       ball4._update_pos()

       
    if score == 200:
       ball1._surf = pygame.transform.scale(ball1._surf, (35, 35))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (35, 35))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (35, 35))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (35, 35))
       ball4._update_pos()

       
    if score == 300:
       ball1._surf = pygame.transform.scale(ball1._surf, (30, 30))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (30, 30))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (30, 30))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (30, 30))
       ball4._update_pos()

       
    if score == 400:
       ball1._surf = pygame.transform.scale(ball1._surf, (25, 25))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (25, 25))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (25, 25))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (25, 25))
       ball4._update_pos()

       
    if score == 500:
       ball1._surf = pygame.transform.scale(ball1._surf, (20, 20))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (20, 20))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (20, 20))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (20, 20))
       ball4._update_pos()

       
    if score == 600:
       ball1._surf = pygame.transform.scale(ball1._surf, (15, 15))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (15, 15))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (15, 15))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (15, 15))
       ball4._update_pos()

       
    if score == 700:
       ball1._surf = pygame.transform.scale(ball1._surf, (10, 10))
       ball1._update_pos()
       ball2._surf = pygame.transform.scale(ball2._surf, (10, 10))
       ball2._update_pos()
       ball3._surf = pygame.transform.scale(ball3._surf, (10, 10))
       ball3._update_pos()
       ball4._surf = pygame.transform.scale(ball4._surf, (10, 10))
       ball4._update_pos()
    

    if game_over==True and score >= Win:
        background.draw()
        screen.draw.text("You Won ^_^ ",color="white", topleft=(325,260),fontsize=60)
        screen.draw.text("Final Score: "+str(score) ,color="white", topleft=(280,320),fontsize=60)
    elif game_over==True and score < Win:
        background.draw()
        screen.draw.text("You Lost -_- ",color="white", topleft=(310,260),fontsize=60)
        screen.draw.text("Final Score: "+str(score) ,color="white", topleft=(280,320),fontsize=60)
        

def update():
    global timer
    global Level
    # Calculate the elapsed time since the start
    elapsed_time =  time.time() - start_time
    # Update the timer variable as an integer
    timer = int(elapsed_time)

def place_ball1():
    ball1.x=randint(100,700)
    ball1.y=randint(100,400)
    
def place_ball2():
    ball2.x=randint(100,700)
    ball2.y=randint(100,400)
    
def place_ball3():
    ball3.x=randint(100,700)
    ball3.y=randint(100,400)
    
def place_ball4():
    ball4.x=randint(100,700)
    ball4.y=randint(100,400)
    
place_ball1()
place_ball2()
place_ball3()
place_ball4()
def on_mouse_down(pos):
    
    global score
    
    if ball1.collidepoint(pos):
        print("GREAT!!")
        place_ball1()
        score=score+10
        
    elif ball2.collidepoint(pos):
        print("GREAT!!")
        place_ball2()
        score=score+10
        
    elif ball3.collidepoint(pos):
        print("GREAT!!")
        place_ball3()
        score=score+10
        
    elif ball4.collidepoint(pos):
        print("GREAT!!")
        place_ball4()
        score=score+30
        
    else:
        print("CLOSE!")
        score=score-10

        
        
def time_up():
    global game_over
    game_over=True
clock.schedule(time_up,40.0)

pgzrun.go()
