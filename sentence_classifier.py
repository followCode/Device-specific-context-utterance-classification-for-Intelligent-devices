from __future__ import print_function

import os
import sys

import numpy as np
import keras

from sentence_types import load_encoded_data
from sentence_types import encode_data, import_embedding, encode_phrases
from sentence_types import get_custom_test_comments

from keras.preprocessing import sequence
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Activation, Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D

from keras.preprocessing.text import Tokenizer

class Classifier:
    maxlen = 500
    encoding_name = "data/default"

    def __init__(self, model_name="models/cnn"):
        self.model_name = model_name

        # load CNN model JSON
        json_file = open(self.model_name + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)

        # load weights into new model
        self.model.load_weights(model_name + ".h5")
        print("Loaded model from disk")

        # Compile model
        self.model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

    def predict(self, inp):
        # Encode commment into vector
        word_encoding, category_encoding = import_embedding(self.encoding_name)
        inp, _, _ = encode_phrases(inp, word_encoding, True)

        inp = np.asarray(inp)

        new_inp = sequence.pad_sequences(inp, maxlen=self.maxlen)
        pred = self.model.predict_classes(new_inp, verbose=0)

        return pred

'''def test():
    while(True):
        cls = Classifier()
        sample = input("Enter the sentence: ")
        if cls.predict([sample]) == [1]:
            print("It's a question")
        elif cls.predict([sample])== [2]:
            print("It's a statement")
        elif cls.predict([sample])== [3]:
            print("It's a command")
test()'''
