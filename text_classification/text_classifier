#This is used for classifying predicted text.

import csv
import linecache
import numpy as np
from sklearn import metrics
import tensorflow as tf
from tensorflow.models.rnn import rnn, rnn_cell
import skflow


### Training data

# csv is used to tran
# At this point, contents of csv files are read.
def load_dataset(filename):
    target = []
    data = []
    reader = csv.reader(open(filename), delimiter=',')
    for line in reader:
        target.append(int(line[0]))
        data.append(line[2])
    return data, np.array(target, np.float32)

# X_train and X_test are strings that are indicated at load_dataset.
X_train, y_train = load_dataset('openstack_csv/train.csv')
X_test, y_test = load_dataset('openstack_csv/test1.csv')


### Process vocabulary

MAX_DOCUMENT_LENGTH = 10
# From here, strings are changed to int array
vocab_processor = skflow.preprocessing.VocabularyProcessor(MAX_DOCUMENT_LENGTH)
X_train = np.array(list(vocab_processor.fit_transform(X_train)))
X_test = np.array(list(vocab_processor.transform(X_test)))

n_words = len(vocab_processor.vocabulary_)
print('Total words: %d' % n_words)


### Models

EMBEDDING_SIZE = 50

def average_model(X, y):
    word_vectors = skflow.ops.categorical_variable(X, n_classes=n_words,
                        embedding_size=EMBEDDING_SIZE, name='words')
    features = tf.reduce_max(word_vectors, reduction_indices=1)
    return skflow.models.logistic_regression(features, y)

def rnn_model(X, y):
    word_vectors = skflow.ops.categorical_variable(X, n_classes=n_words,
                        embedding_size=EMBEDDING_SIZE, name='words')
    word_list = [tf.squeeze(w, [1]) for w in tf.split(1, MAX_DOCUMENT_LENGTH, word_vectors)]
    cell = rnn_cell.GRUCell(EMBEDDING_SIZE)
    _, encoding = rnn.rnn(cell, word_list, dtype=tf.float32)
    return skflow.models.logistic_regression(encoding[-1], y)

classifier = skflow.TensorFlowEstimator(model_fn=rnn_model, n_classes=15,
                                        steps=1000, optimizer='Adam', learning_rate=0.01, continue_training=True)

while True:
#    classifier.fit(X_train, y_train)
#    score = metrics.accuracy_score(classifier.predict(X_test), y_test)
#    print('Accuracy: {0:f}'.format(score))
    classifier.fit(X_train, y_train)
    score = metrics.accuracy_score(classifier.predict(X_test), y_test)
    a = classifier.predict(X_test)[0]
    print a
    print('Accuracy: {0:f}'.format(score))
    target_line = linecache.getline('openstack_csv/classes.txt', int(a))
    print(target_line)
    linecache.clearcache()
