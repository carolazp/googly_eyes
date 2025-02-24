import cv2 as cv
import numpy as np
from PIL import Image

# Load face and eye detector using OpenCV's pre-trained Haar cascades
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")


def detect_faces(img_cv: np.ndarray):
    """
    Detects faces in the provided image using OpenCV's Haar cascade classifier.

    Args:
        img_cv (np.ndarray): The input image in NumPy array format (OpenCV style).

    Returns:
        - img_gray (np.ndarray): Grayscale version of the input image.
        - faces (list): A list of faces detected, each represented by a tuple (x, y, width, height).
    """
    img_gray = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    return img_gray, faces


def overlay_googly_eye(image_cv: np.ndarray, image_gray: np.ndarray, faces: list):
    """
    Overlays googly eyes onto the detected faces in the image.

    Args:
        image_cv (np.ndarray): The input image in OpenCV style (color image).
        image_gray (np.ndarray): Grayscale version of the input image used for eye detection.
        faces (list): A list of faces detected, each represented by a tuple (x, y, width, height).

    Returns:
        image_cv (np.ndarray): The processed image with googly eyes overlaid.
    """

    for (x, y, w, h) in faces:

        roi_gray = image_gray[y:y+h, x:x+w]  # Region Of Interest (ROI) of the face in grayscale: in order to find eyes in this Region Of the Interest where the face is in= Grayscale ROI for eye detection

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=4)  # List of (x, y, width, height)

        for (ex, ey, ew, eh) in eyes:

            # Add googly eyes: size and orientation of the pupils
            center = (x + ex + ew//2, y + ey + eh//2)
            radius = ew // 2

            # White eye
            cv.circle(image_cv, center, radius, (255, 255, 255), -1)

            # Black pupil
            pupil_offset = np.random.randint(-radius//3, radius//3)  # Random pupil position (orientation)
            pupil_size = np.random.randint(radius//2, radius)     # Random pupil size
            cv.circle(img=image_cv,
                        center=(center[0] + pupil_offset, center[1] + pupil_offset),
                        radius=pupil_size,
                        color=(0, 0, 0),
                        thickness= -1)

    return image_cv


def process_image(image_pil: Image.Image):
    """
    Processes the input image by detecting faces, detecting eyes, and overlaying googly eyes on the faces.

    Args:
        image_pil (Image.Image): The input image in PIL Image format.

    Returns:
        Image.Image: The processed image with googly eyes overlayed, in PIL Image format.
    """

    image_pil = image_pil.convert("RGB")
    image_cv = np.array(image_pil)  # Convert PIL image to OpenCV format

    image_gray, faces = detect_faces(image_cv)
    processed_image_cv = overlay_googly_eye(image_cv, image_gray, faces)

    return Image.fromarray(processed_image_cv) # Convert OpenCV format back to PIL image
