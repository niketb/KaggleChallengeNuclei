import os
from PIL import Image


#Function to resize all images to size 256*256
def resizeImage(imageFilePath,filename):
    img=Image.open(imageFilePath)
    new_image=img.resize((256,256))

    filename=filename+"-resized.png"

    resizedImagePath="/Users/anujatike/Documents/sem4/CS256/project/Data/resizedImages/"+filename

    new_image.save(resizedImagePath)





#Root path to search for "Images" folder in all image folders
root='/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train'

#Searching image to resize in Images folder
for dirpath, dirs, files in os.walk(root):

    if "images" in dirpath:

        for filename in files:

            #Path of image file to resize
            imageFilePath=os.path.join(dirpath, filename)

            #Extracting only name and not extention from filename
            onlyName = filename.split(".")

            #Passing only image name wihout extension and imageFilePath to resize the image
            resizeImage(imageFilePath,onlyName[0])


