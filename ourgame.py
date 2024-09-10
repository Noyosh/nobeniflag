import pygame
import pygame
pygame.init()

pygame.init()

pygame.init()
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("benitoroei")
screen.fill(" dark green")

pygame.display.set_caption('image')


imp = pygame.image.load("BENI.png").convert()

running = True

while running:
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        pygame.display.flip()
        # keys=pygame.key.get_pressed()
        #
        # if keys[pygame.K_LEFT]:
        #
        # if keys[pygame.K_RIGHT]:
        #
        # if keys[pygame.K_DOWN]:
        #
        # if keys[pygame.K_UP]:































































































