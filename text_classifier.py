#This is used for classifying predicted text.

import csv
import linecache
import numpy as np
from sklearn import metrics
import tensorflow as tf
from tensorflow.models.rnn import rnn, rnn_cell
import skflow

class text_classifier:
    EMBEDDING_SIZE = 50
    n_words = 1
    MAX_DOCUMENT_LENGTH = 10

    ### Training data
    @classmethod
    def load_dataset(self,filename):
        target = []
        data = []
        reader = csv.reader(open(filename), delimiter=',')
        for line in reader:
            target.append(int(line[0]))
            data.append(line[2])
        return data, np.array(target, np.float32)

    @classmethod
    def average_model(self,X, y):
        word_vectors = skflow.ops.categorical_variable(X, n_classes=self.n_words,
                            embedding_size=self.EMBEDDING_SIZE, name='words')
        features = tf.reduce_max(word_vectors, reduction_indices=1)
        return skflow.models.logistic_regression(features, y)
    @classmethod
    def rnn_model(self,X, y):
        word_vectors = skflow.ops.categorical_variable(X, n_classes=self.n_words,
                            embedding_size=self.EMBEDDING_SIZE, name='words')
        word_list = [tf.squeeze(w, [1]) for w in tf.split(1, self.MAX_DOCUMENT_LENGTH, word_vectors)]
        cell = rnn_cell.GRUCell(self.EMBEDDING_SIZE)
        _, encoding = rnn.rnn(cell, word_list, dtype=tf.float32)
        return skflow.models.logistic_regression(encoding[-1], y)

    @classmethod
    def exec_tensor(self):

        # X_train and X_test are strings that are indicated at load_dataset.

        X_train, y_train = self.load_dataset('openstack_csv/train.csv')
        X_test, y_test = self.load_dataset('openstack_csv/test1.csv')
        ### Process vocabulary

        # From here, strings are changed to int array
        vocab_processor = skflow.preprocessing.VocabularyProcessor(self.MAX_DOCUMENT_LENGTH)
        X_train = np.array(list(vocab_processor.fit_transform(X_train)))
        X_test = np.array(list(vocab_processor.transform(X_test)))

        self.n_words = len(vocab_processor.vocabulary_)
        print('Total words: %d' % self.n_words)

        ### Models
        classifier = skflow.TensorFlowEstimator(model_fn=self.rnn_model, n_classes=15,
                                                steps=1000, optimizer='Adam', learning_rate=0.01, continue_training=True)

        #while True:
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

        return target_line
        # csv is used to tran
        # At this point, contents of csv files are read.
