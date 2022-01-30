import pygame
from sys import exit

pygame.init()  # Not sure why, but this is REQUIRED to be run before any other pygame code even though, without it, it runs fine. Do as those before say, at least in the beginning...

# All constant values
FPS = 30
WIDTH, HEIGHT = 500, 500
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 32, 32)
GREEN = (32, 255, 32)
BLUE = (32, 32, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VEL = 5


clock = pygame.time.Clock()  # I don't know what it's called when I do this, I'll call it "assigning functions." I think it's an apt description. Anyway, assigning funcs goes here.
test_rect = pygame.Rect(200, 200, 10, 10)
x, y = 100, 100              # The starting pos of the snake


# This function does as its name describes, it updates the window when called so things that happen behind the scenes (like a ship moving) actually shows up.
def draw_root():
    ROOT.fill(BLACK)
    pygame.draw.rect(ROOT, GREEN, test_rect)
    pygame.display.update()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the event pygame.QUIT is called (in this case by pressing the exit button) it stops the loop.
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        test_rect.y -= VEL
    if keys[pygame.K_DOWN]:
        test_rect.y += VEL
    if keys[pygame.K_LEFT]:
        test_rect.x -= VEL
    if keys[pygame.K_RIGHT]:
        test_rect.x += VEL


# This is the main game function, rather obvious based on its name.
def main():
    while True:
        check_events()
        draw_root()
        clock.tick(FPS)  # This limits the game, so it runs at the set FPS.


if __name__ == '__main__':
    main()
