"""
Проект
"""
import pygame
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, player_group)
        self.pos_x = 150
        self.pos_y = 360
        self.image = player_image
        self.rect = self.image.get_rect().move(self.pos_x, self.pos_y)
        self.speed = 10


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.pos_x = x
        self.pos_y = y
        self.image = pygame.Surface((8, 14))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = 1


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


pygame.init()
pygame.display.set_caption('space invaders')
size = width, height = 360, 500
screen = pygame.display.set_mode(size)

bullets = list()
cooldown = 120

player_image = pygame.transform.scale(load_image('spaceship.png'), (60, 60))

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()

player = Player()

running = True
while running:

    screen.fill((0, 0, 0))

    cooldown -= 1
    if cooldown == 0:
        bullets.append(Bullet(player.rect.x + 26, player.rect.y))
        cooldown = 120

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.pos_x -= player.speed
            elif event.key == pygame.K_d:
                player.pos_x += player.speed
            if event.key == pygame.K_s:
                player.pos_y += player.speed
            elif event.key == pygame.K_w:
                player.pos_y -= player.speed

        player.rect = player.image.get_rect().move(player.pos_x, player.pos_y)

    # for i in range(len(bullets)):
    #     bullets[i].pos_y -= bullets[i].speed
    #     bullets[i].rect = bullets[i].image.get_rect().move(bullets[i].pos_x, bullets[i].pos_y)
    #
    #     if bullets[i].pos_y < 0:
    #         del bullets[i]

    for bullet in bullets:
        bullet.pos_y -= bullet.speed
        bullet.rect = bullet.image.get_rect().move(bullet.pos_x, bullet.pos_y)

        if bullet.pos_y < 0:
            bullets.remove(bullet)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
