import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
import math
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from skimage import exposure
from skimage.feature import hog


def cv2_to_tkinter(image):
    b, g, r = cv2.split(image)
    image = cv2.merge((r, g, b))
    return ImageTk.PhotoImage(image=Image.fromarray(image))


def import_and_display_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    if file_path:
        global original_image
        original_image = cv2.imread(file_path)
        img_tk = cv2_to_tkinter(original_image)
        image_label.config(image=img_tk)
        image_label.image = img_tk


def harris_corner_detector(image, threshold=0.5, harris=0.04):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    Ix = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Iy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    Ixx = Ix**2
    Ixy = Ix * Iy
    Iyy = Iy**2
    kernel_size = 3
    Ixx = cv2.GaussianBlur(Ixx, (kernel_size, kernel_size), 0)
    Ixy = cv2.GaussianBlur(Ixy, (kernel_size, kernel_size), 0)
    Iyy = cv2.GaussianBlur(Iyy, (kernel_size, kernel_size), 0)
    det_M = Ixx * Iyy - Ixy**2
    trace_M = Ixx + Iyy
    R = det_M - harris * (trace_M**2)
    corners = np.where(R > threshold * R.max()) 
    return list(zip(corners[1], corners[0]))


def Haris_dis(image):
    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    corners = harris_corner_detector(image)
    for x, y in corners:
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Harris Corners")
    plt.show()


def HOG_dis(image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    hog_features, hog_image = hog(
        gray_image, pixels_per_cell=(8, 8), block_norm="L2-Hys", visualize=True
    )
    hog_image = exposure.rescale_intensity(hog_image, in_range=(0, 10))
    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.subplot(122)
    plt.imshow(hog_image, cmap="gray")
    plt.title("HOG Image")
    plt.show()


def Candy_dis(image):
    edges = cv2.Canny(image, 100, 200)
    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.subplot(122)
    plt.imshow(edges, cmap="gray")
    plt.title("Canny")
    plt.show()


def Hough(src):
    dst = cv2.Canny(src, 50, 200, None, 3)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

    linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)

    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.imshow((cv2.cvtColor(src, cv2.COLOR_BGR2RGB)))
    plt.title("Original")
    plt.subplot(122)
    plt.imshow(cdstP)
    plt.title("Hough line")
    plt.show()

    return 0


app = tk.Tk()
app.title("RGB Editor")

original_image = None


button_frame = tk.Frame(app)
button_frame.pack(side="top", pady=10)

import_button = tk.Button(
    button_frame, text="Import Image", command=import_and_display_image
)
import_button.pack(side="left", padx=10)

gray_button = tk.Button(
    button_frame, text="Haris_dis", command=lambda: Haris_dis(image=original_image)
)
gray_button.pack(side="left", padx=10)

histogram_button = tk.Button(
    button_frame, text="HOG", command=lambda: HOG_dis(image=original_image)
)
histogram_button.pack(side="left", padx=10)

mean_button = tk.Button(
    button_frame, text="Canny", command=lambda: Candy_dis(image=original_image)
)
mean_button.pack(side="left", padx=10)

median_button = tk.Button(
    button_frame, text="Hough", command=lambda: Hough(src=original_image)
)
median_button.pack(side="left", padx=10)

image_label = tk.Label(app)
image_label.pack()

app.mainloop()