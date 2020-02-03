# coding=utf-8
import pygame

if __name__ == "__main__":
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)
    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./images/background.png").convert()
    # 3. 把背景图片放到窗口中显示
    screen.blit(background, (0, 0))
    pygame.display.update()
    while True:  # 这里的意思是：循环运行整个文件的代码，直到点击关闭按钮，内部应该是设定了延时防止卡死
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

# import pygame
#
# pygame.init()
#
# # 创建游戏窗口  480*700
# screen = pygame.display.set_mode((480, 700))
#
# # 绘制背景图像
# # 1.加载图片对象
# background_image = pygame.image.load("./images/background.png")
# # 2.blit绘制图像
# screen.blit(background_image, (0, 0))
# # 3.update更新图像
# pygame.display.update()
#
# while True:
#     pass
#
# pygame.quit()
