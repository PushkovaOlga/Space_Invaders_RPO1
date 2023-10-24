import pygame
class hero:
  def __init__(self, screen):
    '''инициализация главного героя'''
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()
    self.screen = screen
    self.screen_rect = screen.get_rect()