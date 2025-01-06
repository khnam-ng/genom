# from tensorflow import keras
import tensorflow as tf
import tensorflow.python.keras.backend as K
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Input, Dense, Dropout, LSTM, Embedding, RepeatVector
from tensorflow.python.keras.callbacks import ModelCheckpoint