# import pygame module
import  pygame
  
pygame.init()
  
# width
width = 800
  
# height
height = 600
  
#store he screen size
z = [width,height]
  
# store the color
white = (255, 255, 255)
screen_display = pygame.display
  
# Set caption of screen
screen_display.set_caption('REMARCA')
  
# setting the size of the window
surface = screen_display.set_mode(z)
  
# set the image which to be displayed on screen
python = pygame.image.load('logo_2016.jpg')
  
# set window true
window = True
while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
              
            # display white on screen other than image
    surface.fill(white)
      
# draw on image onto another
    surface.blit(python,(0, 0))
    screen_display.update()
  
pygame.quit()
