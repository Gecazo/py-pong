import pygame
pygame.init()

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
WIDTH, HEIGHT = 400, 400

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pong')


class Paddle():
    COLOR = WHITE

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(screen, paddles):
    screen.fill(BLACK)

    for paddle in paddles:
        paddle.draw(screen)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)

    running = True
    while running:
        clock.tick(FPS)
        draw(screen, [left_paddle, right_paddle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    pygame.quit()


if __name__ == '__main__':
    main()