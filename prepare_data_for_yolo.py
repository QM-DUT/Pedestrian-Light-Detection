from glob import glob
import os
import numpy as np
IMG_W, IMG_H = 400, 300
classes = {"white": 0, "red": 1}

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


for root, dirs, files in os.walk("/home/invisible/Downloads/Cross-Safe/Cross-Safe/data/new_splitted_data", topdown=False):
    for name in files:
        if name.split('.')[-1]=="JPEG":
            path=os.path.join(root,name)
            print(path)
            cmd="cp "+"\""+path+"\""+" /home/invisible/Hubs/datasets/cross-safe-single-class/images/train"
            print(cmd)
            os.system(cmd)
        elif name.split('.')[-1]=="txt":
            path_ori=os.path.join(root, name)
            path = os.path.join("/home/invisible/Hubs/datasets/cross-safe-single-class/labels/train", name)

            f_ori=open(path_ori)
            label = int(f_ori.readline())

            if label==0 or label==1:
                label=0

            box_coords = f_ori.readline().split(' ')
            box_coords = np.array([int(x) for x in box_coords])
            xywh=convert([IMG_W, IMG_H],box_coords)

            f=open(path,'w')
            content=str(label)+" "+str(xywh[0])+" "+str(xywh[1])+" "+str(xywh[2])+" "+str(xywh[3])+"\n"
            f.write(content)




