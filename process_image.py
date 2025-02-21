import cv2 as cv
import numpy as np
from PIL import Image

# Load eye detector
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')


def detect_eyes(image: np.ndarray):
    """Detects eyes in the image."""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    return eyes  # list of (x,y,width, height)


def overlay_googly_eye(image_pil: Image.Image, eyes, googly_eye_path="googly_eye.png"):
    # TODO: SIGHTLY RANDOMISED BOTH IN SIZE AND ORIENTATION OF THE PUPILS!
    """Overlay googly eyes on detected eyes."""
    googly_eye = Image.open(googly_eye_path).convert("RGBA")
    image_pil = image_pil.convert("RGBA")

    for (x, y, w, h) in eyes:
        # Modify of the eyes: TODO
        googly_resized = googly_eye.resize((w, h))  # exact eye size, no random changes

        # Overlay on the face
        image_pil.paste(googly_resized, (x, y), googly_resized)  # overly with transparency

    return image_pil


def process_image(image_pil: Image.Image):
    """Detect eyes and overlays googly eyes on the image."""
    image_cv = np.array(image_pil)  # convert to OpeCV format numpy.array
    eyes = detect_eyes(image_cv)
    return overlay_googly_eye(image_pil, eyes)
