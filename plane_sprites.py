import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # 屏幕大小
FRAME_PER_SEC = 60  # 刷新的帧率
CREATE_ENEMY_EVENT = pygame.USEREVENT  # 创建敌机的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1  # 英雄发射子弹事件


class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏基类'''

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    '''游戏背景类'''

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):
        # 1.调用父类方法实现
        super().update()
        # 2.判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    ''''敌机类'''

    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 设置敌机的随机速度
        self.speed = random.randint(1, 3)
        # 设置敌机的随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 敌机飞出屏幕后，需要从敌机组中删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()  # kill方法自动调用析构函数

    def __del__(self):
        pass


class Hero(GameSprite):
    '''英雄类'''

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 英雄的初始位置设置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹类对象
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平上移动
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 创建子弹类，一连发三个
        for i in (0, 1, 2):
            bullet = Bullet()
            # 设置子弹位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(GameSprite):
    '''子弹类'''

    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", speed=-2)

    def update(self):
        # 调用父类方法，子弹沿垂直方向飞行
        super().update()
        # 判断子弹飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")
