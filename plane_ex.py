
import pygame

# ----------游戏的初始化-------------
pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 加载图像->blit绘制图像->更新显示
bgImage = pygame.image.load('./images/background.png')
screen.blit(bgImage, (0, 0))

# 绘制英雄飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (150, 300))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

#创建敌机
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
enemy_group = pygame.sprite.Group(enemy,enemy1)


# ----------游戏循环----------------
while True:
    # 屏幕刷新频率
    clock.tick(60)
    #事件监听
    for event in pygame.event.get():
        
        # 判断用户是否点击了关闭按钮
        if event.type==pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            exit()

    hero_rect.y -= 1
    # 判断飞机的Y轴位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    screen.blit(bgImage, (0, 0))
    screen.blit(hero, hero_rect)

    #精灵组调用方法
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()


