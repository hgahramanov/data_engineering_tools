import os
import random

def generate(inpath, outpath):
    os.system('mkdir ' + os.path.join(outpath, 'images'))
    os.system('mkdir ' + os.path.join(outpath, 'labels'))
    labels = os.listdir(os.path.join(inpath, 'labels'))
    size = len(labels)
    jpg = 'jpg'
    print(size)
    rands = []


    for i in range(100):
        idx = random.randint(0, size-1)
        if idx in rands:
            i-=1
            continue
        rands.append(idx)
        os.system('mv ' +  os.path.join(inpath, 'labels', labels[idx]) + ' ' + os.path.join(outpath, 'labels'))
        img = labels[idx][:-3] + jpg
        os.system('mv ' +  os.path.join(inpath, 'images', img) + ' ' +  os.path.join(outpath, 'images'))

generate('/home/huseyn/synapline/custom_data/yolo_custom_data', '/home/huseyn/synapline/custom_data/yolo_custom_data_val')



    

