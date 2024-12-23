import random

from PIL import Image, ImageFont,ImageDraw


def random_char():
    return chr(random.randint(65, 90))


def random_back_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

def random_font_color():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def create_font():
    return ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 30)


if __name__ == '__main__':
    # print(random_char())
    height = 50
    width = 50 * 4
    image_new = Image.new("RGB", (width, height), (255, 255, 255))
    font_new = create_font()
    image_draw = ImageDraw.Draw(image_new)
    #填充背景
    for i in range(width):
        for j in range(height):
            image_draw.point((i,j),fill=random_back_color())

    #填充文本
    for item in range(4):
        image_draw.text((50*item+10,8),random_char(),font=font_new,fill=random_font_color())

    #保存
    image_new.save("verification.jpg","jpeg")

