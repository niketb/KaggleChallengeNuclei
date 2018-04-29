import os
from PIL import Image



def resizeImage(imageFilePath):
    pass


#Root path to search for "Images" folder in all image folders

root='/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train'

#Searching image to resize in Images folder
for dirpath, dirs, files in os.walk(root):

    if "images" in dirpath:

        for filename in files:

            imageFilePath=os.path.join(dirpath, filename)
            resizeImage(imageFilePath)
            print(imageFilePath)


