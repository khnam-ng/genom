import random 
import numpy as np

from downloader import download_genome
from organism import organisms
from kmers import encode_nucl, stream_kmers

def trim_sequence(seq, fragment_len):
    if fragment_len <= 0:
        raise ValueError("Fragement length must be greater than 0.")
    start_index = random.randint(0, len(seq))

    return seq[start_index:start_index+fragment_len]

def split_sequence(seq, subseq_len, randomize=False):
    if subseq_len <= 0:
        raise ValueError("Subsequence length must be greater than 0.")

    if randomize:
        # Generate a list of random starting indices
        indices = sorted(random.sample(range(len(seq)),\
                            len(seq) // subseq_len))
        subseqs = [seq[i:i + subseq_len] \
              for i in indices if i + subseq_len <= len(seq)]
    else:
        # Use regular slicing without randomization
        subseqs = [
            seq[i:i + subseq_len] \
            for i in range(0, len(seq), subseq_len)]

    return subseqs

def seqs_dictionary_maker(number_genomes, fragment_len, multi_fragments = False):
    seqs_dict = {}
    kmers_dict = {}
    indexes = np.random.randint(len(organisms), size=number_genomes)
    for index in indexes:
        seqs_dict[index] = str(download_genome(organisms[index]))
    
    print('indexes of organisations:', indexes)
    print('len(seqs_dict), should be equal to N:', len(seqs_dict))

    if multi_fragments == True:
        fragment_dict = {}
        for k, v in seqs_dict.items():
            fragment_dict[k] = split_fragment(v, fragment_len=fragment_len)
        for key, value in fragment_dict.items():
            kmers_dict[key] = []
            for seq in value:
                kmers_dict[key].extend(stream_kmers(seq, k))
            
    else:  
        for key, value in seqs_dict.items():
            kmers_dict[key] = []
            kmers_dict[key].extend(stream_kmers(trim_sequence(v, fragment_len=fragment_len), k))

    # print(f'length of frag_dict: {len(fragment_dict)}')
    del seqs_dict

    return kmers_dict