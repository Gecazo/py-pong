import pygame
pygame.init()

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
WIDTH, HEIGHT = 400, 400

FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pong')


class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, WIDTH, HEIGHT, color):
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        def draw(self, screen):
            pygame.draw.rectangle(screen, self.COLOR,
                                  (self.x, self.y, self.WIDTH, self.HEIGHT))


def draw(screen):
    screen.fill(BLACK)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)

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