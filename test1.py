from PIL import Image
import os
import numpy as np
import scipy.misc as spm

def resizeImage(imageFilePath):
    pass

# root = "/Users/Niket/PycharmProject/AiProject/stage1_train"
root = "/Users/Niket/PycharmProject/AiProject/stage1_train/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e/masks"

for dirpath, dirs, files in os.walk(root):
    print("dirpath: ", dirpath, "\ndirs: ",  dirs, "\nfiles: ", files, "\n")
    new_image_array = np.zeros((320, 256), dtype = np.uint8)
    # count = 0
    for filename in files:
        imageFilePath = os.path.join(dirpath, filename)
        image = Image.open(imageFilePath)
        image_pixels = image.load()
        width, height = image.size
        print("Opening mask ", filename)
        for i in range(0, width):
            for j in range(0, height):
                new_image_array[i, j] += image_pixels[i, j]

    for j in range(0, height):
        for i in range(0, width):
            print(new_image_array[i, j], end = "\t")
        print("\n")

    new_image_array_t = np.matrix.transpose(new_image_array)
    new_image = spm.toimage(new_image_array_t)
    new_image.save("union.png")

