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
    
    pygame.display.flip()
    screen.fill(bg)
    hero.output_hero()
start_game()