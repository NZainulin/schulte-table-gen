from PIL import Image, ImageDraw, ImageFont
import os


font = ImageFont.truetype("VT323-Regular.ttf", 80)

def check_dir():
    if not os.path.isdir('images'):
        os.mkdir('images')

def img_gen():
    check_dir()

    for i in range(1, 101):
        im = Image.new('RGB', (95, 95), 'silver')
        d = ImageDraw.Draw(im)
        d.text((50, 72), f'{i}', fill='black', anchor='ms', font=font)
        im.save(f'images/{i}.jpg')

if __name__ == '__main__':
    img_gen()