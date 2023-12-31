import pygame, controls
from hero import Hero
from pygame.sprite import Group

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    enemys = Group()

    flag = True
    while flag:
        controls.events(screen, hero, bullets)
        hero.moving_hero(screen)

        controls.update(screen, hero, enemys, bullets)
        controls.update_bullets(screen, bullets)
        controls.create_army(screen,enemys)

start_game()
