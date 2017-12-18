#image will be saved to current folder
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# random letter:
def rndChar():
    return chr(random.randint(65, 90))

# random color1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# random color 2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# create Font object:
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# create Draw object:
draw = ImageDraw.Draw(image)
# filling in every pixel:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# output the image:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# Blur the image:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
