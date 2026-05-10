from sklearn.cluster import KMeans
# Dataset: [weight, color_score]
X = [
    [150, 8],
    [160, 7],
    [200, 3],
    [210, 4]
]

# Create the model
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)
# TODO: Train the model (fit it to X)
# Hint: Use kmeans.fit(...)
clusters=kmeans.predict(X)
# TODO: Predict cluster for each fruit
# Hint: Use kmeans.predict(...)
print("Cluster assignments:", clusters)