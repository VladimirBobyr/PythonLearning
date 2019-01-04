
import pygame

MAX_X = 1366
MAX_Y = 768
game_over = False
bg_color = (0, 2, 0)  # Red, Geeen, Blue

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First PyGame")

print(pygame.image.get_extended())
myimage = pygame.image.load("intel.jpg").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = 100
y = 100

# =============== MAIN game loop =================== #
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x = x - 10
            if event.key == pygame.K_RIGHT:
                x = x + 10
            if event.key == pygame.K_UP:
                y = y - 10
            if event.key == pygame.K_DOWN:
                y = y + 10
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

        screen.fill(bg_color)
        screen.blit(myimage, (x, y))
        pygame.display.flip()
