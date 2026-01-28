"""
    图像处理
        三原色：红黄蓝（美术）、红绿蓝（色光）

    图像处理库
        pip install pillow
"""

from PIL import Image
def image_show():
    """
        查看图片
    """
    image = Image.open('../20210803202628.png')

    print(f'image.format: {image.format}')#image.format: PNG
    print(f'image.size: {image.size}')#image.size: (1558, 1018)
    print(f'image.mode: {image.mode}')#image.mode: RGB
    image.show()

def image_crop():
    """裁剪"""

    image = Image.open('../20210803202628.png')
    image.crop((80, 20, 310, 360)).show()

def image_thumbnail():
    """缩略图"""
    image = Image.open('../20210803202628.png')
    image.thumbnail((100, 100))
    image.show()

    pass

from PIL import ImageFilter
def image_filter():
    """滤镜"""
    image = Image.open('../20210803202628.png')
    image.filter(ImageFilter.GaussianBlur(1)).show()
    image.filter(ImageFilter.CONTOUR).show()


import random
from PIL import Image,ImageDraw,ImageFont
def random_color():
    """
        随机生成颜色
    """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

def image_draw():
    """
        绘制图片
    """
    height = 1080
    width = 1920
    image = Image.new(mode='RGB',size=(width, height),color=(255, 255, 255))# 创建图片
    draw = ImageDraw.Draw(image)# 创建画笔
    font = ImageFont.truetype('resources/simhei.ttf', size=40)# 创建字体

    draw.text(xy=(10, 10), text='Hello World', fill=random_color(), font=font)# 绘制文本
    draw.line(xy=(0, 0, width, height), fill=random_color(), width=5)
    draw.line(xy=(0, height, width, 0), fill=random_color(), width=5)

    xy = width // 2 - 60, height // 2 - 60,  width // 2 + 60, height // 2 + 60# 绘制矩形
    draw.rectangle(xy=xy, fill=random_color(), outline=random_color(), width=5)

    for i in range(4):
        left,top,right,bottom = width // 2 - 60 + i * 120, height // 2 - 60, width // 2 + 60 + i * 120, height // 2 + 60
        draw.ellipse(xy=(left, top, right, bottom), fill=random_color(), outline=random_color(), width=5)

    image.show()
    image.save('draw.png')


def main():
    # image_show()
    # image_crop()
    # image_thumbnail()
    # image_filter()
    image_draw()

    pass

if __name__ == '__main__':
    main()