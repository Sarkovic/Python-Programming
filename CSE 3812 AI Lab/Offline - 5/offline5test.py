import math
import numpy as np
import matplotlib.pyplot as plt

# Load data.csv into 2D numpy array "Data"
data_path = 'offline_5_data.csv'
data = np.genfromtxt(data_path, delimiter=',')
n = data.shape[0]
k = 6

# Load centers.csv into 2D numpy array "Centers"
cluster_centers = data[np.random.choice(n, k, replace=False)]

# Initialize clusters and temp_clusters
clusters = [[] for _ in range(k)]
temp_clusters = [[] for _ in range(k)]

# Initialize iteration
iteration = 0

# Main loop
while True:
    # Clear temp_clusters
    temp_clusters = [[] for _ in range(k)]

    # Assign each sample to the closest center
    for i, sample in enumerate(data):
        min_distance_idx = np.argmin(np.linalg.norm(sample - cluster_centers, axis=1))
        temp_clusters[min_distance_idx].append(i)

    # Calculate new centers
    new_centers = np.array([np.mean(data[temp_clusters[i]], axis=0) for i in range(k)])

    # Check for convergence
    if np.array_equal(new_centers, cluster_centers):
        break

    # Update centers and clusters
    centers = new_centers
    clusters = temp_clusters.copy()

    iteration += 1

    # Check for convergence based on shifts
    if iteration > 1:
        shift_count = 0
        for i, sample in enumerate(data):
            old_cluster_idx = np.argmax([i in cluster for cluster in clusters])
            new_cluster_idx = np.argmax([i in cluster for cluster in temp_clusters])
            if old_cluster_idx != new_cluster_idx:
                shift_count += 1

        if shift_count < 10:
            break

# Plotting
colors = ['r', 'g', 'b', 'c', 'm', 'y']

for i, cluster in enumerate(clusters):
    cluster_data = data[cluster]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i], label=f'Cluster {i+1}')

plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='k', marker='X', label='Cluster Centers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('K-Means Clustering')
plt.show()

