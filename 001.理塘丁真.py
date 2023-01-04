import time

import pygame
from pygame.constants import *


def main():
    # 1创建一个窗口
    screen = pygame.display.set_mode((450, 650), 0, 32)
    # 2创建一个图片，当做背景
    background = pygame.image.load("./image/background.jpg")
    player = pygame.image.load("./image/dingzhen.jpg")

    # 3将背景图片贴到窗口中
    screen.blit(background, (0, 0))
    screen.blit(player, (480 / 2 - 50, 600))
    x = 480 / 2 - 50
    y = 600


    # player速度
    speed = 2

    while True:

        # 3将背景图片贴到窗口中
        screen.blit(background, (0, 0))
        screen.blit(player, (x, y))

        # 获取事件
        # 点x退出


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # 左右空格控制
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            print("上")
            y -= speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print("下")
            y += speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print("左")
            x -= speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("右")
            x += speed
        if key_pressed[K_SPACE]:
            print("空格")

        pygame.display.update()

        time.sleep(0.01)


if __name__ == '__main__':
    main()
