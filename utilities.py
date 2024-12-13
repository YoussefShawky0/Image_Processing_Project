import cv2
import os
import cv2 as cv
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

original_image = None
processed_image = None
file_path = None


def upload_image(before_canvas, histogram_canvas):
    global original_image, processed_image, file_path

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    if file_path:
        original_image = Image.open(file_path).convert(
            "RGB"
        )  # Convert to RGB to handle transparency
        processed_image = original_image.copy()
        display_image(original_image, before_canvas)
        reset_histogram(histogram_canvas)


def display_image(img, canvas):
    """Display an image on a canvas."""
    canvas_width, canvas_height = 350, 350
    img = img.resize((canvas_width, canvas_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(
        canvas_width // 2, canvas_height // 2, image=photo, anchor=tk.CENTER
    )
    canvas.image = photo  # Keep reference to avoid garbage collection


def apply_processing(filter_combobox, after_canvas, histogram_canvas, periodic_types):
    global processed_image, file_path
    if not original_image or filter_combobox.get() == "Select Filter":
        messagebox.showerror("Error", "Please upload an image and select a filter.")
        return

    filter_type = filter_combobox.get()
    np_image = np.array(original_image)

    cv2.
    if filter_type == "Median Filter":
        gray_np = cv2.cvtColor(np_image, cv2.COLOR_RGB2GRAY)
        processed_np = cv2.medianBlur(gray_np, 3)  # Kernel size 3x3
    elif filter_type == "Averaging Filter":
        processed_np = cv2.blur(np_image, (1, 1))  # Kernel size 9x9
    elif filter_type == "Low-pass Filters":
        processed_np = cv2.GaussianBlur(
            np_image, (9, 9), 0
        )  # Gaussian Blur with kernel size 9x9
    elif filter_type == "Canney Edge Detection":
        processed_np = cv2.Canny(np_image, 100, 200)  # Canny Edge Detection
    elif filter_type == "Periodic noise Filter":
        filter_type = periodic_types.get()
        periodic_type_code = apply_periodic_filter(filter_type)
        processed_np = remove_periodic_noise(file_path, periodic_type_code)
    elif filter_type == "RGB to Grayscale":
        processed_np = rgb2gray(np_image, file_path)
    else:
        return

    processed_image = Image.fromarray(processed_np)
    display_image(processed_image, after_canvas)
    plot_histogram(processed_image, histogram_canvas)


def reset_images(before_canvas, after_canvas, histogram_canvas):
    before_canvas.delete("all")
    after_canvas.delete("all")
    reset_histogram(histogram_canvas)


def reset_histogram(histogram_canvas):
    histogram_canvas.delete("all")
    if os.path.exists("histogram.png"):
        os.remove("histogram.png")


def plot_histogram(img, histogram_canvas):
    """Plot histogram of an image."""
    np_image = np.array(img).flatten()
    plt.figure(figsize=(3, 2))
    plt.hist(np_image, bins=256, color="gray", alpha=0.7)
    plt.title("Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("histogram.png", dpi=100)
    plt.close()

    hist_img = Image.open("histogram.png")
    display_image(hist_img, histogram_canvas)


def save_image():
    if processed_image:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*"),
            ],
        )
        if file_path:
            try:
                # Ensure the image is in a compatible mode before saving
                if processed_image.mode == "F":
                    processed_image_converted = processed_image.convert("L")
                else:
                    processed_image_converted = processed_image
                processed_image_converted.save(file_path)
                messagebox.showinfo("Saved", f"Image saved successfully at {file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save image: {e}")


def apply_periodic_filter(filter_type):
    if filter_type == "vertical noise":
        return 1
    elif filter_type == "horizontal noise":
        return 2
    elif filter_type == "right diagonal noise":
        return 3
    elif filter_type == "left diagonal noise":
        return 4
    else:
        return 0


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
        # left diagonal mask
        center_shift[: crow - 10, : ccol - 10] = 1
        center_shift[crow + 10 :, ccol + 10 :] = 1
    elif filter_type == 4:  # left diagonal noise
        # right diagonal mask
        center_shift[: crow - 10, ccol + 10 :] = 1
        center_shift[crow + 10 :, : ccol - 10] = 1

    f_shift = np.fft.ifftshift(center_shift)
    denoised_image = np.fft.ifft2(f_shift)
    denoised_image = np.real(denoised_image)
    denoised_image = np.clip(denoised_image, 0, 255).astype(np.uint8)
    return denoised_image


def rgb2gray(rgb, file_path):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
