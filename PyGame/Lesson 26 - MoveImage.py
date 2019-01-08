
import pygame

MAX_X = 1366
MAX_Y = 768
IMAGE_SIZE = 100
game_over = False
bg_color = (0, 2, 0)  # Red, Geeen, Blue

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First PyGame")

print(pygame.image.get_extended())
myimage = pygame.image.load("spaceship.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = IMAGE_SIZE
y = IMAGE_SIZE

move_righ = False
move_left = False
move_up = False
move_down = False

# =============== MAIN game loop =================== #
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_righ = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                game_over = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_righ = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_righ:
        if x < MAX_X - IMAGE_SIZE:
            x = x + 1
        if move_left:
            if x > 0:
                x = x - 1
        if move_down:
            if y < MAX_Y - IMAGE_SIZE:
                y = y + 1
        if move_up:
            if y > 0:
                y = y - 1





        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

        screen.fill(bg_color)
        screen.blit(myimage, (x, y))
        pygame.display.flip()
