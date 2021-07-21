import pygame
import io

pygame.init()
  
disp_w = 800
disp_h = 600

game_display = pygame.display.set_mode((disp_w,disp_h))
pygame.display.set_caption('Is This Working?')
  
black = (0,0,0)
white = (255,255,255)

racoon_img = pygame.image.load('racoon.jpeg')

def racoon(x,y):
    game_display.blit(racoon_img, (x,y))

# define starting point of racoon
x = (disp_w * 0.3)
y = (disp_h * 0.5)
    

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():  # all events registered in queue, use .get()
        if event.type == pygame.QUIT:  #  QUIT == close button, therefore terminate program
            crashed = True
        #print(event)

    game_display.fill(white)
    racoon(x,y)

    pygame.display.update()  # update portions of the screen for software displays
    clock.tick(60)   # 60 FPS

pygame.quit()
quit()

