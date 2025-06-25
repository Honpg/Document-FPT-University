import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from stitch import stitch_images

def main(image_paths):
    # Read the images
    images = []
    for image_path in image_paths:
        image = cv2.imread(image_path)
        images.append(image)

    # Stitch the images
    result = stitch_images(images)

    if result is not None:
        # Display the stitched image
        cv2.imshow("Stitched Image", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image stitching failed!")

def import_images():
    global file_paths
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_paths:
        file_paths = list(file_paths)
        
def cv2_to_tkinter(image):
    b, g, r = cv2.split(image)
    image = cv2.merge((r, g, b))
    return ImageTk.PhotoImage(image=Image.fromarray(image))
def print1(image_paths):
    print(image_paths)

app = tk.Tk()
app.title("Image Stitching App")

original_images = []

button_frame = tk.Frame(app)
button_frame.pack(side="top", pady=10)
import_button = tk.Button(
    button_frame, text="Import Images", command=import_images)
import_button.pack(side="left", padx=10)

stitch_button = tk.Button(
    button_frame, text="Stitch Images", command=lambda: main(image_paths=file_paths))
stitch_button.pack(side="left", padx=10)

image_label = tk.Label(app)
image_label.pack()

app.mainloop()
