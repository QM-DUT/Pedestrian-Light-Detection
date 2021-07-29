from glob import glob
import os
import numpy as np
IMG_W, IMG_H = 400, 300



# image_lists=sorted(glob("/home/invisible/Desktop/fp_images/*.jpg"))
# print(image_lists)
#
#
# for i in range(0,len(image_lists),20):
#
#     filename=image_lists[i].split('/')[-1].split('.')[-2]
#     label_name=filename+".txt"
#
#     cmd="cp "+image_lists[i]+" /home/invisible/Hubs/datasets/cross-safe-with-background-images/images/train/"
#     os.system(cmd)
#
#     f=open("/home/invisible/Hubs/datasets/cross-safe-with-background-images/labels/train/"+label_name,'w')
#     f.close()


image_lists=sorted(glob("/home/invisible/Hubs/datasets/cross-safe-with-background-images/images/train/*.jpg"))
print(image_lists)


for i in range(0,len(image_lists)):

    filename=image_lists[i].split('/')[-1].split('.')[-2]
    label_name=filename+".txt"

    f=open("/home/invisible/Hubs/datasets/cross-safe-with-background-images/labels/train/"+label_name,'w')
    f.close()