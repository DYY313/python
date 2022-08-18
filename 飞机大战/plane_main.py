import pygame

from sprite import *


class PlayGame:
    """飞机大战主程序"""

    def __init__(self):
        print("initiating")

        # 创建游戏窗口
        # 游戏屏幕大小为 480*700
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建精灵和精灵组
        self.__create_sprites()
        # 设置定时器事件——敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件——子弹 0.5s
        pygame.time.set_timer(BULLET_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵
        bg1 = Background()
        bg2 = Background(True)

        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("start")
        # 游戏循环
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME)

            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵组
            self.__updare_sprite()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        # 捕获用户的事件并监听
        for event in pygame.event.get():
            # 判断是否是退出事件
            if event.type == pygame.QUIT:
                PlayGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == BULLET_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlayGame.__game_over()

    def __updare_sprite(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("game over")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建对象
    game = PlayGame()
    # 启动游戏
    game.start_game()
