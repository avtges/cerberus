import tensorflow as tf, sys

image_path = './deepfakes/real_faces/download9.jpeg'

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

#Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_Data as input to the graph and get first predictions
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    for node_id in top_k:
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (image_path, score))
