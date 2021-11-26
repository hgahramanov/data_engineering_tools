import os
import sys
import json

def convert(vottpath, outpath, pattern):
    os.system('mkdir '+ os.path.join(outpath, 'images'))
    cnt = 0
    for doc in os.listdir(os.path.join(vottpath, 'labels')):
        if doc.endswith('.json') == False:
            print('File is not in JSON format. Skipped.')
            continue

        with open(os.path.join(vottpath, 'labels', doc)) as f:
            data=json.load(f)
        os.system('cp '+os.path.join(vottpath, 'images', data['asset']['name'])+' '+os.path.join(outpath, 'images', pattern+str(cnt)+'.jpg'))
        output = os.path.join(outpath, 'images', pattern+str(cnt))+'.jpg ' 
        for i in range(len(data['regions'])):
            box = []
            box.append(str(data['regions'][i]['boundingBox']['left']))
            box.append(str(data['regions'][i]['boundingBox']['top']))
            box.append(str(float(data['regions'][i]['boundingBox']['width'])+float(box[0])))
            box.append(str(float(data['regions'][i]['boundingBox']['height'])+float(box[1])))
            if data['regions'][i]['tags'][0] == 'people':
                label = '0'
            elif data['regions'][i]['tags'][0] == 'car':
                label = '1'
            else:
                continue
            box.append(label)
            output += ','.join(box) + ' '

        with open(outpath + '/labels.txt', 'a') as fout:
            fout.write(output + ' \n')

        print(output)
        cnt+=1
convert(sys.argv[1], sys.argv[2], sys.argv[3])
