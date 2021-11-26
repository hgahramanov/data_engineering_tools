import sys
import os

def replace(keyword, target, path):
    with open(path, "r+") as f:
        lines = [i.split(' ') for i in f.readlines()]
        f.seek(0)
        f.truncate(0)
        for i in range(len(lines)):
            if lines[i][0]==target: lines[i][0]=keyword
            lines[i]=" ".join(lines[i])
        f.writelines(lines)
        f.close()

def delete(keyword, path):
     with open(path, "r+") as f:
        lines = [i.split(' ') for i in f.readlines()]
        f.seek(0)
        f.truncate()
        newlines = []
        for i in range(len(lines)):
            if lines[i][0]==keyword: continue
            lines[i]=" ".join(lines[i])
            newlines.append(lines[i])
        f.writelines(newlines)
        f.close()

def modify(path):
    for filename in os.listdir(path):
        filename = os.path.join(path, filename)
        if filename.endswith(".txt"):
            replace('1', '2', filename)
            replace('4', '5', filename)
            replace('4', '6', filename)
            replace('4', '9', filename)
            delete('0', filename)
            delete('3', filename)
            delete('7', filename)
            delete('8', filename)
            delete('10', filename)
            delete('11', filename)
            replace('0', '1', filename)
            replace('1', '4', filename)
            print(filename, " Modified")
            
if len(sys.argv)>1: path = sys.argv[1]
else: path = os.getcwd()
modify(path)
