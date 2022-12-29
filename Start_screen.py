import pygame
import sys
import Load_images
import rules_window
from button import Button

size = width, height = 600, 400
screen = pygame.display.set_mode(size)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = []
    pygame.display.set_caption('Меню')
    pygame.init()
    fon = pygame.transform.scale(Load_images.load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 345
    button = Button(90, 50)
    button.draw(175, 345, 'Играть', screen)
    rules_button = Button(90, 50)
    rules_button.draw(286, 345, 'Правила', screen)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 175
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if button.get_pressed():
                return
            if rules_button.get_pressed():
                rules_window.open_rules_window()
        pygame.display.flip()
