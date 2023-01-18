import pygame
import sys
import os
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, player_group)
        self.pos_x = 170
        self.pos_y = 360
        self.image = player_image
        self.rect = self.image.get_rect().move(self.pos_x, self.pos_y)
        self.speed = 8

    def update(self):
        if pygame.sprite.spritecollideany(self, enemy_group) or pygame.sprite.spritecollideany(self, bullets_group):
            # Проиграли
            pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(enemy_group, all_sprites)
        self.image = enemy_image
        self.rect = self.image.get_rect().move(randint(-5, 385), -10)
        self.health = 2
        self.timer = 0

    def update(self):
        global enemy_counter
        self.rect.y += 2
        self.timer += 1

        if not self.timer % enemy_reload_cooldown:
            Bullet(self.rect.x + 26, self.rect.y + 70, -5)

        if pygame.sprite.spritecollideany(self, bullets_group):
            self.health -= 1
            for bullet in bullets_group:
                if pygame.sprite.spritecollideany(bullet, enemy_group):
                    bullet.kill()

        if not self.health:
            self.kill()
            enemy_counter += 1


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(enemy_group, all_sprites)
        self.image = meteor_image
        self.rect = self.image.get_rect().move(randint(-5, 385), -10)
        self.health = 4

    def update(self):
        global enemy_counter
        self.rect.y += 1

        if pygame.sprite.spritecollideany(self, bullets_group):
            self.health -= 1
            for bullet in bullets_group:
                if pygame.sprite.spritecollideany(bullet, enemy_group):
                    bullet.kill()

        if not self.health:
            self.kill()
            enemy_counter += 1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__(bullets_group, all_sprites)
        self.pos_x = x
        self.pos_y = y
        self.image = pygame.Surface((8, 14))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.counter = 2

    def update(self):
        self.pos_y -= self.speed
        self.rect = self.image.get_rect().move(self.pos_x, self.pos_y)

        if not game_area.contains(self.rect):
            self.kill()


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = star_image
        self.rect = self.image.get_rect().move(randint(-5, 385), -10)

    def update(self):
        global reload_cooldown
        global enemy_counter
        self.rect.y += 1

        if pygame.sprite.spritecollideany(self, player_group):
            if reload_cooldown > 10:
                reload_cooldown -= 3
            else:
                enemy_counter += 1
            self.kill()


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


pygame.init()
pygame.display.set_caption('space invaders')
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
game_area = pygame.Rect(-20, -10, 430, 600)

reload_cooldown = 30
enemy_reload_cooldown = 75
fps = 60
enemy_counter = 0

enemy_cooldown = 200
meteor_cooldown = 300
enemy_timer = 0
meteor_timer = 0
reload_timer = 0
star_timer = 0


player_image = pygame.transform.scale(load_image('spaceship.png'), (60, 60))
enemy_image = pygame.transform.scale(load_image('enemyship.png'), (60, 60))
meteor_image = pygame.transform.scale(load_image('meteor.png'), (60, 60))
star_image = pygame.transform.scale(load_image('star.png'), (60, 60))

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()

player = Player()

clock = pygame.time.Clock()
running = True
while running:

    screen.fill((0, 0, 0))

    f = pygame.font.Font(None, 44)
    text = f.render(str(enemy_counter), True, (180, 0, 0))

    reload_timer -= 1
    if reload_timer < 0:
        Bullet(player.rect.x + 26, player.rect.y, 15)
        reload_timer = reload_cooldown

    enemy_timer += 1
    if enemy_timer == enemy_cooldown:
        Enemy()
        if enemy_cooldown > 50:
            enemy_cooldown = enemy_cooldown - 8
        enemy_timer = 0

    meteor_timer += 1
    if meteor_timer == meteor_cooldown:
        Meteor()
        if meteor_cooldown > 50:
            meteor_cooldown = meteor_cooldown - 8
        meteor_timer = 0

    star_timer += 1
    if star_timer == 550:
        Star()
        star_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            if player.rect.x > -10:
                player.pos_x -= player.speed

        if keystate[pygame.K_d]:
            if player.rect.x + player.rect.w <= 410:
                player.pos_x += player.speed

        if keystate[pygame.K_s]:
            if player.rect.y + player.rect.h < 610:
                player.pos_y += player.speed

        if keystate[pygame.K_w]:
            if player.rect.y > -10:
                player.pos_y -= player.speed

        player.rect = player.image.get_rect().move(player.pos_x, player.pos_y)

    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(text, (190, 40))

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
