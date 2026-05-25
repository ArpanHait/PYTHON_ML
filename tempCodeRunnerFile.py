import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import time

def generate_data(n_samples=300, centers=4):
    X, y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=0.60, random_state=42)
    return X

def perform_clustering(X, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    return kmeans.labels_, kmeans.cluster_centers_

def plot_clusters(X, labels, centers, title="K-Means Clustering Result"):
    plt.figure(figsize=(10, 6))
    
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis', alpha=0.7, label='Data Points')
    
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', label='Centroids')
    
    plt.title(title, fontsize=15, fontweight='bold')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    filename = "clustering_result.png"
    plt.savefig(filename)
    print(f"Plot saved as {filename}")
    plt.show()

def main():
    print("--- Machine Learning Clustering Demonstration ---")
    
    print("Generating synthetic data...")
    
    X = generate_data()
    
    print("Performing K-Means clustering (K=4)...")
    labels, centers = perform_clustering(X)
    
    print("Visualization processing...")
    
    plot_clusters(X, labels, centers)
    
    print("\nSummary:")
    print(f"Total Samples: {len(X)}")
    
    print(f"Number of Clusters: 4")
    print("-" * 45)
    
    print("Execution complete. Check clustering_result.png for the visual output.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"\nTotal Execution Time: {time.time() - start_time:.2f} seconds")
