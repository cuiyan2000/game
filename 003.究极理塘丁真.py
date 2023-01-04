import random
import time


import pygame
import self as self
from pygame.constants import *

# player的方法
class hero(pygame.sprite.Sprite):
    # 初始化属性
    def __init__(self, screen):
        # 类的初始化方法必须调用
        pygame.sprite.Sprite.__init__(self)

        self.player = pygame.image.load("./image/dingzhen.jpg")

        self.rect = self.image.get_rect()
        self.rect.topleft = [480 / 2 - 60, 500]

        # palyer的速度
        self.speed = 2

        self.screen = screen

        # 装子弹的类
        self.bullet = pygame.sprite.Group()

    def key_control(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.bottom += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.right += self.speed
        if key_pressed[K_SPACE]:
            # 空格键射击
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            # 装填到列表
            self.bullet.add(bullet)

    def update(self):
        self.key_control()
        self.dispaly()

    def dispaly(self):
        # 将palyer贴到窗口
        self.screen.blit(self.player, self.rect)
        # 遍历所以子弹
        self.bullet.update()
        self.bullet.draw(self.screen)

# 敌人
class enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        # 类的初始化方法必须调用
        pygame.sprite.Sprite.__init__(self)

        self.player = pygame.image.load("./image/yangrong.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

        # palyer的速度
        self.speed = 2

        self.screen = screen

        # 装子弹的类
        self.bullet = pygame.sprite.Group()

        self.direction = 'right'

    def dispaly(self):
        # 将palyer贴到窗口
        self.screen.blit(self.player, self.rect)
        # 遍历所以子弹
        self.bullet.update()
        self.bullet.draw(self.screen)

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.dispaly()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.right -= self.speed

        if self.rect.right > 390:
            self.direction = 'left'
        elif self.rect.right < 0:
            self.direction = 'right'

    def auto_fire(self):
        random_num = random.randint(1, 10)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.rect.left, self.rect.top)
            self.bullet.add(bullet)


# 敌方子弹
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.x = x + 70/2 - 17
        self.y = y + 70
        self.image = pygame.image.load("./image/zhengtianxiang.png")   # 这里的地方子弹可以换
        self.screen = screen
        self.speed = 10

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # bullet 移动
    def auto_move(self):
        self.y += self.speed




# 我方子弹

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.x = x + 50 - 17
        self.y = y - 32
        self.image = pygame.image.load("./image/zhengtianxiang.png")
        self.screen = screen
        self.speed = 10

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # bullet 移动
    def auto_move(self):
        self.y -= self.speed

# 背景音乐
class MUSIC(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./music/ltdz.mp3')
        pygame.mixer.music.set_volume(0.5)

# 开始播放
    def playmusic(self):
        pygame.mixer.music.play(-1)




def main():

    sound = MUSIC()
    sound.playmusic()


    # 1创建一个窗口
    screen = pygame.display.set_mode((450, 650), 0, 32)
    # 2创建一个图片，当做背景
    background = pygame.image.load("./image/background.jpg")

    player = hero(screen)
    enemyplayer = enemy(screen)

    while True:

        # 将背景图片贴到窗口中
        screen.blit(background, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 执行player的按键监听
        player.key_control()
        player.dispaly()
        enemyplayer.dispaly()
        # 敌人自动移动
        enemyplayer.auto_move()
        # 敌人自动开火
        enemyplayer.auto_fire()

        # 更新显示
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
