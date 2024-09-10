import pygame
import pygame
pygame.init()

pygame.init()

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("benitoroei")
x = 50
y = 50
vet = 5
imp = pygame.image.load("BENI.png")
imp = pygame.transform.scale(imp, (40 , 80))
running = True

while running:
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    # screen.blit(imp, (0, 0))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x+= 1
    if keys[pygame.K_DOWN]:
        y+= 1
    if keys[pygame.K_UP]:
        y -= 1
    screen.fill("dark green")
    screen.blit(imp ,(x, y))
    pygame.display.update()
print("1")











        for row in range(25):
            for column in range(50):
                color = GREEN
                if grid[row][column] == 1:
                    color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
