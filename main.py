import pygame
import os
import sys
import Load_images
from button import Button
import Start_screen


pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
Start_screen.start_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()
