import os
from sklearn.cluster import KMeans
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))

header = ['Index', 'Class A', 'Class B', 'Class C', 'Class D', 'Class E']
numerical = pd.read_csv(os.path.join(dir_path, "numerical.csv"), header=0, names=header)
numerical = numerical[['Class A', 'Class B', 'Class C', 'Class D', 'Class E']]
kmeans = KMeans(n_clusters=2, random_state=0).fit(numerical)
print(kmeans.labels_)
print(kmeans.cluster_centers_)

