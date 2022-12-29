import pygame


class Button:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height

    def draw(self, x, y, message, screen):
        self.x = x
        self.y = y
        pygame.draw.rect(screen, (255, 229, 180), (x, y, self.width, self.height))
        font = pygame.font.Font(None, 30)
        text = font.render(f'{message}', True, (220, 20, 60))
        text_x = self.width // 2 - text.get_width() // 2 + self.x
        text_y = self.height // 2 - text.get_height() // 2 + self.y
        screen.blit(text, (text_x, text_y, self.width - 10, self.height - 10))

    def get_pressed(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1:
            if self.x < mouse[0] < self.x + self.width:
                if self.y < mouse[1] < self.y + self.height:
                    return True
        return False