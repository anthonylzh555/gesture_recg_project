import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



Path = "./"
Cindy_Path = "./"
folderlist = os.listdir(Path)
folderlist.remove(".DS_Store")
plt.figure()
jj=0
for folder in folderlist:
    if jj>101:
        Img_Path = Path+folder+"/"
        imglist = os.listdir(Img_Path)
        if ".DS_Store" in imglist:
            imglist.remove(".DS_Store")

        img = Image.open(Img_Path+imglist[0])
        img2 = plt.imread(Img_Path+imglist[1])
        #print(Img_Path+imglist[jj])
        plt.subplot(1,2,1)
        plt.imshow(img)
        plt.subplot(1,2,2)
        plt.imshow(img2)
        plt.show()

        rot = input('Enter 0:No, 1:Right, 2:Left')
        for imgname in imglist:
            im = Image.open(Img_Path+imgname)
            print(Img_Path+imgname)
            if rot == "1":
                img_rotate = im.transpose(Image.ROTATE_270)
                img_rotate.save(Img_Path + imgname)
            elif rot == "2":
                img_rotate = im.transpose(Image.ROTATE_90)
                img_rotate.save(Img_Path + imgname)
            else :
                img_rotate = img

    jj=jj+1








