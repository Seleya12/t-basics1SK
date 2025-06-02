import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Emily in Space')

IMAGE_PATH = "IMG_0958.jpeg"

class Emily:
    def __init__(self):
        img = pygame.image.load(IMAGE_PATH).convert_alpha()
        self.original_img = pygame.transform.scale(img, (100, 100))
        self.img = self.original_img.copy()
        self.center_x = random.randint(100, 700)
        self.center_y = random.randint(100, 500)
        self.radius = random.randint(50, 150)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(0.01, 0.05)
        self.rotation = 0
        self.tint_color = (
            random.randint(0, 50),
            random.randint(0, 50),
            random.randint(0, 50)
        )
        self.original_img.fill((*self.tint_color, 0), special_flags=pygame.BLEND_RGB_ADD)

    def animate(self):
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)
        self.rotation = (self.rotation + 1) % 360
        self.img = pygame.transform.rotate(self.original_img, self.rotation)
        self.angle += self.speed

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

emilys = [Emily() for _ in range(random.randint(5, 10))]
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill((30, 30, 30))
    for emily in emilys:
        emily.animate()
        emily.draw()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
