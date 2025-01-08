# from tensorflow import keras
import tensorflow as tf
import tensorflow.python.keras.backend as K
from tensorflow.python.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout, LSTM, Embedding, RepeatVector
from tensorflow.keras.callbacks import ModelCheckpoint

def model_creator(X_train, Y_train):
    model = Sequential()
    model.add(LSTM(X_train.shape[1], input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True))
    model.add(LSTM(X_train.shape[1]))
    # model.add(Dropout(0.2))
    # model.add(Dense(kmer_len, activation='relu'))
    # model.add(RepeatVector(X_train.shape[1]))
    model.add(Dense(Y_train.shape[1], activation='softmax'))
    model.compile(loss=['categorical_crossentropy'] , optimizer='adam', metrics=['accuracy'])
    model.summary()

    return model