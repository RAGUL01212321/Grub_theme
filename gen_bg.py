import os
from PIL import Image

def create_bg():
    os.makedirs('menu_bg', exist_ok=True)
    # Create a 16x16 image with 50% transparent black
    img = Image.new('RGBA', (16, 16), color=(0, 0, 0, 150))
    
    suffixes = ['c', 'n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']
    for s in suffixes:
        path = f'menu_bg/bg_{s}.png'
        img.save(path)
        print(f"Saved {path}")

if __name__ == '__main__':
    create_bg()
