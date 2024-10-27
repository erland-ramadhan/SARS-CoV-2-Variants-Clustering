import os
import time
import numpy as np
from itertools import product

def where_id(al, s):
    base = len(al)
    id = 0
    for i in range(len(s)):
        id += base**i * al.index(s[-1-i])
    return id

proSeq = np.load(os.getcwd() + '/filtered_protein_seq.npy')
dataSize = proSeq.shape[0]
seqLen = len(proSeq[0])

k = 3
aminoSeq = 'ACDEFGHIKLMNPQRSTVWXY'
fvLen = len(aminoSeq)**k

freqVec = np.zeros(shape=(dataSize, fvLen))
start_time = time.time()

for i in range(dataSize):
    for j in range(seqLen-k):
        id = where_id(aminoSeq, proSeq[i][j:j+k])
        freqVec[i, id] += 1

freqVec = freqVec.astype(np.uint8)
np.save(os.getcwd() + '/feature_frequency_vector.npy', freqVec)

print(f"finished after {time.time()-start_time:.2f}s")
