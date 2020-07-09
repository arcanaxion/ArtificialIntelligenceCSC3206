# import libraries
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# generate dataset
from sklearn.datasets import make_blobs
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)
points = data[0]

# initialise the k-means model
kmeans = KMeans(n_clusters=4)

# train the k-means model
kmeans.fit(points)

# identify the cluster of each point
y_km = kmeans.fit_predict(points)

# visualise the result
plt.figure('KMeans')
plt.scatter(points[:,0], points[:,1], c=y_km)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='red')

plt.figure('Original')
plt.scatter(points[:,0], points[:,1], c=data[1])
plt.show()