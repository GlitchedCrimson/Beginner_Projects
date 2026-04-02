
import pygame

pygame.init()

width, height = 360, 360
screen = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption("pygame physics test (Beginner)")
fps = pygame.time.Clock()
color = (255,0,0)

loop = True

# sprites
ballr = pygame.Rect(130,50,50,50) # x,y,w,h
floore = pygame.Rect(60,230,200,30)

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    screen.fill("WHITE")

    # ball
    ball = pygame.draw.rect(screen, color, ballr) # x,y,w,h
    fps.tick(230)
    



    # floor
    floor = pygame.draw.rect(screen, color,  floore)

    
    if ballr.colliderect(floore):
        
        ballr.y -= ballr.y
        fps.tick(24)
        ballr.y = -120 / -2
        
    
    else:
        ballr.y += 1
        fps.tick(230)
    

    pygame.display.flip()