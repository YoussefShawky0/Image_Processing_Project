import tkinter as tk
from tkinter import ttk
from utilities import *


# Gui
root = tk.Tk()
root.title("Noise Reduction and K-Means Clustering APP")
root.geometry("1150x600")
root.configure(bg="#CBDCEB")

# Header Frame and Label
header_frame = tk.Frame(root, bg="#133E87", height=50)
header_frame.pack(fill=tk.X)
header_label = tk.Label(
    header_frame,
    text="Noise Reduction and K-Means Clustering APP",
    bg="#133E87",
    fg="#CBDCEB",
    font=("calibri", 20, "bold"),
)
header_label.pack(pady=10)

# Main Content
content_frame = tk.Frame(root, bg="#CBDCEB")
content_frame.pack()

# before image
before_canvas = tk.Canvas(
    content_frame,
    width=350,
    height=350,
    bg="lightgray",
    bd=2,
    relief="ridge",
    border=0,
)
before_canvas.grid(row=1, column=0, padx=5, pady=10)

# after image
after_canvas = tk.Canvas(
    content_frame,
    width=350,
    height=350,
    bg="lightgray",
    bd=2,
    relief="ridge",
    border=0,
)
after_canvas.grid(row=1, column=1, padx=5, pady=10)

# histogram
histogram_canvas = tk.Canvas(
    content_frame,
    width=350,
    height=350,
    bg="lightgray",
    bd=2,
    relief="ridge",
    border=0,
)
histogram_canvas.grid(row=1, column=2, padx=5, pady=10)

# Labels
before_label = tk.Label(
    content_frame,
    text="Before",
    bg="#CBDCEB",
    font=("calibri", 20, "bold"),
    foreground="#133E87",
)
before_label.grid(row=0, column=0, pady=5)

after_label = tk.Label(
    content_frame,
    text="After",
    bg="#CBDCEB",
    foreground="#133E87",
    font=("calibri", 20, "bold"),
)
after_label.grid(row=0, column=1, pady=5)

histogram_label = tk.Label(
    content_frame,
    text="Histogram",
    foreground="#133E87",
    bg="#CBDCEB",
    font=("calibri", 20, "bold"),
)
histogram_label.grid(row=0, column=2, pady=5)

# Button Styling
style = ttk.Style()
style.configure(
    "Rounded.TButton",
    font=("calibri", 11, "bold"),
    background="#CBDCEB",
    padding=5,
    foreground="#133E87",
)
# Allow dynamic changes to the style
style.map(
    "Rounded.TButton",
    background=[("active", "#CBDCEB")],
    relief=[("pressed", "sunken")],
)

# Buttons and Dropdown
buttons_frame = tk.Frame(content_frame, bg="#CBDCEB")
buttons_frame.grid(row=2, column=0, columnspan=1, pady=10)

upload_button = ttk.Button(
    buttons_frame,
    text="Upload ⬆",
    command=lambda: upload_image(before_canvas, histogram_canvas),
    style="Rounded.TButton",
)
upload_button.grid(row=0, column=0, padx=5)

apply_button = ttk.Button(
    buttons_frame,
    text="Apply",
    command=lambda: apply_processing(
        filter_combobox, after_canvas, histogram_canvas, periodic_types
    ),
    style="Rounded.TButton",
)
apply_button.grid(row=0, column=1, padx=5)

reset_button = ttk.Button(
    buttons_frame,
    text="Reset ⟳",
    command=lambda: reset_images(before_canvas, after_canvas, histogram_canvas),
    style="Rounded.TButton",
)
reset_button.grid(row=1, column=0, padx=5)

save_button = ttk.Button(
    buttons_frame,
    text="Save",
    command=save_image,
    style="Rounded.TButton",
)
save_button.grid(row=1, column=1, padx=5)

filter_combobox = ttk.Combobox(
    buttons_frame,
    values=[
        "Median Filter",
        "Averaging Filter",
        "Low-pass Filters",
        "Canney Edge Detection",
        "RGB to Grayscale",
        "K-Means Clustering",
        "Periodic noise Filter",
    ],
    state="readonly", 
    width=18,
    justify="center",
    style="Rounded.TButton",
    font=("calibri", 10, "bold"),
)
filter_combobox.set("Select Filter ▼")
filter_combobox.grid(row=0, column=2, pady=5)

periodic_types = ttk.Combobox(
    buttons_frame,
    values=[
        "vertical noise",
        "horizontal noise",
    ],
    state="readonly",
    width=18,
    justify="center",
    style="Rounded.TButton",
    font=("calibri", 10, "bold"),
)
periodic_types.set("Periodic Type ▼")
periodic_types.grid(row=1, column=2, pady=5)
periodic_types.grid_remove()  # Hide initially


kmeans_apply_button = ttk.Button(
    buttons_frame,
    text="Apply K-Means",
    command=lambda: apply_kmeans(),
    style="Rounded.TButton",
)
kmeans_apply_button.grid(row=1, column=2, pady=5)
kmeans_apply_button.grid_remove()  # Hide initially

def show_periodic_types(event):
    if filter_combobox.get() == "Periodic noise Filter":
        periodic_types.grid()
    else:
        periodic_types.grid_remove()

def show_kmeans_view(event):
    if filter_combobox.get() == "K-Means Clustering":
        kmeans_apply_button.grid()
    else:
        kmeans_apply_button.grid_remove()

filter_combobox.bind(
    "<<ComboboxSelected>>", lambda e: (show_periodic_types(e), show_kmeans_view(e))
)



# Run App
root.mainloop()
