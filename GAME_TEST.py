import pygame


clock = pygame.time.Clock()

class box():
    def __init__(self):
        self.rect = pygame.Rect(400,400,150,150)
        self.rect2 = pygame.Rect(800,400,150,150)
        
    def move(self,screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            #self.x -= 10
            self.rect.move_ip(-10,0)
            self.draw(screen)
        if keys[pygame.K_d]:
            #self.x -= 10
            self.rect.move_ip(10,0)
            self.draw(screen)
        if keys[pygame.K_LEFT]:
            #self.x -= 10
            self.rect2.move_ip(-10,0)
            self.draw(screen)
        if keys[pygame.K_RIGHT]:
            #self.x -= 10
            self.rect2.move_ip(10,0)
            self.draw(screen)
            
            
    def draw(self,screen):
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (0,0,128), self.rect)
        pygame.draw.rect(screen,(0,0,128),self.rect2)
        
# =============================================================================
#     def stop(self):
#         while True:
#             clocka = pygame.time.Clock()
#             timer = 2 
#             dt = 0 
#             timer -= dt
#             if timer <= 0:
#                 break
#     
#             dt = clocka.tick(60) /1000
# =============================================================================
           
        
pygame.init()        
screen = pygame.display.set_mode((1600,800))
screen.fill((255,255,255))
BOX = box()        
BOX.draw(screen)
start = 0
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(60)
    BOX.move(screen)
    #BOX.draw()
    pygame.display.flip()
    
pygame.quit()
