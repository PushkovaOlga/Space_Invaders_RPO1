import pygame
import sys
from hero import Hero

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Самая лучшая игра")
    bg = (255, 255, 255)
    
    hero = Hero(screen)
    bullets=[]
    
    clock = pygame.time.Clock()
    flag = True

    acceleration = 0.2
    deceleration = 0.1
    max_speed = 5
    speed_x = 0
    speed_y = 0

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(hero.rect.centerx, hero.rect.top)
                    bullets.append(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            speed_x -= acceleration
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            speed_x += acceleration
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            speed_y -= acceleration
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            speed_y += acceleration
        
        # Применяем замедление при отпускании клавиш
        if not keys[pygame.K_a] and not keys[pygame.K_LEFT]:
            if speed_x < 0:
                speed_x += deceleration
        if not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
            if speed_x > 0:
                speed_x -= deceleration
        if not keys[pygame.K_w] and not keys[pygame.K_UP]:
            if speed_y < 0:
                speed_y += deceleration
        if not keys[pygame.K_s] and not keys[pygame.K_DOWN]:
            if speed_y > 0:
                speed_y -= deceleration
        
        # Ограничиваем скорость
        speed_x = max(-max_speed, min(max_speed, speed_x))
        speed_y = max(-max_speed, min(max_speed, speed_y))

        hero.rect.x += speed_x
        hero.rect.y += speed_y
        # Обновляем позицию пуль и удаляем пули, которые вышли за пределы экрана
        for bullet in bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
        
        # Проверяем границы экрана
        if hero.rect.left < 0:
            hero.rect.left = 0
        if hero.rect.right > screen.get_width():
            hero.rect.right = screen.get_width()
        if hero.rect.top < 0:
            hero.rect.top = 0
        if hero.rect.bottom > screen.get_height():
            hero.rect.bottom = screen.get_height()
            
        pygame.display.flip()
        screen.fill(bg)
        hero.output_hero()
        
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)

        clock.tick(60)

start_game()