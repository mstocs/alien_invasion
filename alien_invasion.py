# -*- coding:utf-8 -*-
import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    #screen = pygame.display.set_mode((1200,800))
    #pygame.display.set_caption("Alien Invasion")
    #设置背景色
    #bg_color = (23,230,230)
    #引入settings模块后改写为
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #sys.exit()
        #引入game_functions模块后改写为：
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        #每次循环时都重新绘制屏幕
        #screen.fill(bg_color)
        #引入Settings后改写
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        #让最近绘制的屏幕可见
        #pygame.display.flip()
        #引入gf中的update_screen()方法后改写为：
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()