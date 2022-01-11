import pygame
from sys import exit

pygame.init()  # Not sure why, but this is REQUIRED to be run before any other pygame code, even though, without it, it runs fine. Do as those before say, at least in the beginning...

# All constant values
FPS = 60
WIDTH, HEIGHT = 512, 512
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 32, 32)
GREEN = (32, 255, 32)
BLUE = (32, 32, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

grid = []  # Grid will be used to make the game world and store the player's position
clock = pygame.time.Clock()  # I don't know what it's called when I do this, I'll call it "assigning functions." I think it's an apt description. Anyway, assigning funcs goes here.
body = pygame.Rect(10, 10, 24, 24)  # This is stuff for the snak's body


# This function does as its name describes, it updates the window when called so things that happen behind the scenes (like a ship moving) actually shows up.
def draw_root():
	ROOT.fill(WHITE)
	pygame.draw.rect(ROOT, GREEN, body)
	pygame.display.update()


# This function is for the user to set the number of row and columns for the game.
def start_menu():
	ROOT.fill(BLACK)



# This is the main game function, rather obvious based on its name.
def main():

	start_menu()
	print('test 1')
	start_menu_true = True
	while start_menu_true:
		start_menu()

	while True:

		clock.tick(FPS)  # This limits the game so it runs at 60FPS.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # If the event pygame.QUIT is called (in this case by pressing the exit button) it stops the loop.
				pygame.quit()
				exit()
		draw_root()


if __name__ == '__main__':
	main()
