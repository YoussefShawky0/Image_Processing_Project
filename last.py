import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Global Variables
original_image = None
processed_image = None


# Functions
def upload_image():
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
        reset_histogram()


def display_image(img, canvas):
    """Display an image on a canvas."""
    canvas_width, canvas_height = 350, 350
    img = img.resize((canvas_width, canvas_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(
        canvas_width // 2, canvas_height // 2, image=photo, anchor=tk.CENTER
    )
    canvas.image = photo  # Keep reference to avoid garbage collection


def apply_processing():
    global processed_image
    if not original_image or filter_combobox.get() == "Select Filter":
        messagebox.showerror("Error", "Please upload an image and select a filter.")
        return

    filter_type = filter_combobox.get()
    np_image = np.array(original_image)

    if filter_type == "Median Filter":
        processed_np = cv2.medianBlur(np_image, 5)  # Kernel size 5
    elif filter_type == "Averaging Filter":
        processed_np = cv2.blur(np_image, (5, 5))  # Kernel size 5x5
    elif filter_type == "Low-pass Filters":
        processed_np = cv2.GaussianBlur(np_image, (5, 5), 0)  # Gaussian Blur
    else:
        return

    processed_image = Image.fromarray(processed_np)
    display_image(processed_image, after_canvas)
    plot_histogram(processed_image)


def reset_images():
    if original_image:
        display_image(original_image, before_canvas)
        display_image(original_image, after_canvas)
        reset_histogram()


def reset_histogram():
    histogram_canvas.delete("all")


def plot_histogram(img):
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


# Gui
root = tk.Tk()
root.title("Noise Reduction and K-Means Clustering APP")

root.geometry("1150x600")
root.configure(bg="#A9C4E2")  # Background color

# Header
header_frame = tk.Frame(root, bg="#506B86", height=50)
header_frame.pack(fill=tk.X)
header_label = tk.Label(
    header_frame,
    text="Noise Reduction and K-Means Clustering APP",
    bg="#506B86",
    fg="black",
    font=("Times New Roman", 16, "bold"),
)
header_label.pack(pady=10)

# Main Content
content_frame = tk.Frame(root, bg="#A9C4E2")
content_frame.pack()

before_canvas = tk.Canvas(
    content_frame, width=350, height=350, bg="lightgray", bd=2, relief="ridge", border=0
)
before_canvas.grid(row=1, column=0, padx=5, pady=10)
after_canvas = tk.Canvas(
    content_frame, width=350, height=350, bg="lightgray", bd=2, relief="ridge", border=0
)
after_canvas.grid(row=1, column=1, padx=5, pady=10)
histogram_canvas = tk.Canvas(
    content_frame, width=350, height=350, bg="lightgray", bd=2, relief="ridge", border=0
)
histogram_canvas.grid(row=1, column=2, padx=5, pady=10)

# Labels
before_label = tk.Label(
    content_frame, text="Before", bg="#A9C4E2",  font=("Times New Roman", 15, "bold") ,

)
before_label.grid(row=0, column=0, pady=5)
after_label = tk.Label(
    content_frame, text="After", bg="#A9C4E2",     font=("Times New Roman", 15, "bold"),

)
after_label.grid(row=0, column=1, pady=5)
histogram_label = tk.Label(
    content_frame, text="Histogram", bg="#A9C4E2",     font=("Times New Roman", 15, "bold"),

)
histogram_label.grid(row=0, column=2, pady=5)

# Button Styling
style = ttk.Style()
style.configure(
    "Rounded.TButton",
    font=("Times New Roman", 10, "bold"),
    background="#A9C4E2",
    # padding=3,
    relief="raised",
)
style.map(
    "Rounded.TButton",
    background=[("active", "#DDEEFF")],
    relief=[("pressed", "sunken")],
)


# Buttons and Dropdown
before_buttons_frame = tk.Frame(content_frame, bg="#A9C4E2")
before_buttons_frame.grid(row=2, column=0, pady=10)  # Place below "Before" canvas

upload_button = ttk.Button(
    before_buttons_frame, text="Upload ⬆", command=upload_image, style="Rounded.TButton"
)
upload_button.grid(row=0, column=0, padx=5 )

apply_button = ttk.Button(
    before_buttons_frame,
    text="Apply",
    command=apply_processing,
    style="Rounded.TButton",
)
apply_button.grid(row=0, column=1, padx=5)

reset_button = ttk.Button(
    before_buttons_frame, text="Reset ⟳", command=reset_images, style="Rounded.TButton"
)
reset_button.grid(row=1, column=0, padx=5)

save_button = ttk.Button(
    before_buttons_frame, text="Save", command=save_image, style="Rounded.TButton"
)
save_button.grid(row=1, column=1, padx=5)

filter_combobox = ttk.Combobox(
    before_buttons_frame,
    values=["Median Filter", "Averaging Filter", "Low-pass Filters"],
    state="readonly",
    width=18,
    justify="center",
    style="Rounded.TButton",
    font=("Times New Roman", 10, "bold"),
)  # Make combobox read-only
filter_combobox.set("Select Filter ▼")
filter_combobox.grid(row=0, column=2, pady=5)

# Run App
root.mainloop()
