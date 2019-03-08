import cv2
import numpy as np
from PIL import Image
import os

image_path = './deepfake/[insert directory here]/frames/'

face_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_eye.xml')

def save_faces(cascade, imgname):
    img = cv2.imread(os.path.join(image_path, imgname))
    for i, face in enumerate(cascade.detectMultiScale(img)):
        x, y, w, h = face
        sub_face = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join("./deepfake/[insert directory here]/frames/faces", "{}".format(imgname, i)), sub_face)

if __name__ == '__main__':
    face_cascade = './opencv/data/haarcascades/haarcascade_frontalface_alt.xml'
    cascade = cv2.CascadeClassifier(face_cascade)
    # Iterate through files
    for f in [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]:
        save_faces(cascade, f)
