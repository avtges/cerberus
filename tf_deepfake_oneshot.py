import numpy as np
import tensorflow as tf

import csv
import os
import random
import pandas
from tensorflow.python.platform import gfile

# step 1: import training data from csv, assign labels

with open('./csv_files/deepfake.csv', 'r') as f:
    deepfake_data = list(csv.reader(f, delimiter=';'))
print(deepfake_data[:3])

filenames = tf.constant(deepfake_data)
print(filenames)

labels = []
for i in range (4402):
    labels.append(random.randrange(0,4402,2))
    tf.constant((labels), dtype=tf.float64)
#print(labels)

# step 2: create a dataset returning slices of `filenames`
dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))

# step 3: parse every image in the dataset using `map`
def _parse_function(filename, label):
    image_string = tf.read_file(filename[0])
    image_decoded = tf.image.decode_png(image_string)
    image_resized = tf.image.resize_images(image_decoded, [48, 48])
    return image_resized, label

dataset = dataset.map(_parse_function)
dataset = dataset.batch(2)
print(dataset)

# step 4: create iterator and final input tensor
iterator = dataset.make_one_shot_iterator()
images, labels = iterator.get_next()

# step 5: create graph of dataset
with tf.Session() as sess:
    os.system("rm -rf ./tmp/load")
    tf.train.write_graph(sess.graph_def, "./tmp/load", "test.pb", True)

# Load graph
with gfile.FastGFile("./tmp/load/test.pb",'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# step 6: monitored training session
init = tf.global_variables_initializer()
print(init)

def run_my_model(init, session_args):
    with tf.train.MonitoredTrainingSession(**session_args) as sess:
        sess.run(init)

run_my_model(init, {})

