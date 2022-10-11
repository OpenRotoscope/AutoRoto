import os
import sys
import shutil

filetypeExport = sys.argv[1]

def exportImages():
    folder = 'D:/Rotoscope/imp/AutoRotoNew/Results'
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename): continue
        oldbase, file_extension = os.path.splitext(filename)
        newname = infilename.replace(file_extension, '.'+filetypeExport)
        output = os.rename(infilename, newname)

    shutil.make_archive("output_filename", 'zip', folder)
print(exportImages())
sys.stdout.flush()