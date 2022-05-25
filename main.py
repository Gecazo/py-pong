import pygame
pygame.init()  

white, black = (255, 255, 255), (0, 0, 0) 
width, height = 400, 400

fps = 120

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pong')
  
class Paddle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        def draw(self, screen):
            pygame.draw.rectangle(screen, self.color, (self.x, self.y, self.width, self.height))

def draw(screen):
    screen.fill(black)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(fps)

    draw(screen)

    running = True
    while running:
        for event in pygame.event.get():      
            if event.type == pygame.QUIT:
                running = False
                break
    pygame.quit()


if __name__ == '__main__':
    main()