import pygame
import sys
import os

from pygame import mixer
mixer.init()
pygame.init()
WIN = pygame.display.set_mode((1000,690))
BACKGROUND = pygame.image.load(os.path.join("Assests","space.png"))
BACKGROUND1 = pygame.transform.rotate(BACKGROUND,90)
SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("Assests","spaceship.png")),(60,60))
SPACE_SHIP = pygame.transform.rotate(SPACE_SHIP, 180)
ENEMY = pygame.transform.scale(pygame.image.load(os.path.join("Assests","enemy.png")),(55,55))
SPEED = 10

bgY1 = 0
bgX1 = 0
 
bgY2 = -BACKGROUND.get_height()
bgX2 = 0
        
def update(value):
    global bgY1,bgX1,bgY2,bgX2
    WIN.blit(BACKGROUND, (bgX1, bgY1))
    WIN.blit(BACKGROUND1, (bgX2, bgY2))
    bgY1 += value
    bgY2 += value
   
    if bgY1 >= BACKGROUND.get_height():
        bgY1 = -BACKGROUND.get_height()
    if bgY2 >= BACKGROUND.get_height():
        bgY2 = -BACKGROUND.get_height()
    

def draw_window(block,value,bullets):
    #Moving background Logic
    update(value)
    
   

    
    for bullet in bullets:
        pygame.draw.rect(WIN,"red",bullet)
    WIN.blit(SPACE_SHIP,(block.x,block.y))
    WIN.blit(ENEMY,(700,80))
    pygame.display.update()
def control_movement(key_pressed,block):
    if key_pressed[pygame.K_UP] and block.y >0:
        block.y -= SPEED
        
    if key_pressed[pygame.K_DOWN] and block.y <610:
        block.y +=SPEED
    if key_pressed[pygame.K_LEFT] and block.x >0:
        block.x -=SPEED
    if key_pressed[pygame.K_RIGHT] and block.x <920:
        block.x +=SPEED


def handle_bullets(bullets):
    for bullet in bullets:
        bullet.y -= 15
        if bullet.y < 0:
            bullets.remove(bullet)


def main():
        block  = pygame.Rect(450,600,60,60)
        value = 1
        bullets = []
        
        
        while True:
            clock = pygame.time.Clock()
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(bullets) <10:
                                    
                        bullet = pygame.Rect(block.x+block.width-30,block.y+block.height//2-2,5,10)
                        mixer.music.load(os.path.join("Assests","Gun+Silencer.mp3"))
                        mixer.music.play()
                        mixer.music.set_volume(0.2)
                        bullets.append(bullet) 
            key_pressed = pygame.key.get_pressed()
            
            
            
            
            draw_window(block,value,bullets)
            handle_bullets(bullets)
            control_movement(key_pressed,block)
        
if __name__ == "__main__":
    main()