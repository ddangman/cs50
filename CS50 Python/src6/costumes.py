# Opens and saves binary files

import sys # access CMD line arguments

from PIL import Image

images = []

# argv[0] is name of program.py
for arg in sys.argv[1:]: # slice out argv[0]
    image = Image.open(arg)
    images.append(image)

# name of file to create, save_all frames passed in, images to append, milliseconds, 0 loops forever or finite>0 
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
# python costumes.py costume1.gif costume2.gif