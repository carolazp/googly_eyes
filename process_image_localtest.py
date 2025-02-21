import cv2 as cv
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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
        # MOdification of the eyes: TODO
        googly_resized = googly_eye.resize((w, h))  # exact eye size, no random changes

        # Overlay on the face
        image_pil.paste(googly_resized, (x, y), googly_resized)  # overaly with transparency

    return image_pil


def process_image(image_path):
    """Detect eyes and overlays googly eyes on the image."""
    image_cv = cv.imread(image_path)  # load with opencv
    image_pil = Image.fromarray(cv.cvtColor(image_cv, cv.COLOR_BGR2RGB))  # convert to PIL

    eyes = detect_eyes(image_cv)
    output_image = overlay_googly_eye(image_pil, eyes)

    return output_image


# --- TEST
face_image_path = "face.jpg"
output = process_image(face_image_path)

# Show result
plt.imshow(output)
plt.axis("off")
plt.show()

# Save output
output.save("googly_face.png")