import pygame
import math

# scaling to fit my laptop screen
WINDOW_WIDTH = 1920 // 2
WINDOW_HEIGHT = 1080 // 2

CAR_WIDTH = 60
CAR_HEIGHT = 60

BORDER_COLOR = (255, 255, 255, 255) 

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Test")

"""Map/Track Settings"""
mapImage = pygame.image.load("images/map_1.png").convert()
mapImage = pygame.transform.scale(mapImage, (WINDOW_WIDTH, WINDOW_HEIGHT)) # Scales to fit window dimensions

"""Car settings"""
class Car:
    def __init__(self):
        carImage = pygame.image.load("images/car.png").convert_alpha() # alpha keeps transparency in png's
        self.carImage = pygame.transform.scale(carImage, (50, 35)) # scale car image
        self.carX = WINDOW_WIDTH // 2
        self.carY = WINDOW_HEIGHT - 50 # Random value to have car on track to start (map1)
        self.carAngle = 0  # Current rotation angle in degrees
        self.carSpeed = 2  
        self.rotationSpeed = 3

        self.alive = True # Did car crash?

running = True
clock = pygame.time.Clock()

testCar = Car()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(mapImage, (0, 0))

    keys = pygame.key.get_pressed()

    moving = False  # Handle rotation and movement
    
    # Move forward in the direction the car is facing
    if keys[pygame.K_UP]:
        testCar.carX += testCar.carSpeed * math.cos(math.radians(testCar.carAngle))
        testCar.carY += testCar.carSpeed * math.sin(math.radians(testCar.carAngle))
        moving = True

    # Move backward (reverse)
    if keys[pygame.K_DOWN]:
        testCar.carX -= testCar.carSpeed * math.cos(math.radians(testCar.carAngle))
        testCar.carY -= testCar.carSpeed * math.sin(math.radians(testCar.carAngle))
        moving = True
    
    if moving:
        if keys[pygame.K_LEFT]:
            testCar.carAngle -= testCar.rotationSpeed
        if keys[pygame.K_RIGHT]:
            testCar.carAngle += testCar.rotationSpeed
    
    testCar.carAngle = testCar.carAngle % 360 # Keep angle within 0-360 degrees
    
    rotatedCar = pygame.transform.rotate(testCar.carImage, -testCar.carAngle)  # Negative because pygame's coordinate system
    
    # Get the rect of the rotated image and center it on the car position
    carRect = rotatedCar.get_rect()
    carRect.center = (testCar.carX, testCar.carY)

    # If center of car hits edge, it "dies"
    if(screen.get_at((int(testCar.carX), int(testCar.carY))) == BORDER_COLOR):
        testCar.alive = False

    if (testCar.alive):
        screen.blit(rotatedCar, carRect)
    else:
        pass
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()