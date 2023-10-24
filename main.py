import pygame
import sys

def start_game():
  '''Основная функция для описания игры'''
  pygame.init()
  screen = pygame.display.set_mode((800,600))
  pygame.display.set_caption("Самая лучшая игра")
  
  flag=True
  while flag:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        flag=False
        pygame.quit
        sys.exit()
      screen.fill((0,0,0))
      pygame.display.update()

start_game()