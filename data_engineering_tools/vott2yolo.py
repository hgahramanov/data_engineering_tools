import PIL
import os
import json


def convert_box(size, box):
    # Convert VisDrone box to YOLO xywh box
    dw = 1. / size[0]
    dh = 1. / size[1]
    return (box[0] + box[2] / 2) * dw, (box[1] + box[3] / 2) * dh, box[2] * dw, box[3] * dh



def convert_dataset(vottpath, outpath, title):
    incr=0
    converted=[]
    os.system('mkdir ' + os.path.join(outpath, 'images'))
    os.system('mkdir ' + os.path.join(outpath, 'labels'))
    for doc in os.listdir(vottpath):

        if doc.endswith('.json') == False:
            print('File is not in JSON format. Skipped.')
            continue

        with open(os.path.join(vottpath, doc)) as f:
            data=json.load(f)

        
        size = []
        size.append(int(data['asset']['size']['width']))
        size.append(int(data['asset']['size']['height']))

        impath = data['asset']['path'][5:] #we start from 5th char because before that is "file:" which we don't need here
        os.system('cp ' + impath + ' ' + os.path.join(os.path.join(outpath, 'images'), title + str(incr) + '.jpg'))
        os.system('touch ' + os.path.join(os.path.join(outpath, 'labels'), title + str(incr) + '.txt'))
        converted.append(impath)

        for i in range(len(data['regions'])):
            box = []
            box.append(int(data['regions'][i]['boundingBox']['left']))
            box.append(int(data['regions'][i]['boundingBox']['top']))
            box.append(int(data['regions'][i]['boundingBox']['width']))
            box.append(int(data['regions'][i]['boundingBox']['height']))
            if data['regions'][i]['tags'][0] == 'people':
                label = '0'
            elif data['regions'][i]['tags'][0] == 'car':
                label = '1'
            else:
                continue
            output = convert_box(size, box)
            print(output)
            with open(os.path.join(os.path.join(outpath, 'labels'), title + str(incr) + '.txt'), 'a') as f:
                f.writelines(label + ' ' + str(output[0]) + ' ' + str(output[1]) + ' ' + str(output[2]) + ' ' + str(output[3]) + '\n')
        incr+=1

convert_dataset('/home/huseyn/synapline/custom_data/test8_data/labels', '/home/huseyn/synapline/custom_data/test8_yolo', 'synapline080')

