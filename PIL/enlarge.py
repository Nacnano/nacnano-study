import numpy as np 
from PIL import Image
import os
import png

from environment import DIRECTORY
from environment import PROGRESSIVE, INTERLACE

directory = DIRECTORY
for foldername in os.listdir(directory):
    new_directory = os.path.join(directory, foldername)
    resized_directory = "enlarged_" + new_directory
    if ".DS_Store" in resized_directory:
            continue

    if not os.path.exists(resized_directory):
        os.makedirs(resized_directory)

    for filename in os.listdir(new_directory):
        path = os.path.join(new_directory, filename)
        save_path = os.path.join(resized_directory, filename)
        if ".DS_Store" in path:
            continue
        image = Image.open(path)

        current_size = os.path.getsize(path)
        count = 1
        multiplier = 1
        while count < 10:
            multiplier *= 2
            width, height = image.size
            new_size = (int(multiplier*width), int(multiplier*height))
            resized_image = image.resize(new_size)
            resized_image.save(save_path, optimize=True, progressive=PROGRESSIVE)

            print(save_path, os.path.getsize(path), os.path.getsize(save_path))
            current_size = os.path.getsize(save_path)

            if current_size < 1000000:
                count += 1
            else:
                break
            