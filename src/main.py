import random
import numpy as np

from tensorflow.python.keras.utils import to_categorical

from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    #@title Download N genomes and save them into array before making its k-mers signatures.
    N = 10
   
