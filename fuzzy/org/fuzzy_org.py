import pandas as pd
import numpy as np
import time

import csv
import os

from fcmeans import FCM

print("Packages Loaded!!!")

vector_path = os.getcwd() + "/../../feature_frequency_vector.npy"
variant_path = os.getcwd() + "/../../filtered_variants.npy"

X = np.load(vector_path)
y_orig = np.load(variant_path)

print("Attributed data Reading Done")

unique_varaints = list(np.unique(y_orig))

int_variants = []
for ind_unique in range(len(y_orig)):
    variant_tmp = y_orig[ind_unique]
    ind_tmp = unique_varaints.index(variant_tmp)
    int_variants.append(ind_tmp)

print("Attribute data preprocessing Done")

y =  np.array(int_variants, dtype=np.uint8)

start_time = time.time()

number_of_clusters = 5 #number of clusters

print("Number of Clusters = ", number_of_clusters)
clust_num = number_of_clusters

fcm = FCM(n_clusters=clust_num, random_state=0)
fcm.fit(X)
fcm_centers = fcm.centers
labels = fcm.predict(X)

np.save(os.getcwd() + '/new_Labels_fuzzy_org.npy', labels)

end_time = time.time() - start_time
print("Clustering Time in seconds =>",end_time)

write_path_112 = os.getcwd() +  "/new_int_true_variants_k_" + str(clust_num) + ".csv"

pd.DataFrame(y).to_csv(write_path_112, header=False, index=False)

write_path_11 = os.getcwd() + "/new_orig_true_variants_k_" + str(clust_num) + ".csv"

pd.DataFrame(y_orig).to_csv(write_path_11, header=False, index=False)

print("All Processing Done!!!")

