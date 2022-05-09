#pygame Project

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Flappy Bird"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/flappybird.png")
        self.image = pygame.transform.scale(self.image, (40, 40)  # scale

       self.rect


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- RENDER
        screen.fill(BLACK)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()