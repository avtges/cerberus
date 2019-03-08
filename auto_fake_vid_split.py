import cv2
print(cv2.__version__)
import os
import numpy as np
from pathlib import Path
import rm_ds_store
print('Removing .DS_Store files, please wait...')

gatherDir = './videos/'
targetDir = './deepfake_videos/'

my_dir = Path(targetDir)
if my_dir.is_dir():
    print('Remove the deepfake_videos folder!')
    pass

else:
    def split_Vid(path, video):
        vidcap = cv2.VideoCapture(path)
        success,image = vidcap.read()
        count = 0
        success = True
        while success:
          cv2.imwrite('./deepfake_videos/' + folder + "/frame/" + "frame%d.jpg" % count, image)     # save frame as JPEG file
          success,image = vidcap.read()
          count += 1

    # Here is the actual logic #
    folders = os.listdir(gatherDir)
    for folder in folders:
        pathToDF = gatherDir + folder
        files = os.listdir(pathToDF)
        fileCount = len(files)
        # Read the video file
        os.makedirs(targetDir + folder + "/frame/")
        video = files[0]
        split_Vid(pathToDF + '/' + video, video)