import numpy as np
import matplotlib.pyplot as plt


def k_means_clustering(dataset, k):
    n = dataset.shape[0]

    cluster_centers = dataset[np.random.choice(n, k, replace=False)]

    clusters = [[] for _ in range(cluster_centers.shape[0])]
    temp_clusters = [[] for _ in range(cluster_centers.shape[0])]

    iteration = 0

    while True:
        temp_clusters = [[] for _ in range(cluster_centers.shape[0])]
        distance = np.zeros((n, k))
        for i in range(k):
            distance[:, i] = ((dataset - cluster_centers[i]) ** 2).sum(axis=1) ** 0.5

        # Keep the minimum distance
        closest_center_indices = np.argmin(distance, axis=1)

        for sample_idx, center_idx in enumerate(closest_center_indices):
            # Append sample index in the ith list of temporary clusters
            temp_clusters[center_idx].append(sample_idx)

        # Calculate new centers by determining the average
        for i in range(k):
            cluster_centers[i] = dataset[closest_center_indices == i].mean(axis=0)

        iteration += 1

        if iteration > 1:
            shifts = np.zeros(dataset.shape[0], dtype=bool)

            for idx, sample in enumerate(dataset):
                old_cluster = np.where([idx in cluster_samples for cluster_samples in clusters])[0]
                new_cluster = np.where([idx in cluster_samples for cluster_samples in temp_clusters])[0]

                if clusters != temp_clusters:
                    shifts[idx] = True

            shift_count = np.sum(shifts)

            if shift_count < 10:
                clusters = temp_clusters.copy()
                break

        clusters = temp_clusters.copy()

    plt.scatter(dataset[:, 0], dataset[:, 1], c=closest_center_indices)
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='*')
    plt.show()


# Example usage
data_path = 'E:\Important Documents\Programming\Python-Programming\CSE 3812 AI Lab\Offline - 5\offline_5_data.csv'
data = np.genfromtxt(data_path, delimiter=',')
k_means_clustering(data, k=6)
