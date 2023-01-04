import random
import time
import pygame
from pygame.constants import *

# player的方法
class hero(object):
    # 初始化属性
    def __init__(self, screen):
        self.player = pygame.image.load("./image/dingzhen.jpg")

        # player的坐标
        self.x = 480 / 2 - 60
        self.y = 500

        # palyer的速度
        self.speed = 2

        self.screen = screen

        # 装子弹的类
        self.bullet = []

    def key_control(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            # 空格键射击
            bullet = Bullet(self.screen, self.x, self.y)
            #装填到列表
            self.bullet.append(bullet)

    def dispaly(self):
        # 将palyer贴到窗口
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所以子弹
        for bullet in self.bullet:
            bullet.auto_move()
            bullet.display()

# 敌人
class enemy(object):
    # 初始化属性
    def __init__(self, screen):
        self.player = pygame.image.load("./image/yangrong.png")

        # player的坐标
        self.x = 0
        self.y = 0

        # palyer的速度
        self.speed = 2

        self.screen = screen

        # 装子弹的类
        self.bullets = []

        # 自动移动的方向
        self.direction = 'right'


    def dispaly(self):
        # 将palyer贴到窗口
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所以子弹
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed

        if self.x > 390:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


# 敌方子弹
class EnemyBullet(object):
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

class Bullet(object):
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
