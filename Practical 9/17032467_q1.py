# import libraries
import matplotlib.pyplot as plt
import numpy as np
import random

# functions
## function to take input of data and number of clusters, return centroids and other data
def get_random_centroids(data_points, n_centroids=2):
  # np.random.seed(0)
  choices = np.random.choice(data_points.shape[0], n_centroids, replace=False, ) 
  return data_points[choices], np.delete(data_points, choices, axis=0)

## function to group data according to centroids
def group_to_centroids(data_points, centroids):
  distance = centroids-data_points[:,np.newaxis]
  # euclidean = np.abs(np.sum(distance, axis=2))
  euclidean = np.abs(np.sqrt(np.square(distance[:,:,0]) + np.square(distance[:,:,1])))
  ind = np.argpartition(euclidean, 1)[:,0]
  return ind

## function to calculate centroids from grouped data
def find_centroids(data_points, groups):
  return np.array([np.mean(group, axis=0) for group in groupby(data_points, groups)])
  
# func from stackoverflow
def groupby(a, b):
  # Get argsort indices, to be used to sort a and b in the next steps
  sidx = b.argsort(kind='mergesort')
  a_sorted = a[sidx]
  b_sorted = b[sidx]

  # Get the group limit indices (start, stop of groups)
  cut_idx = np.flatnonzero(np.r_[True,b_sorted[1:] != b_sorted[:-1],True])

  # Split input array with those start, stop ones
  out = [a_sorted[i:j] for i,j in zip(cut_idx[:-1],cut_idx[1:])]
  return out

# generate dataset
from sklearn.datasets import make_blobs
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6)

points = data[0]

plt.figure
plt.scatter(points[:,0], points[:,1])
plt.show()


# identify initial centroids
centroids, others = get_random_centroids(points, 4)

# repeat until centroids stabilise
cents = None
old_centroids = np.zeros_like(centroids)
plt.figure('Manual KMeans')
while not np.array_equal(old_centroids, centroids):
  old_centroids = centroids
  ## group data to centroids
  groups = group_to_centroids(others, centroids)
  

  # plot
  plt.scatter(others[:,0], others[:,1], c=groups)
  if cents:
    cents.remove()
  cents = plt.scatter(centroids[:,0], centroids[:,1], c='red')

  plt.pause(0.5)

  ## update centroids
  centroids = find_centroids(others, groups)


plt.show()

print('terminated')