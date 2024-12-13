import numpy as np
from tkinter import messagebox
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score


class KMeansClusteringApp:

    def __init__(self):

        self.preprocessing()
        self.train()

        self.y_pred = self.model.labels_

        self.map_clusters()
        self.show_clusters()
        self.show_accuracy_score()

    def preprocessing(self):

        self.df = load_digits()

        self.X = self.df["images"]

        self.y = self.df["target"]
        self.X_flattened = self.df["data"]

        mx_val = self.X_flattened.max()
        self.X_flattened /= mx_val  # Normalization

    def train(self):

        self.model = KMeans(n_clusters=10, random_state=5)
        self.model.fit(self.X_flattened)

    def most_common_digit(self, cluster):

        cluster_indices = np.where(self.y_pred == cluster)
        true_digits = self.y[cluster_indices]

        frequencies = np.bincount(true_digits)
        most_common = frequencies.argmax()

        return most_common

    def map_clusters(self):

        edits = []

        for cluster in range(10):

            # Storing the most common digit in a cluster in the edits list

            most_common = self.most_common_digit(cluster)
            edits.append(most_common)

        # Cluster number -> most common digit found in it

        self.y_pred = [edits[cluster] for cluster in self.y_pred]
        self.y_pred = np.array(self.y_pred)

    def show_clusters(self):

        plt.title("K-Means Clustering")

        for cluster in range(10):

            plt.subplot(2, 5, cluster + 1)
            plt.xlabel(f"digit = {self.y_pred[cluster + 10]}")
            plt.imshow(self.X[cluster + 10])

        plt.show()

    def predict(self, X_flattened):
        return self.model.predict(X_flattened)

    def show_accuracy_score(self):

        accuracy = round(accuracy_score(self.y, self.y_pred), 2) * 100
        messagebox.showinfo("Accuracy", f"Accuracy Score = {accuracy} %")
