import tkinter as tk
from tkinter import filedialog, messagebox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score

class KMeansClusteringApp:
  
    def __init__(self, root):
      
        self.root = root
        self.root.title("K-Means Clustering")

        self.label = tk.Label(root, text="Load Dataset:")
        self.label.pack()

        self.file_button = tk.Button(root, text="Load Digits Dataset", command=self.load_file)
        self.file_button.pack()

        self.cluster_button = tk.Button(root, text="Cluster", command=self.perform_clustering)
        self.cluster_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def load_file(self):
        
        self.df = load_digits()   
        
        self.X = self.df['images'] 
        self.result_label.config(text="File Loaded Successfully")
        
        self.y = self.df['target']
        self.X_flattened = self.df["data"]
       
        mx_val = self.X_flattened.max()
        self.X_flattened /= mx_val # Normalization   

    def perform_clustering(self):
      
        if hasattr(self, 'X'):
            
            model = KMeans(n_clusters = 10, random_state = 5)
            model.fit(self.X_flattened)
            self.y_pred = model.labels_
            
            self.map_clusters()
            self.show_clusters()
            self.show_accuracy_score()
            
        else:
            self.result_label.config(text="Please load a dataset first.")
    
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
       
        plt.title('K-Means Clustering')
        
        for cluster in range(10):

            plt.subplot(2, 5, cluster + 1)
            plt.xlabel(f"digit = {self.y_pred[cluster + 10]}")
            plt.imshow(self.X[cluster + 10])

        plt.show()
    
    def show_accuracy_score(self):
        
        accuracy = round(accuracy_score(self.y, self.y_pred), 2) * 100
        messagebox.showinfo("Accuracy", f"Accuracy Score = {accuracy}")
        
       

if __name__ == "__main__":
  
    root = tk.Tk()
    app = KMeansClusteringApp(root)
    root.mainloop()