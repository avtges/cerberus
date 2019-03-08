import cv2
import numpy as np
from PIL import Image
import os
import sys

targetDir = "./" + sys.argv[2] + "/";
targetDir2 = "./" + sys.argv[2];
gatherDir = "./" + sys.argv[1] + "/";
print ('Now using ' + gatherDir + 'to create ' + targetDir + '. Please wait...')

# Functions used #
def save_faces(image_path, folder, image, stack):
    face_cascade = './opencv/data/haarcascades/haarcascade_frontalface_alt.xml'
    cascade = cv2.CascadeClassifier(face_cascade)

    directory = os.path.dirname(targetDir + folder + "/"  + str(stack) + "/")
    exists = os.path.exists(directory)
    if not exists:
        os.makedirs(directory)
    img = cv2.imread(image_path)
    for i, face in enumerate(cascade.detectMultiScale(img)):
        x, y, w, h = face
        sub_face = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(targetDir2,folder,str(stack),"face0" + image), sub_face)

def iterate_through_images(stack_path, folder, stack):
    images = os.listdir(stack_path)

    for image in images:
        image_path = stack_path + image
        save_faces(image_path, folder, image, stack)

# Here is where the logic begins #
if __name__ == '__main__':
    folders = os.listdir(gatherDir)
    for folder in folders:
        path = gatherDir + folder + "/"
        files = os.listdir(path)
        fileCount = len(files)
        if fileCount == 1:
            fileName = files[0]
            stack_path = path + fileName + "/"
            iterate_through_images(stack_path, folder, 0)
        else:
            for stack in files:
                stack_path = path + stack + "/"
                iterate_through_images(stack_path, folder, stack)
