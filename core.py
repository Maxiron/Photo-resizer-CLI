from PIL import Image
from pathlib import Path


def fav_generator(in_path, icon_size):   
       icon_sizes = [(icon_size, icon_size)]
       image = Image.open(image_url)
       img_format = image.format
       for size in icon_sizes:
              new_image = image.resize(size)
              new_image.save(f"{Path(in_path).stem}_{size[0]}x{size[1]}.{img_format}")

# image_url, icon_size = 'pubg.jpg', 30

# fav_generator(image_url, icon_size)