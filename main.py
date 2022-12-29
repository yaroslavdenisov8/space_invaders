import pygame
import os
import sys
from Load_images import load_image
from button import Button
from Start_screen import start_screen

size = width, height = 600, 400
screen = pygame.display.set_mode(size)


def main():
    pygame.init()
    start_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.quit()


main()
