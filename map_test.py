import json

from PIL import ImageDraw, ImageFont


def make_rect(points):
    rect = (points['x'], points['y'], points['x'] + points['width'], points['y'] + points['height'])
    return rect


coords = json.load(open("map.json", "r"))
new_c = coords.copy()

img = ImageDraw.Image.open('map.png')
draw = ImageDraw.Draw(img)

node = 0
for x in new_c:
    draw.rectangle(make_rect(x), outline=(255, 0, 0), width=3)
    draw.text(make_rect(x), "{},{}".format(node, x), font=ImageFont.truetype(font='arial'), stroke_width=1,
              stroke_fill=(0, 0, 0))
    node += 1

img.show()
