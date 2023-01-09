import pygame
import sys
import Load_images
from button import Button
import Start_screen

size = width, height = 600, 400
screen = pygame.display.set_mode(size)


def terminate():
    pygame.quit()
    sys.exit()


def open_settings_window():
    intro_text = ['Громкость', 'Музыка']
    pygame.display.set_caption('Настройки')
    pygame.init()
    fon = pygame.transform.scale(Load_images.load_image('fon2.jpg'), (width, height))

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 80
    button = Button(90, 50)
    button.draw(10, 10, 'Назад', screen)
    button_decrease_volume = Button(20, 20)
    button_decrease_volume.draw(150, 90, '-', screen)
    button_increase_volume = Button(20, 20)
    button_increase_volume.draw(180, 90, '+', screen)
    button_turnOff_music = Button(50, 20)
    button_turnOff_music.draw(150, 120, 'выкл', screen)
    button_turnOn_music = Button(50, 20)
    button_turnOn_music.draw(205, 120, 'вкл', screen)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if button.get_pressed():
                Start_screen.start_screen()
            if button_decrease_volume.get_pressed():
                # убавляем фон. музыку
                pass
            if button_increase_volume.get_pressed():
                # прибавляем фон. музыку
                pass
            if button_turnOff_music.get_pressed():
                Start_screen.music = False
            if button_turnOff_music.get_pressed():
                Start_screen.music = True
        pygame.display.flip()
