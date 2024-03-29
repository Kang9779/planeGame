import pygame
from plane_sprites import *


class PlaneGame(object):
    '''飞机大战主游戏'''

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 1.创建游戏主窗口
        self.clock = pygame.time.Clock()  # 2.创建游戏的时钟
        self.__create_sprites()

        # 设置定时器事件 1秒
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000) #创建敌机
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(is_alt=True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        #创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到精灵组中
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动!")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘提供的方法获取键盘按键 可以持续按下
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0
    #碰撞检测
    def __check_collide(self):
        #子弹与敌机的碰撞检测
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # 敌机与英雄的碰撞检测
        enemys = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemys):
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束!")
        pygame.quit()
        exit()


if __name__ == "__main__":

    game = PlaneGame()
    game.start_game()
