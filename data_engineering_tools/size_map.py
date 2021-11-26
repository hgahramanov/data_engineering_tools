import os
import sys
from utils.metrics import ap_per_class
import numpy as np

def get_output(path):
    for txt in os.listdir(os.path.join(path, 'labels')):
        if txt.endswith('txt') == False:
            continue
        with open(os.path.join(path,'labels', txt), 'r') as f:
            lines = f.readlines()
    return lines



def xywh_2_x1y1x2y2(lst):
    lst[0] = lst[0] - (lst[2]/2)
    lst[1] = lst[1] - (lst[3]/2)
    lst[2] = lst[2] + lst[0]
    lst[3] = lst[3] + lst[1]
    return lst


def compute_iou(truth, pred):
    truth = xywh_2_x1y1x2y2(truth)
    pred = xywh_2_x1y1x2y2(pred)
    x1, y1, x2, y2 = truth
    x3, y3, x4, y4 = pred
    x_inter1 = max(x1, x3)
    y_inter1 = max(y1, y3)
    x_inter2 = min(x2, x4)
    y_inter2 = min(y2, y4)
    width_inter = abs(x_inter2 - x_inter1)
    height_inter = abs(y_inter2 - y_inter1)
    area_inter = width_inter * height_inter
    width_box1 = abs(x2 - x1)
    height_box1 = abs(y2 - y1)
    width_box2 = abs(x4 - x3)
    height_box2 = abs(y4 - y3)
    area_box1 = width_box1 * height_box1
    area_box2 = width_box2 * height_box2
    area_union = area_box1 + area_box2 - area_inter
    iou = area_inter / area_union
    return iou

def average(path):
    areas = 0
    nobjects = 0
    for txt in os.listdir(os.path.join(path, 'labels')):
        if txt.endswith('txt') == False:
            continue
        with open(os.path.join(path,'labels', txt), 'r') as f:
            lines = f.readlines()
            nobjects+=len(lines)
        for line in lines:
            line = line.strip('\n').split(' ')
            print(line)
            image = Image.open(os.path.join(path, 'images', txt[:-4] + '.jpg'))
            image_width, image_height = image.size
            print('width: ', image_width, ' height: ', image_height)
            areas += (float(line[3]) * float(line[4]))
    return areas/nobjects


def divide(path):
    average = average(path)
    small_ob = []
    big_ob = []
    for txt in os.listdir(os.path.join(path, 'labels')):
        if txt.endswith('txt') == False:
            continue
        with open(os.path.join(path,'labels', txt), 'r') as f:
            lines = f.readlines()
        temp_small = []
        temp_big = []
        for line in lines:
            line = line.strip('\n').split(' ')
            if float(line[3]) * float(line[4])<=average:
                temp_small.append(line)
            else:
                temp_big.append(line)
        small_ob.append(temp_small)
        big_ob.append(temp_big)
    return small_ob, big_ob

def labels(target_path, pred_path):
    small_tar, big_tar = divide(target_path)
    small_pred, big_pred = divide(pred_path)
    for i in range(len(small_pred)):
        for j in range(len(small_tar)):
            ious = compute_iou()



    









   	
