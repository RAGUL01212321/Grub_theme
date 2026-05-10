import os
from PIL import Image

def create_bg():
    os.makedirs('menu_bg', exist_ok=True)
    # Create a 1x1 image with 50% transparent black
    img = Image.new('RGBA', (1, 1), color=(0, 0, 0, 128))
    img.save('menu_bg/bg_c.png')

if __name__ == '__main__':
    create_bg()
