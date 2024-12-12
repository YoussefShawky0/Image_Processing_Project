import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def remove_periodic_noise(img_path: str, filter_type: int):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)  # read image in grayscale

    fourier_transform = np.fft.fft2(img)
    center_shift = np.fft.fftshift(fourier_transform)

    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    if filter_type == 1:  # vertical noise
        # horizontal mask
        center_shift[crow - 4 : crow + 4, 0 : ccol - 10] = 1
        center_shift[crow - 4 : crow + 4, ccol + 10 :] = 1
    elif filter_type == 2:  # horizontal noise
        # vertical mask
        center_shift[: crow - 10, ccol - 4 : ccol + 4] = 1
        center_shift[crow + 10 :, ccol - 4 : ccol + 4] = 1
    elif filter_type == 3:  # right diagonal noise
        # diagonal-1 mask
        for x in range(0, rows):
            for y in range(0, cols):
                if x == y:
                    for i in range(0, 10):
                        center_shift[x - i, y] = 1
    elif filter_type == 4:  # left diagonal noise
        # diagonal-2 mask
        for x in range(0, rows):
            for y in range(0, cols):
                if x + y == cols:
                    for i in range(0, 10):
                        center_shift[x - i, y] = 1

    f_shift = np.fft.ifftshift(center_shift)
    denoised_image = np.fft.ifft2(f_shift)
    denoised_image = np.real(denoised_image)
    denoised_image = np.clip(denoised_image, 0, 255).astype(np.uint8)
    return denoised_image
