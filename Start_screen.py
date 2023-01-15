import pygame
import sys
import Load_images
import rules_window
from button import Button
import settings
import os

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
music = True


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = []
    pygame_icon = pygame.image.load(os.path.join('data', 'icon.jpg'))
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption('Меню')
    pygame.init()
    if music:
        # pygame.mixer.init()
        # pygame.mixer.music.load('sounds/fon.mp3')
        # pygame.mixer.music.play(-1)
        pass
    fon = pygame.transform.scale(Load_images.load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 345
    rules_button = Button(100, 50)
    button = Button(100, 50)
    settings_button = Button(110, 50)
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('white'))
    #     intro_rect = string_rendered.get_rect()
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     intro_rect.x = 175
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)

    while True:
        rules_button.draw(286, 345, 'Правила', screen)
        settings_button.draw(480, 10, 'Настройки', screen)
        button.draw(175, 345, 'Играть', screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if rules_button.get_pressed():
                rules_window.open_rules_window()
            if settings_button.get_pressed():
                settings.open_settings_window()
            if button.get_pressed():
                pass
        pygame.display.flip()
