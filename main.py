import pygame
import math

# scaling to fit my laptop screen
WINDOW_WIDTH = 1920 // 2
WINDOW_HEIGHT = 1080 // 2

CAR_WIDTH = 60
CAR_HEIGHT = 60

BORDER_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Test")

"""Map/Track Settings"""
mapImage = pygame.image.load("images/map_1.png").convert()
mapImage = pygame.transform.scale(mapImage, (WINDOW_WIDTH, WINDOW_HEIGHT)) # Scales to fit window dimensions

"""Car settings"""
carImage = pygame.image.load("images/car.png").convert_alpha() # alpha keeps transparency in png's
carImage = pygame.transform.scale(carImage, (50, 35)) # scale car image
carX = WINDOW_WIDTH // 2
carY = WINDOW_HEIGHT // 2
carAngle = 0
carSpeed = 1

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(mapImage, (0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        carX += 0.1
    if keys[pygame.K_LEFT]:
        carX -= 0.1
    if keys[pygame.K_UP]:
        carY -= 0.1
    if keys[pygame.K_DOWN]:
        carY += 0.1
    
    screen.blit(carImage, (carX, carY))
    pygame.display.flip()

pygame.quit()