import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb, file_path):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

