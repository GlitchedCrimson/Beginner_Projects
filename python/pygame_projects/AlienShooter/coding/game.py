import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def asset_path(filename):
    return os.path.join(os.path.dirname(__file__), "Asset", filename)

import pygame
import random


pygame.init()

# setup
w,h = 500,500
screen = pygame.display.set_mode((w,h))
screen_rect = pygame.Rect(0,0, w,h)
pygame.display.set_caption("Alien Shooter")
clock = pygame.time.Clock()
bullet_delay = 2000
font = pygame.font.SysFont("arial", 32)
Game_over = 0
Game_overf = font.render("Game over, press R to try again...", True, "Black")
score = 0


run = True

# player
player = pygame.image.load(asset_path("Rocket.png")).convert_alpha()
player = pygame.transform.scale(player, (100,100))
rplayer = player.get_rect()
rplayer.topleft = (220,400)

# bullet
class bullet(pygame.sprite.Sprite): # the clone creation using pygame sprite func
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load(asset_path("Bullet.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = -5
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()
bullets = pygame.sprite.Group() # this helps to add clones into the game
# --
# alien bullets
class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(asset_path("ABullet.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 3
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.kill()
        if self.rect.colliderect(rplayer):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1)) # creates an event which you can later use in lots

abullets = pygame.sprite.Group()
# Aliens
class Alien(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load(asset_path("Alien.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(center=(x,y))
        self.sdelay = random.randint(1000,3000) # timer
        self.lshot = pygame.time.get_ticks() # gets timer
    def update(self):
        if self.rect.bottom < 0:
            self.kill()
    def shoot(self, gbullet):
        now = pygame.time.get_ticks()
        if now - self.lshot > self.sdelay: # checks if the timer runs out.
            Abullets = Alien_Bullets(self.rect.centerx,self.rect.bottom)
            gbullet.add(Abullets)
            self.lshot = now
            

        
        


aliens = pygame.sprite.Group()
ax = [10,50,100,150,200, 250, 300, 350]
ay = [10,50,100,150,200, 250]

# add lists to resemble shapes
Laliens = [ Alien(ax[random.randint(1,7)],ay[random.randint(1,5)]), Alien(ax[random.randint(1,7)],ay[random.randint(1,5)]) 
           , Alien(ax[random.randint(1,7)],ay[random.randint(1,5)]) , Alien(ax[random.randint(1,7)],ay[random.randint(1,5)]),
             Alien(ax[random.randint(1,7)],ay[random.randint(1,5)]), Alien(ax[random.randint(1,7)],ay[random.randint(1,5)])]
for i in range(10):
    aliens.add(Laliens[random.randint(1,5)])
    
        


while run:
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bullet = bullet(rplayer.centerx,rplayer.top)
                bullets.add(Bullet)
        if event.type == pygame.USEREVENT + 1:
            Game_over = 1
    
    if Game_over == 1:
         keys = pygame.key.get_pressed()
         screen.fill("white")
         screen.blit(Game_overf, (20,200))
         bullets.empty()
         abullets.empty()
         aliens.empty()

         if keys[pygame.K_r]:
             Game_over = 0
             score = 0
            

         pygame.display.flip()
         continue


    screen.fill("white")

    

    


# player --------------------------:
    
    screen.blit(player, rplayer)
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        rplayer.x -= 5
    if key[pygame.K_d]:
        rplayer.x += 5
    if key[pygame.K_LEFT]:
        rplayer.x -= 5
    if key[pygame.K_RIGHT]:
        rplayer.x += 5

    




    # collisions
     
    
    shot = pygame.sprite.groupcollide(aliens, bullets, True,True) # checks if bullets touch alien
    if shot:
        score += 1
    
    



    # blit stuff here
    
    
    
    if not aliens:
        for i in range(10):
            aliens.add(Laliens[random.randint(1,5)])
    
    
    

    
    aliens.update()
    aliens.draw(screen)
    abullets.update()
    abullets.draw(screen)
    for Alien in aliens:
        Alien.shoot(gbullet=abullets)


   
    



            
    rplayer.clamp_ip(screen_rect)
        
               

    bullets.update()   
    bullets.draw(screen)

    scoref = font.render(f"Score: {score}", True, "Black")

    

    screen.blit(scoref, (200,20))

    pygame.display.flip()
    clock.tick(60)
            
