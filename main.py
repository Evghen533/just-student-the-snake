import pygame
from random import randint

class GameObject:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color

    def draw(self):
        pass

class Circle(GameObject):
    def __init__(self, surface, color, x, y, radius, speed):
        super().__init__(surface, color)
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = 1

    def draw(self):
        pygame.draw.circle(self.surface, 
                            self.color, 
                            (self.x, self.y), 
                            self.radius)


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
SCREEN_CENTER_X, SCREEN_CENTER_Y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
FPS = 10

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

circle = Circle(screen, (255, 0, 0), SCREEN_CENTER_X, SCREEN_CENTER_Y, 40, 10)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circle.direction = -1
            if event.key == pygame.K_RIGHT:
                circle.direction = 1
    screen.fill((0, 0, 0))
    circle.draw()
    if circle.x + circle.radius >= SCREEN_WIDTH:
        circle.direction = -1
    if circle.x - circle.radius <= 0:
        circle.direction = 1
    circle.x += circle.speed * circle.direction
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()