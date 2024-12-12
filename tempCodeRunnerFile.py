import tkinter as tk
from tkinter import filedialog
from sklearn.cluster import KMeans
import pandas as pd

import matplotlib.pyplot as plt

class KMeansClusteringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Means Clustering")

        self.label = tk.Label(root, text="Select Dataset:")
        self.label.pack()

        self.file_button = tk.Button(root, text="Browse", command=self.load_file)
        self.file_button.pack()

        self.cluster_button = tk.Button(root, text="Cluster", command=self.perform_clustering)
        self.cluster_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def load_file(self):
        self.file_path = filedialog.askopenfilename()
        self.data = pd.read_csv(self.file_path)
        self.result_label.config(text="File Loaded: " + self.file_path)

    def perform_clustering(self):
        if hasattr(self, 'data'):
            kmeans = KMeans(n_clusters=3)
            self.data['Cluster'] = kmeans.fit_predict(self.data.iloc[:, :-1])
            self.show_clusters()
        else:
            self.result_label.config(text="Please load a dataset first.")

    def show_clusters(self):
        plt.scatter(self.data.iloc[:, 0], self.data.iloc[:, 1], c=self.data['Cluster'])
        plt.title('K-Means Clustering')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = KMeansClusteringApp(root)
    root.mainloop()