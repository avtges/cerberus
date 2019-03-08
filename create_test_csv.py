import os
import csv
from pprint import pprint

image_path = './images/faces'

def deepfake_find(image_path):
    return [os.path.join(path, file)
        for (path, dir, files) in os.walk(image_path)
        for file in sorted(files)]

deepfake_list=[]
deepfake_list = deepfake_find(image_path)

pprint(deepfake_list)

#Assuming res is a flat list
with open('csv_files/test.csv', 'w') as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in deepfake_list:
        writer.writerow([val])