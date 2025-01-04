import random
import numpy as np


# from tensorflow import keras
import tensorflow as tf
import tensorflow.python.keras.backend as K
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Input, Dense, Dropout, LSTM, Embedding, RepeatVector
from tensorflow.python.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.utils import to_categorical

from sklearn.model_selection import train_test_split

from downloader import download_genome
from organism import organisms

def split_fragment(seq, fragment_len):
    if fragment_len <= 0:
        raise ValueError("Fragement length must be greater than 0.")
    start_index = random.randint(0, len(seq))

    return seq[start_index:start_index+fragment_len]

def seqs_dictionary_maker(number_genomes):
    seqs_dict = {}
    fragment_dict = {}
    indexes = np.random.randint(len(organisms), size=number_genomes)
    for index in indexes:
        seqs_dict[index] = str(download_genome(organisms[index]))
    
    print('indexes of organisations:', indexes)
    print('len(seqs_dict), should be equal to N:', len(seqs_dict))

    

if __name__ == "__main__":
    #@title Download N genomes and save them into array before making its k-mers signatures.
    N = 10
   
