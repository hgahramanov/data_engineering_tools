from PIL import Image
import os
from collections import Counter

def count(path):
    sizes = []
    for im in os.listdir(path):
        width, height = Image.open(path+im).size
        sizes.append(str(width)+"x"+str(height))
    sizes = Counter(sizes)
    print(sizes)

path = os.sys.argv[1]
count(path)

