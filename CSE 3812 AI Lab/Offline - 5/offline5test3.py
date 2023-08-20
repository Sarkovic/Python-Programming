import numpy as np

# Load data.csv into a 2D numpy array "Data"
data_path = 'E:\Important Documents\Programming\Python-Programming\CSE 3812 AI Lab\Offline - 5\offline_5_data.csv'
Data = np.genfromtxt(data_path, delimiter=',')
n = Data.shape[0]
k = 6
# Load centers.csv into a 2D numpy array "Centers"
# centers_path = 'E:\Important Documents\Programming\Python-Programming\CSE 3812 AI Lab\Offline - 5\offline_5_data.csv'
Centers = Data[np.random.choice(n, k, replace=False)]

# Initialize clusters and temp_clusters
Clusters = [[] for _ in range(Centers.shape[0])]
Temp_Clusters = [[] for _ in range(Centers.shape[0])]

iteration = 0

while True:
    # Clear Temp_Clusters at the start of each iteration
    Temp_Clusters = [[] for _ in range(Centers.shape[0])]

    # Calculate distances between each sample and each center using broadcasting
    distances = np.linalg.norm(Data[:, np.newaxis, :] - Centers, axis=2)

    # Assign samples to the closest center using argmin
    closest_center_indices = np.argmin(distances, axis=1)
    for sample_idx, center_idx in enumerate(closest_center_indices):
        Temp_Clusters[center_idx].append(sample_idx)

    # Calculate new centers
    for cluster_idx, cluster_samples in enumerate(Temp_Clusters):
        if len(cluster_samples) > 0:
            new_center = np.mean(Data[cluster_samples], axis=0)
            Centers[cluster_idx] = new_center

    iteration += 1

    if iteration > 1:
        shifts = np.zeros(Data.shape[0], dtype=bool)

        for idx, sample in enumerate(Data):
            old_cluster = np.where([idx in cluster_samples for cluster_samples in Clusters])[0]
            new_cluster = np.where([idx in cluster_samples for cluster_samples in Temp_Clusters])[0]

            if old_cluster != new_cluster:
                shifts[idx] = True

        shift_count = np.sum(shifts)

        if shift_count < 10:
            Clusters = Temp_Clusters.copy()
            break

    Clusters = Temp_Clusters.copy()

# Plot the clusters and centers
import matplotlib.pyplot as plt

colors = ['r', 'g', 'b', 'c', 'm', 'y']

for cluster_idx, cluster_samples in enumerate(Clusters):
    color = colors[cluster_idx % len(colors)]
    plt.scatter(Data[cluster_samples, 0], Data[cluster_samples, 1], c=color, marker='o', alpha=0.5)

for center_idx, center in enumerate(Centers):
    plt.scatter(center[0], center[1], c='k', marker='X', s=100)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.show()
