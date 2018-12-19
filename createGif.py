# Gif-generating code from: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python

import imageio
import os
import sys
import re

# Type this in the terminal to run: python createGif.py
# Will create a gif for each folder of .pngs in the folder /generatedImages

##############
# Source: https://stackoverflow.com/a/5967539
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
##############

curDir = os.path.curdir
imgFolder = "generatedImages"
imgPath = os.path.join(curDir, imgFolder)
dirs = os.listdir(imgFolder)
dirs.remove(".ipynb_checkpoints")

for dir_ in dirs:
    # Loop through each directory (which is a separate run) and create a gif of all .pngs from that directory
    dir_with_pics = os.path.join(imgPath, dir_)
    pictures = os.listdir(dir_with_pics)
    savePath = os.path.join(curDir, "gifs", dir_+".gif")
    
    # Pre-processing step. Sometimes a ".ipyn_checkpoint appears and we also want the files sorted
    is_not_png = lambda x: ".png" in x
    pictures = list(filter(is_not_png, pictures))
    pictures.sort(key=natural_keys)
    
    images = []
    for pic in pictures:
        images.append(imageio.imread(os.path.join(dir_with_pics, pic)))
    imageio.mimsave(savePath, images)