import cv2
import numpy as np

def stitch_images(images):
    
    stitcher = cv2.createStitcher() if cv2.__version__.startswith('3.') else cv2.Stitcher_create()

    (status, stitched) = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        return stitched
    else:
        print("Image stitching failed!")
        return None
