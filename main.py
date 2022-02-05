import pygame
from sys import exit
from random import randrange

pygame.init()  # Not sure why, but this is REQUIRED to be run before any other pygame code even though, without it, it runs fine. Do as those before say, at least in the beginning...

# All constant values
FPS = 10
WIDTH, HEIGHT = 400, 400  # Width and height of the window
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 32, 32)
GREEN = (32, 255, 32)
BLUE = (32, 32, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VEL = 20  # How many pixels the snake will move
snake_posx, snake_posy = 200, 200  # The starting pos of the snake

# This is where I set up pygame.events for ingame events, like moving the snake a tile or spawning power ups/enemies, if I do those.
MOVE_SNAKE_EVENT = 1
pygame.time.set_timer(MOVE_SNAKE_EVENT, 1000)

clock = pygame.time.Clock()  # I don't know what it's called when I do this, I'll call it "assigning functions." I think it's an apt description. Anyway, assigning funcs goes here.
snake_head = pygame.Rect(200, 200, 20, 20)
food_x, food_y = 110, 110
generate_food = True
move_dir = 'Right'
width_list = []  # The width of the window
height_list = []  # The height of the window


# This function is meant to be passed lists of x and y coords to check if they're the same, if they're the same that means they're colliding. Foo is for when were passing the snake's head because we
# need to add pixels for it to work properly.
def hit_check(obj1, obj2, foo):
    if foo:
        obj1[0], obj1[1] = obj1[0] + 10, obj1[1] + 10
    if obj1 == obj2:
        return True


def draw_food():
    global generate_food
    global food_x
    global food_y
    if generate_food:
        x_var = len(width_list)
        y_var = len(height_list)
        food_x = width_list[randrange(1, x_var)] + 10
        food_y = height_list[randrange(1, y_var)] + 10
        generate_food = False

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
    pygame.draw.rect(ROOT, GREEN, snake_head)
    pygame.display.update()


# This is function is for checking events (clicking the X button or getting keyboard input) and updating relevant variables.
def check_events():
    global move_dir
    # These if statements check for keyboard inputs and sets an object's (test_rect as of writing) velocity to move the object in the correct direction.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_dir = 'Up'
    if keys[pygame.K_DOWN]:
        move_dir = 'Down'
    if keys[pygame.K_LEFT]:
        move_dir = 'Left'
    if keys[pygame.K_RIGHT]:
        move_dir = 'Right'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the event pygame.QUIT is called (in this case by pressing the exit button) it stops the loop.
            pygame.quit()
            exit()
        if event.type == MOVE_SNAKE_EVENT:
            if move_dir == 'Up':
                snake_head.y -= VEL
                print('moved snake')
            if move_dir == 'Down':
                snake_head.y += VEL
                print('moved snake')
            if move_dir == 'Left':
                snake_head.x -= VEL
                print('moved snake')
            if move_dir == 'Right':
                snake_head.x += VEL
                print('moved snake')


# This is the main game function, rather obvious based on its name.
def main():
    global generate_food
    score = 0
    while True:
        food_pos = [food_x, food_y]
        snake_pos = [snake_head.x, snake_head.y]
        if hit_check(snake_pos, food_pos, True):
            generate_food = True
            score = score + 10
        check_events()
        draw_root()
        print(score)
        clock.tick(FPS)  # This limits the game, so it runs at the set FPS.


if __name__ == '__main__':
    main()
