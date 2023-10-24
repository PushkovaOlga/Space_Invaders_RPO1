import pygame
class Hero:
  def __init__(self, screen):
    '''инициализация главного героя'''
    self.image = pygame.image.load("images/hero.png")
    self.rect = self.image.get_rect()
    self.screen = screen
    self.screen_rect = screen.get_rect()
  def output_hero(self):
    self.screen.blit(self.image, self.rect)