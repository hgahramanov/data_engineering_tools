import string, os
#import os
import pdb
from PIL import Image


def find_x(bbox_left,image_width,box_xmax):
	image_width = 1.0 * int(image_width)
	absolute_x = int(bbox_left) + 0.5 * (int(box_xmax) - int(bbox_left))
	x = absolute_x / image_width
	return str(x)

	

def find_y(image_height,box_ymax,bbox_top):
	image_height = 1.0 * int(image_height)
	absolute_y = int(bbox_top) + 0.5 * (int(box_ymax) - int(bbox_top))
	y = absolute_y / image_height
	return str(y)

def find_width(box_xmax,bbox_left,image_width): 
	absolute_width = int(box_xmax) - int(bbox_left)
	image_width = 1.0 * int(image_width)
	width = absolute_width / image_width 
	return str(width)


def find_height(bbox_top,box_ymax,image_height):
	absolute_height = int(box_ymax) - int(bbox_top)
	image_height = 1.0 * int(image_height)
	height = absolute_height / image_height
	return str(height)

for f in os.listdir('/home/huseyn/synapline/yolo/yolov5/data/datasets/VisDrone/VisDrone2019-DET-val/annotations/'):
    if f != "vis.py":
            #filename = f
            #pdb.set_trace()
	    #filename_without_ext =  str(f.split(".")[:-1])
	    #fname = filename
	    #fname_out = filename_without_ext + "_out.txt"
            fname = f
            fname_out = f
            image = Image.open('/home/huseyn/synapline/yolo/yolov5/data/datasets/VisDrone/VisDrone2019-DET-val/images/'+ f[:-4]+'.jpg')
            image_width, image_height = image.size
		
           # image_width = 1360
           # image_height = 765
            content = []

            with open('/home/huseyn/synapline/yolo/yolov5/data/datasets/VisDrone/VisDrone2019-DET-val/annotations/'+ fname) as f:
                content = f.readlines()
	    # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 

	    #print(content)

            new_content = []

            for x in content:
                y = x.split(",")
		#del y[4]
		#del y[6]
  		#del y[7]
                bbox_left = y[0]
                bbox_top = y[1]
                bbox_width = y[2]
                bbox_height = y[3]
                box_xmax = str(int(y[0]) + int(y[2]))
                box_ymax = str(int(y[1]) + int(y[3]))
                place_0_value = y[5] 
                place_1_value = find_x(bbox_left,image_width,box_xmax)
                place_2_value = find_y(image_height,box_ymax,bbox_top)
                place_3_value = find_width(box_xmax,bbox_left,image_width)
                place_4_value = find_height(bbox_top,box_ymax,image_height)

                output = str(place_0_value) + " " + str(place_1_value) + " " + str(place_2_value) + " " + str(place_3_value) + " " + str(place_4_value)
                new_content.append(output)

		
            with open('/home/huseyn/synapline/yolo/yolov5/data/datasets/VisDrone/VisDrone2019-DET-val/labels/'+fname_out, 'w') as f:
                f.truncate(0)
                for item in new_content:
                    f.write("%s\n" % item)


