import pygame,sys

class crosshair(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,color):
        super().__init__()
        self.image =pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
      #  self.rect.center = [pos_x,pos_y]

pygame.init()
clock = pygame.time.Clock()


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("neww.jpg")  
backgrass = pygame.image.load("newgrass.jpg")  
backlight = pygame.image.load("newstreetoff.png")  

crosshair = crosshair(50,50,500,500,(255,255,255))
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)  


while True:
   for event in pygame.event.get():
       
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
       
       pygame.display.flip()
       screen.blit(background,(100,300)) 
       screen.blit(background,(400,300))  #for rendering background display
       screen.blit(background,(795,300))  #for rendering background display
       screen.blit(background,(1190,300))  #for rendering background display
       screen.blit(background,(1300,300))
       screen.blit(backgrass,(200,100))  #for rendering background display
       screen.blit(backgrass,(700,100))  #for rendering background display
       screen.blit(backgrass,(1100,100))  #for rendering background display
       screen.blit(backlight,(400,400))  #for rendering background display
      
    


       crosshair_group.draw(screen)
       clock.tick(60)      
        
       
    
