import os
from sklearn.cluster import KMeans
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))

header = ['Index', 'A', 'B']
numerical = pd.read_csv(os.path.join(dir_path, "numerical.csv"), header=0, names=header)
numerical = numerical[['A', 'B']]
kmeans = KMeans(n_clusters=2, random_state=0).fit(numerical)
print(kmeans.labels_)
print(kmeans.cluster_centers_)