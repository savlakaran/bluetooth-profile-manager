# from switch_profiles import create_image
from PIL import Image, ImageDraw

imagePath = ''

def get_tray_image_icon():
    if imagePath:
        return Image.open(imagePath)
    else:
        return create_image()


def create_image():
    width=12
    height=12
    color1="red"
    color2="blue"
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image
