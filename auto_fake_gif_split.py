import os
import PIL
from PIL import Image
import sys


targetDir = "./" + sys.argv[2] + "/";
gatherDir = "./" + sys.argv[1] + "/";
print ('Using ' + gatherDir + 'to create ' + targetDir + '. Please wait...')


def iter_frames(im):
    try:
        i = 0
        while 1:
            im.seek(i)
            im.frame = im.copy()
            if i == 0:
                palette = im.frame.getpalette()
            else:
                im.frame.putpalette(palette)
            yield im.frame
            i += 1
    except EOFError:
        pass

def gif_to_frames(folder, im, stack):
    directory = os.path.dirname(targetDir+ folder + "/" + str(stack) + "/")
    exists = os.path.exists(directory)
    if not exists:
        os.makedirs(directory)
        for i, frame in enumerate(iter_frames(im)):
            frame.save(targetDir + folder + "/" + str(stack) + "/fake" + str(i) + ".jpeg", **frame.info)


# Here is the actual logic #
folders = os.listdir(gatherDir)
for folder in folders:
    pathToDF = gatherDir + folder + "/deepfake/"
    files = os.listdir(pathToDF)
    fileCount = len(files)
    if fileCount == 1:
        fileName = files[0]
        im = Image.open(pathToDF + fileName)
        gif_to_frames(folder, im, 0)
    else:
        stack = 0
        for image in files:
            im = Image.open(pathToDF + image)
            gif_to_frames(folder, im, stack)
            stack += 1
