import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 帧数常量
FRAME = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 子弹事件
BULLET_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 先调用父类的初始化方法，再编写其他代码
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 继承父类
        super().__init__("./images/background.png")
        # 判断第几张图
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 继承父类
        super().update()
        # 增加功能
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 继承父类
        super().__init__("./images/enemy1.png")
        # 指定敌机速度 1-3
        self.speed = random.randint(1, 3)
        # 随机敌机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 继承父类
        super().update()
        # 销毁没用的精灵
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类
        super().__init__("./images/me1.png", 0)
        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平方向移动
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0,1,2):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置位置
            bullet.rect.y = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 加入精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

