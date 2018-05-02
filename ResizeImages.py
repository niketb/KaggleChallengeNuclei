import os
from PIL import Image

#Function to resize all images to size 256*256
def resizeImage(imageFilePath,filename,resizedImagePath):
    img=Image.open(imageFilePath)
    new_image=img.resize((256,256))

    filename=filename+"-resized.png"

    resizedImagePathNew=resizedImagePath+filename

    new_image.save(resizedImagePathNew)



def main():

    #Root path to search for "Images" folder in all image folders
    root='/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train'

    #Searching image and mask to resize in images and masks folder respectively
    for dirpath, dirs, files in os.walk(root):

        if "images" in dirpath:

            for filename in files:

                #Path of image file to resize
                imageFilePath=os.path.join(dirpath, filename)

                #Extracting only name and not extention from filename
                onlyNameImage = filename.split(".")

                #Passing only image name wihout extension, imageFilePath and resizedImagePath to resize the image
                resizedImagePath = "/Users/anujatike/Documents/sem4/CS256/project/Data/resizedImages/"
                resizeImage(imageFilePath,onlyNameImage[0],resizedImagePath)

        if "masks" in dirpath:
            for filename in files:

                #Path of mask file to resize
                maskFilePath=os.path.join(dirpath, filename)

                #Extracting only name and not extention from filename
                onlyNameMask = filename.split(".")

                #Passing only mask name wihout extension,maskFilePath and resizedMaskPath to resize the mask
                resizedMaskPath = "/Users/anujatike/Documents/sem4/CS256/project/Data/resizedMasks/"
                resizeImage(maskFilePath,onlyNameMask[0],resizedMaskPath)



if __name__=="__main__":
    main()