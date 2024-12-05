import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os


original_image = None
processed_image = None


def upload_image(before_canvas, histogram_canvas):
    global original_image, processed_image
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


def apply_processing(filter_combobox, after_canvas, histogram_canvas):
    global processed_image
    if not original_image or filter_combobox.get() == "Select Filter":
        messagebox.showerror("Error", "Please upload an image and select a filter.")
        return

    filter_type = filter_combobox.get()
    np_image = np.array(original_image)

    if filter_type == "Median Filter":
        processed_np = cv2.medianBlur(np_image, 9)  # Kernel size 9
    elif filter_type == "Averaging Filter":
        processed_np = cv2.blur(np_image, (3, 3))  # Kernel size 9x9
    elif filter_type == "Low-pass Filters":
        processed_np = cv2.GaussianBlur(np_image, (9, 9), 0)  # Gaussian Blur with kernel size 9x9
    elif filter_type == "Canney Edge Detection":
        processed_np = cv2.Canny(np_image, 100, 200)  # Canny Edge Detection
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
            processed_image.save(file_path)
            messagebox.showinfo("Saved", f"Image saved successfully at {file_path}")