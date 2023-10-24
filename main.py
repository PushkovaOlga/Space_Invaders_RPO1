import pygame
import sys 
from hero import Hero

def start_game():
  '''Основная функция для описания игры'''
  pygame.init()
  screen = pygame.display.set_mode((800,600))
  pygame.display.set_caption("Самая лучшая игра")
  bg=(255,255,255)
  
  hero = Hero(screen)
  
  flag=True
  while flag:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        flag=False
        sys.exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
                hero.rect.x -= 15   # сдвигаем героя влево
          elif event.key == pygame.K_RIGHT:
                hero.rect.x += 15   # сдвигаем героя вправо
          elif event.key == pygame.K_UP:
                hero.rect.y -= 15   # сдвигаем героя вверх
          elif event.key == pygame.K_DOWN:
                hero.rect.y += 15   # сдвигаем героя вниз
    
    pygame.display.flip()
    screen.fill(bg)
    hero.output_hero()
start_game()