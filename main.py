import pygame
import sys
from hero import Hero
from enemy import Enemy
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Space_Invaders_RPO1_Chibotar/images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

    
def start_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")
    
    background = pygame.image.load("Space_Invaders_RPO1_Chibotar/images/background.jpg")
    
    hero = Hero(screen)
    bullets=[]
    
    clock = pygame.time.Clock()
    spawn_interval = 2000  # Интервал в миллисекундах между спавном врагов
    last_spawn_time = 0
    flag = True

    acceleration = 0.2
    deceleration = 0.1
    max_speed = 5
    speed_x = 0
    speed_y = 0
    
    #ENEMY
    max_enemies = 7
    ENEMY_WIDTH = 50
    ENEMY_HEIGHT = 50
    SCREEN_WIDTH = 800
    ENEMY_SPACING = 100
    enemies = pygame.sprite.Group()

    def spawn_enemy():
        num_enemies = 5  # Заданное количество врагов
        total_width = num_enemies * (ENEMY_WIDTH + ENEMY_SPACING) - ENEMY_SPACING
        start_x = (SCREEN_WIDTH - total_width) // 2  # Центрирование врагов по горизонтали

        for i in range(num_enemies):
            x = start_x + i * (ENEMY_WIDTH + ENEMY_SPACING)
            y = random.randint(-ENEMY_HEIGHT, 0)
            enemy = Enemy(x, y)
            enemies.add(enemy)

        enemies.draw(screen)
    
    while flag:
        screen.blit(background, (0, 0))
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
        
        # Применяем замедление при отпускании клавиш
        if not keys[pygame.K_a] and not keys[pygame.K_LEFT]:
            if speed_x < 0:
                speed_x += deceleration
        if not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
            if speed_x > 0:
                speed_x -= deceleration
        
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
        
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        
        
        current_time = pygame.time.get_ticks()

        if current_time - last_spawn_time > spawn_interval:
            spawn_enemy()
            last_spawn_time = current_time

        for enemy in enemies:
            enemy.update()
            screen.blit(enemy.image, enemy.rect)

        hero.output_hero()

        
        pygame.display.flip()
        clock.tick(60)

start_game()