import pygame


pygame.init()
background_colour = (234, 212, 252)
  
screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('IS THIS WORKING')
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
# Update the full display Surface to the screen
pygame.display.flip()

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():  # all events registered in queue, use .get()
        if event.type == pygame.QUIT:  #  QUIT == close button, therefore terminate program
            crashed = True
        print(event)
    pygame.display.update()  # update portions of the screen for software displays
    clock.tick(60)

