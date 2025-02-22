import cv2 as cv
import numpy as np
from PIL import Image

# Load face and eye detector
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

def detect_faces(img_cv: np.ndarray):
    """Detects in the image."""
    img_gray = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)  # convert color to gray
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    return img_gray, faces  # list of (x,y,width, height)

def overlay_googly_eye(image_pil: Image.Image, image_cv: np.ndarray, image_gray, faces, googly_eye_path="googly_eye.png"):
    """Overlay googly eyes on detected eyes."""

    googly_eye = Image.open(googly_eye_path).convert("RGBA")
    image_pil = image_pil.convert("RGBA")

    for (x, y, w, h) in faces:
        cv.rectangle(image_cv, (x,y), (x+w, y+h), (255,0,0,2))  # draw a rectangule around the face

        roi_gray = image_gray[y:y+h, x:x+w]  # the region of the face: # we will find eyes in the Region Of the Image where the face is in. REGION OF IMAGE IN GRAY
        roi_color = image_cv[y:y+h, x:x+w]  # the same as before but in color for reposting

        roi_color_pil = Image.fromarray(roi_color) # Convert ROI mumpy array to PIL for pasting

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=4) # list of (x,y,width, height)

        for (ex, ey, ew, eh) in eyes:

            # Modify of the eyes: TODO: SIGHTLY RANDOMISED BOTH IN SIZE AND ORIENTATION OF THE PUPILS! , here are just pasting the googly eyes into the picture
            googly_resized = googly_eye.resize((ew, eh))  # exact googly eye size, no random changes

            # Overlay on the face
            roi_color_pil.paste(googly_resized, (ex, ey), googly_resized)  # overly with transparency

        image_cv[y:y+h, x:x+w] = np.array(roi_color_pil) # to analyze all the picture and not stay in just one face

    return image_cv


def process_image(image_pil: Image.Image):
    """Detect eyes and overlays googly eyes on the image."""
    image_cv = np.array(image_pil)  # convert PIL image to OpeCV format

    image_gray, faces = detect_faces(image_cv)
    processed_image_cv = overlay_googly_eye(image_pil, image_cv, image_gray, faces)

    return Image.fromarray(processed_image_cv) # convert Opencv format back to PIL image