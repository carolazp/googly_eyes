import cv2 as cv
import numpy as np
from PIL import Image

# Load face and eye detector
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

def detect_faces(img_cv: np.ndarray):
    """
    Detects faces in the image.
    input: np.ndarray
    outpt: img_day , face
    """
    img_gray = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)  # Convert image to grayscale
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)  # List of (x, y, width, height)
    return img_gray, faces

def overlay_googly_eye(image_cv: np.ndarray, image_gray, faces, googly_eye_path="googly_eye.png"):
    """
    Overlay googly eyes on detected eyes.
    input: np.ndarray
    output: np.ndarray
    """

    googly_eye = Image.open(googly_eye_path).convert("RGBA")

    for (x, y, w, h) in faces:

        roi_gray = image_gray[y:y+h, x:x+w]  # Region Of Interest (ROI) of the face in grayscale: in order to find eyes in this Region Of the Interest where the face is in= Grayscale ROI for eye detection
        roi_color = image_cv[y:y+h, x:x+w]  # ROI of the face in color for add googly eyes later

        roi_color_pil = Image.fromarray(roi_color) # Convert ROI: from NumPy array to PIL image (for pasting later)

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=4)  # List of (x, y, width, height)

        for (ex, ey, ew, eh) in eyes:

            # Modify of the eyes #TODO: SIGHTLY RANDOMISED BOTH IN SIZE AND ORIENTATION OF THE PUPILS, here are just pasting the googly eyes into the picture
            googly_resized = googly_eye.resize((ew, eh))  # exact googly eye size, no random changes

            # Overlay googly eye onto the face
            roi_color_pil.paste(googly_resized, (ex, ey), googly_resized)  # Overlay with transparency

        image_cv[y:y+h, x:x+w] = np.array(roi_color_pil)  # Update image with modified ROI

    return image_cv


def process_image(image_pil: Image.Image):
    """
    Detects faces, finds eyes and overlays googly eyes on them.
    input: image_pill in Image.Image
    output: in Image.Image ?
    """

    image_pil = image_pil.convert("RGBA")
    image_cv = np.array(image_pil)  # Convert PIL image to OpenCV format

    image_gray, faces = detect_faces(image_cv)
    processed_image_cv = overlay_googly_eye(image_cv, image_gray, faces)

    return Image.fromarray(processed_image_cv) # Convert OpenCV format back to PIL image