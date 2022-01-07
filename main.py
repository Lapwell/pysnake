import pygame
from sys import exit

# All constant values
FPS = 60
WIDTH, HEIGHT = 512, 512
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
GREEN = (32, 255, 32)
RED = (255, 32, 32)
WHITE = (255, 255, 255)

# Grid will be used to make the game world and store the player's position
gred = []

# I don't know what it's called when I do this, I'll call it "assigning functions." I think it's an apt description. Anyway, assigning funcs goes here.
clock = pygame.time.Clock()

# This is stuff for the snak's body
body = pygame.Rect(10, 10, 24, 24)


# This function does as its name describes, it updates the window when called so things that happen behind the scenes (like a ship moving) actually shows up.
def draw_root():
	ROOT.fill(WHITE)
	pygame.draw.rect(ROOT, GREEN, body)
	pygame.display.update()


# This is the main game function, rather obvious based on its name.
def main():

	run = True
	clock.tick(FPS)  # This limits the game so it runs at 60FPS.

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # If the event pygame.QUIT is called (in this case by pressing the exit button) it stops the loop.
				pygame.quit()
				exit()

		draw_root()


if __name__ == '__main__':
	main()
