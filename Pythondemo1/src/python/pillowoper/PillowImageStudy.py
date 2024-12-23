from PIL import Image, ImageFile, ImageFilter


def image_size(img_src:  ImageFile.ImageFile):
    w, h = img_src.size
    print("当前图片的宽：%s，高：%s" % (w, h))


def image_lessen(img_src:  ImageFile.ImageFile):
    w, h = img_src.size
    img_src.thumbnail((w // 2, h // 2))
    img_src.save("lessen.jpg", "jpeg")


def images_blur(img_src:  ImageFile.ImageFile):
    blur_image = img_src.filter(ImageFilter.BLUR)
    blur_image.save("blur.jpg","jpeg")


if __name__ == "__main__":
    image_open = Image.open("jianba.jfif")
    # image_lessen(image_open)
    # images_blur(image_open)
