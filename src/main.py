import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.callbacks import History
from sklearn.model_selection import train_test_split

from seqs import seqs_dictionary_maker, data_maker
from model import model_creator

if __name__ == "__main__":
    N = 2
    fragment_len = 1000
    kmer_size = 4
    correct = 0

    X_set, Y_set = data_maker(seqs_dictionary_maker(number_genomes=N, fragment_len=fragment_len, \
                                                    kmers_size=kmer_size, multi_fragments=False))
    X_train, X_test, Y_train, Y_test = train_test_split(X_set, Y_set)

    print(f'Length of X_train: {len(X_train)} / length of X_test: {len(X_test)}')
    print(f'Length of Y_train: {len(Y_train)} / length of Y_test: {len(Y_test)}')

    history = History()
    lstm = model_creator(X_train, Y_train)
    lstm.fit(X_train, Y_train, batch_size=64, epochs=3, verbose=1, callbacks=[history])

    y_pred = lstm.predict(X_test)
    for i in range(len(y_pred)):
        if np.argmax(y_pred[i]) == np.argmax(Y_test[i]):
            correct += 1
    print(f'LSTM accuracy on test data: {round((correct/len(y_pred)), 2)}')