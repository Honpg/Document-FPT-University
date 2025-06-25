import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import matplotlib.image as mi
from sklearn.cluster import KMeans
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def snake_al(img):

    edges = cv2.Canny(img, threshold1=30, threshold2=100)

    kernel = np.ones((10, 10), np.uint8)
    expanded_edges = cv2.dilate(edges, kernel, iterations=1)
    contours, _ = cv2.findContours(expanded_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        initial_contour = contours[0][:, 0, :].astype(float)
    else:
        initial_contour = None

    snake = active_contour(gaussian(img, 3, preserve_range=False),
                        initial_contour, alpha=0.015, beta=10, gamma=0.001)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(img, cmap=plt.cm.gray)
    ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])
    plt.show()

def mean_shift(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    data_points = lab_image.reshape(-1, 3)
    def mean_shift(data_points, bandwidth, num_iterations):
        for _ in range(num_iterations):
            shifted_points = []
            for point in data_points:
                in_bandwidth = np.linalg.norm(data_points - point, axis=1) < bandwidth
                shift = np.mean(data_points[in_bandwidth] - point, axis=0)
                new_point = point + shift
                shifted_points.append(new_point)
            data_points = np.array(shifted_points)
        return data_points
    bandwidth = 10 
    num_iterations = 5 

    segmented_data = mean_shift(data_points, bandwidth, num_iterations)
    segmented_image = segmented_data.reshape(lab_image.shape)
    segmented_image_bgr = cv2.cvtColor(segmented_image, cv2.COLOR_Lab2BGR)
    cv2.imshow("Segmented Image", segmented_image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def watershed(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradient = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)
    gradient = np.uint8(np.absolute(gradient))

    ret, markers = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    markers = cv2.connectedComponents(markers)[1]
    cv2.watershed(image, markers)
    image[markers == -1] = [0, 0, 255]
    cv2.imshow("Segmented Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def k_mean(img):
    X = img.reshape(img.shape[0]*img.shape[1],img.shape[2])
    for K in [3]:
        kmeans = KMeans(n_clusters=K).fit(X)
        label=kmeans.predict(X)
        img2 = np.zeros_like(X)
        for k in range(K):
            img2[label==k]=kmeans.cluster_centers_[k]
        img3 = img2.reshape((img.shape[0],img.shape[1],img.shape[2]))
        plt.imshow(img3,interpolation='nearest')
        plt.axis('off')
        plt.show()
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
    button_frame, text="Snake_al", command=lambda: snake_al(img=original_image)
)
gray_button.pack(side="left", padx=10)

histogram_button = tk.Button(
    button_frame, text="K_mean", command=lambda: k_mean(img=original_image)
)
histogram_button.pack(side="left", padx=10)
histogram_button = tk.Button(
    button_frame, text="watershed", command=lambda: watershed(image=original_image)
)
histogram_button.pack(side="left", padx=10)
histogram_button = tk.Button(
    button_frame, text="mean_shift", command=lambda: mean_shift(image=original_image)
)
histogram_button.pack(side="left", padx=10)

image_label = tk.Label(app)
image_label.pack()
app.mainloop()