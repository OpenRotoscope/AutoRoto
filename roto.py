import cv2
import glob
import os
from bs4 import BeautifulSoup as bs
import sys
import re

filetypeExport = sys.argv[1]
filenameText = sys.argv[2]


def export():
    img_array = []
    folder = 'D:/Rotoscope/imp/AutoRotoNew/Results'
    file_list = os.listdir(folder)
    def tryint(s):
        try:
            return int(s)
        except:
            return s

    def alphanum_key(s):
        return [ tryint(c) for c in re.split('([0-9]+)', s) ]


    file_list.sort(key=alphanum_key)

    for filename in file_list:
        filename_here = os.path.join(folder,filename)
        img_frame = cv2.imread(filename_here)
        height, width, layers = img_frame.shape
        size = (width,height)
        img_array.append(img_frame)


    out = cv2.VideoWriter(filenameText + '.'+ filetypeExport,cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

print(export())
sys.stdout.flush()