import pygame


class Button:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height

    def draw(self, x, y, message, screen):
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, 'white', (x, y, self.width, self.height))
        font = pygame.font.Font(None, 30)
        text = font.render(f'{message}', True, 'black')
        text_x = x + 10
        text_y = y + 15
        screen.blit(text, (text_x, text_y, self.width - 10, self.height - 10))

    def get_pressed(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            return True
