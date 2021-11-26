import os
import sys
def rename(path, pattern, extension='jpg'):
    for i, f in enumerate(os.listdir(path)):
        if f.endswith(extension):
            os.system('mv '+os.path.join(path, f) + ' ' + os.path.join(path, pattern+str(i)+'.jpg'))
rename(sys.argv[1], sys.argv[2])

