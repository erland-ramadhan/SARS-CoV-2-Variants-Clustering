import requests
import os
import time
import numpy as np
from itertools import product
from tqdm import tqdm

def where_id(al, s):
    base = len(al)
    id = 0
    for i in range(len(s)):
        id += base**i * al.index(s[-1-i])
    return id

proSeq_url = 'https://www.dropbox.com/scl/fi/4ks35g2qfxwlz0p72ueqp/filtered_protein_seq.npy?rlkey=jdlbpabbhfx44rztzkdxygh1q&st=n5i4fwlr&dl=1'
filename = 'filtered_protein_seq.npy'

if os.path.exists(filename):
    print(f"{filename} already exists. Skipping download.")
else:
    response = requests.get(proSeq_url, stream=True)
    
    # Get the total file size from the headers
    totalSize = int(response.headers.get('content-length', 0))
    
    # Define the chunk size (in bytes)
    chunkSize = 1024
    
    print("Downloading filtered protein sequences stored in NumPy binary file!")

    # Open a file to write the downloaded NumPy binary file
    with open(filename, "wb") as file:
        # Wrap the file download with tqdm for progress tracking
        for data in tqdm(response.iter_content(chunk_size=chunkSize), total=totalSize // chunkSize, unit='KB'):
            file.write(data)

    print(f"{filename} downloaded successfully.")

proSeq = np.load(os.path.join(os.getcwd(), filename))
dataSize = proSeq.shape[0]
seqLen = len(proSeq[0])

k = 3
aminoSeq = 'ACDEFGHIKLMNPQRSTVWXY'
fvLen = len(aminoSeq)**k

freqVec = np.zeros(shape=(dataSize, fvLen))
start_time = time.time()

print("Generating feature vectors! Please be patient! \nIt should be finished within minutes.")
for i in range(dataSize):
    for j in range(seqLen-k):
        id = where_id(aminoSeq, proSeq[i][j:j+k])
        freqVec[i, id] += 1

freqVec = freqVec.astype(np.uint8)
np.save(os.getcwd() + '/feature_frequency_vector.npy', freqVec)

print(f"finished after {time.time()-start_time:.2f}s")
