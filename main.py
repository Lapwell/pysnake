import pygame
from sys import exit
from random import randrange

pygame.init()  # Not sure why, but this is REQUIRED to be run before any other pygame code even though, without it, it runs fine. Do as those before say, at least in the beginning...

# All constant values
FPS = 1
WIDTH, HEIGHT = 600, 600
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 32, 32)
GREEN = (32, 255, 32)
BLUE = (32, 32, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VEL = 5
X, Y = 100, 100              # The starting pos of the snake

clock = pygame.time.Clock()  # I don't know what it's called when I do this, I'll call it "assigning functions." I think it's an apt description. Anyway, assigning funcs goes here.
test_rect = pygame.Rect(200, 200, 20, 20)
food_x, food_y = 10, 10
generate_food = True
width_list = []
height_list = []


def draw_food():
    global generate_food
    global food_x
    global food_y
    if generate_food:
        x_var = len(width_list)
        y_var = len(height_list)
        print(x_var, y_var)
        food_x = width_list[randrange(1, x_var)] + 10
        food_y = height_list[randrange(1, y_var)] + 10
        generate_food = False

    print(food_x, food_y)
    pygame.draw.circle(ROOT, RED, (food_x, food_y), 10)


def draw_grid():
    square_size = 20
    for x in range(0, WIDTH, square_size):
        width_list.insert(len(width_list), x)
        for y in range(0, HEIGHT, square_size):
            height_list.insert(len(height_list), y)
            rect = pygame.Rect(x, y, square_size, square_size)
            pygame.draw.rect(ROOT, WHITE, rect, 1)


# This function does as its name describes, it updates the window when called so things that happen behind the scenes (like a ship moving) actually shows up.
def draw_root():
    ROOT.fill(BLACK)
    draw_grid()
    draw_food()
    pygame.draw.rect(ROOT, GREEN, test_rect)
    pygame.display.update()


# This is function is for checking events (clicking the X button or getting keyboard input) and updating relevant variables.
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the event pygame.QUIT is called (in this case by pressing the exit button) it stops the loop.
            pygame.quit()
            exit()

    # These if statements check for keyboard inputs and sets an object's (test_rect as of writing) velocity to move the object in the correct direction.
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
