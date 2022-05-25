import pygame
  
white, black = (255, 255, 255), (0, 0, 0) 

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('pong')
screen.fill(black)
  
#pygame.display.flip()
  
pygame.draw.polygon(screen, white,
                    [(146, 0), (291, 106),
                    (236, 277), (56, 277), (0, 106)])

pygame.draw.line(screen, white,
                (60, 300), (120, 300), 4)

pygame.draw.circle(screen,
           white, (300, 50), 20, 0)

pygame.draw.ellipse(screen, white,
                    (300, 250, 40, 80), 1)

running = True
while running:
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            running = False