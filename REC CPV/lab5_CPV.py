import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def align_images_ransac(image1, image2, ransac_reproj_thresh=3.0):

    detector = cv2.ORB_create()
    keypoints1, descriptors1 = detector.detectAndCompute(image1, None)
    keypoints2, descriptors2 = detector.detectAndCompute(image2, None)

    # Feature matching using a Brute-Force matcher
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)

    # Apply RANSAC to find the best homography
    if len(matches) >= 4:
        src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # Use RANSAC to estimate the homography
        H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, ransac_reproj_thresh)

        # Warp image1 onto image2
        aligned_image = cv2.warpPerspective(image1, H, (image2.shape[1], image2.shape[0]))

        # Draw lines between matching features on the aligned image
        matching_image = cv2.drawMatches(image1, keypoints1, aligned_image, keypoints2, matches, None)

        return aligned_image, matching_image
    else:
        print("Feature detection didn't yield enough matches for alignment.")
        return None, None

def RANSAC_run(image1,image2):
    aligned_image, matching_image = align_images_ransac(image1, image2)
    if aligned_image is not None:
        plt.figure(figsize=(12, 6))
        plt.imshow(cv2.cvtColor(matching_image, cv2.COLOR_BGR2RGB))
        plt.title("RANdom SAmple Consensus")
        plt.axis('off')
        plt.show()

def cv2_to_tkinter(image):
    b, g, r = cv2.split(image)
    image = cv2.merge((r, g, b))
    return ImageTk.PhotoImage(image=Image.fromarray(image))


def import_and_display_image1():
    file_path1 = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path1:
        global original_image1
        original_image1 = cv2.imread(file_path1)
        img_tk = cv2_to_tkinter(original_image1)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        
def import_and_display_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
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
    button_frame, text="Import Image original", command=import_and_display_image1)
import_button.pack(side="left", padx=10)
import_button = tk.Button(
    button_frame, text="Import Image taget", command=import_and_display_image)
import_button.pack(side="left", padx=10)

histogram_button = tk.Button(
    button_frame, text="RANSAC", command=lambda: RANSAC_run(image1=original_image1, image2=original_image))
histogram_button.pack(side="left", padx=10)
image_label = tk.Label(app)
image_label.pack()
app.mainloop()