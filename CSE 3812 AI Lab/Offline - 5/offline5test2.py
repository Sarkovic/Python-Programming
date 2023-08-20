import numpy as np
import matplotlib.pyplot as plt


def k_means_clustering(data, k):
    n = data.shape[0]
    cluster_centers = data[np.random.choice(n, k, replace=False)]

    clusters = [[] for _ in range(cluster_centers.shape[0])]
    temp_clusters = [[] for _ in range(cluster_centers.shape[0])]

    iteration = 0

    while True:
        temp_clusters = [[] for _ in range(cluster_centers.shape[0])]

        distances = np.linalg.norm(data[:, np.newaxis, :] - cluster_centers, axis=2)

        closest_center_indices = np.argmin(distances, axis=1)
        for sample_idx, center_idx in enumerate(closest_center_indices):
            temp_clusters[center_idx].append(sample_idx)

        for cluster_idx, cluster_samples in enumerate(temp_clusters):
            if len(cluster_samples) > 0:
                new_center = np.mean(data[cluster_samples], axis=0)
                cluster_centers[cluster_idx] = new_center

        iteration += 1

        if iteration > 1:
            shifts = np.zeros(data.shape[0], dtype=bool)

            for idx, sample in enumerate(data):
                old_cluster = np.where([idx in cluster_samples for cluster_samples in clusters])[0]
                new_cluster = np.where([idx in cluster_samples for cluster_samples in temp_clusters])[0]

                if old_cluster != new_cluster:
                    shifts[idx] = True

            shift_count = np.sum(shifts)

            if shift_count < 10:
                clusters = temp_clusters.copy()
                break

        clusters = temp_clusters.copy()

    colors = ['r', 'g', 'b', 'c', 'm', 'y']

    for cluster_idx, cluster_samples in enumerate(clusters):
        color = colors[cluster_idx % len(colors)]
        plt.scatter(data[cluster_samples, 0], data[cluster_samples, 1], c=color, marker='o', alpha=0.5)

    for center_idx, center in enumerate(cluster_centers):
        plt.scatter(center[0], center[1], c='k', marker='X', s=100)

    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('K-Means Clustering')
    plt.show()


# Example usage
data_path = 'E:\Important Documents\Programming\Python-Programming\CSE 3812 AI Lab\Offline - 5\offline_5_data.csv'
data = np.genfromtxt(data_path, delimiter=',')
k_means_clustering(data, k=6)
