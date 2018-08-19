import sys, pygame
from pygame.locals import *
import random  # 导入随机模块


# from...import*这样写的原因是方便我们在使用里面的变量啊，事件类型等等方便调用，就像
# 使用内建函数一样，实际上pygame.locals包括在你自己的模块作用域内使用的名字（变量），
# 还包括事件类型、键和视频模式等的名字
class Dianchi():
    top = 0
    left = 0
    def __init__(self):
        self.top = 0
        self.left = random.randint(0,800)


def next_dianchi():
    dianchi_top = 0
    dianchi_left = random.randint(0, 800)
    return dianchi_left, dianchi_top


def print_text(font, x, y, text, color=(0, 0, 0)):
    img_text = font.render(text, True, color)
    screen.blit(img_text, (x, y))


# 初始化
# pygame 实际上是个包，init是初始化里面的模块，让他们随时待命
pygame.init()
dianchi_speed = 8
# 设置文字的格式
font1 = pygame.font.SysFont('simhei', 20)

# 窗口大小
size = window_width, window_height = 800, 600  # 这里的size实际上是个元组
screen = pygame.display.set_mode(size)
# 导入图片
background_image = pygame.image.load("resources/images/background.png")
wanzai_image = pygame.image.load("resources/images/wanzai.png")
dianchi_image =  pygame.image.load("resources/images/dianchi.png")

# 更新图像，pygame通过修改其中一个图像的某些位置的像素颜色，从而达到覆盖的效果
# 设置背景
screen.blit(background_image, (0, 0))
# 设置玩仔
wanzai_left, wanzai_top = window_width // 2, window_height // 2
wanzai_width, wanzai_height = wanzai_image.get_size()  # 得到玩仔的大小
screen.blit(wanzai_image, (wanzai_left - wanzai_width // 2, 400))
mouse_x, mouse_y = 0, 0
# 设置电池
dianchi_width, dianchi_height = dianchi_image.get_size()  # 得到电池的大小
dianchi_left, dianchi_top = next_dianchi()
screen.blit(dianchi_image, (dianchi_left, dianchi_top))

pygame.display.update()

# screen.blit(wanzai_image,(400,400))
# screen.blit(dianchi_image,(200,200))
# 刷新窗体
pygame.display.update()
# 标题
pygame.display.set_caption("欢迎来到编玩边学")
# 事件监听
gameover = False
lives = 50
score = 0

##
dianchi_list = []
count = 0
# dc = Dianchi()
# dianchi_list.append(dc)
while True:
    flag =0
    for event in pygame.event.get():  # 使用for遍历到所有捕捉的的事件，
        # get方法返回到的时间列表中的每一个元素都是一个事件
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            
    wanzai_left, wanzai_top = mouse_x - wanzai_width // 2, 400

    count = count + 1
    if(count > 1):
        d = Dianchi()
        dianchi_list.append(d)
        count = 0

    for d in dianchi_list:
        d.top = d.top + dianchi_speed
        if(d.top > window_height):
            dianchi_list.remove(d)
            lives = lives-1
            #碰撞判定
        if d.left>wanzai_left and d.top>wanzai_top and d.left+dianchi_width < wanzai_left+wanzai_width:
            flag = 1
            dianchi_list.remove(d)
            
    if flag==1:
        score=score+1
    screen.blit(background_image, (0, 0))
    for d in dianchi_list:
        screen.blit(dianchi_image, (d.left, d.top))
        
    if lives <= 0:
        gameover=True
        sys.exit()
    #碰撞判定
    # if dianchi_left>wanzai_left and dianchi_top>wanzai_top and dianchi_left+dianchi_width < wanzai_left+wanzai_width:
    #     score = score + 1
            
    
    screen.blit(wanzai_image, (wanzai_left - wanzai_width // 2, 400))
    print_text(font1,0,0,'lives:'+str(lives))
    print_text(font1,200,0,'score:'+str(score))
    pygame.display.update()
