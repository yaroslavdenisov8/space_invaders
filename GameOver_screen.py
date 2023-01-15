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


def end_screen():
    intro_text = ["Game Over"]
    pygame.display.set_caption('Конец игры')
    pygame.init()
    fon = pygame.transform.scale(Load_images.load_image('fon2.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 60)
    text_coord = 30
    button = Button(90, 50)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        button.draw(250, 300, 'Заново', screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if button.get_pressed():
                Start_screen.start_screen()
        pygame.display.flip()


end_screen()