# Dodge the fireballs
import pygame 
import random
import sys


score = 0 

pygame.init()
screen_w , screen_h = 340 , 340
screen = pygame.display.set_mode((screen_w,screen_h))
screen_rect = pygame.Rect(0, 0, screen_w, screen_h)
caption = pygame.display.set_caption("Dodge The FireBalls")
playeri = pygame.image.load("/home/crimsion/python/pygame_projects/DodgeTheFireballs/Assets/Retro player.png")
icon  = pygame.display.set_icon(playeri)
clock = pygame.time.Clock()
running = True


# player code
player = pygame.image.load("/home/crimsion/python/pygame_projects/DodgeTheFireballs/Assets/Retro player.png")
player = pygame.transform.scale(player, (32,32))
rplayer = player.get_rect()
rplayer.topleft = (150,240)

# FireBall code 
fireball = pygame.image.load("/home/crimsion/python/pygame_projects/DodgeTheFireballs/Assets/Retro fireballs.png")
fireball = pygame.transform.scale(fireball, (32,32))
rfireball = fireball.get_rect()
rfireball.x = random.randint(0,320)
print(score)

    

while running:
    
    #events setup
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False or sys.exit()
    

    screen.fill("white")
    # fills screen with color white.

    # player code here

    controls = pygame.key.get_pressed()
    rplayer.clamp_ip(screen_rect)
    if controls[pygame.K_a]:
        rplayer.x -= 1
    elif controls[pygame.K_d]:
        rplayer.x += 1
    
    screen.blit(player,rplayer)
    


    # Fireballs code here
    clock.tick(160)
    rfireball.y += 1
    if rfireball.y == 245:
        score += 1
        print(score)
        set; rfireball.y = 0
        set; rfireball.x = random.randint(0,320)
    
    if rfireball.colliderect(rplayer): # careful collidedict checks for rect dictonary not collision.

        print("GAME OVER")
        running = False


        
    screen.blit(fireball,rfireball)
        




    # updates the screen.
    pygame.display.flip()

