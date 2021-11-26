import cv2 
vidcap = cv2.VideoCapture('/home/huseyn/Downloads/test8.MP4')
success,image = vidcap.read()
count=0
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line
    cv2.imwrite("test8_data/frame%d.jpg" % count, image)
    success,image = vidcap.read()
    count=count+1
    print('Read')

