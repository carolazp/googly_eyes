from flask import Flask, request, send_file
import io
from PIL import Image, UnidentifiedImageError
from process_image import process_image

# Declare name application and init
googly_service = Flask(__name__)

@googly_service.errorhandler(404)
def not_found(error):
    return "Route not found"

@googly_service.route("/googly_eyes", methods=["POST"])
def googly_eyes():
    """
    Handle image uploads and returns processed images with googly eyes.
    Input: a PNG, JPG or JPEG image sent in the form-data field "image"
    Output: a PNG file with fun eyes
    """

    if "image" not in request.files:
        return {"error": "No file uploaded."}, 400

    file = request.files["image"]

    try:
        # Open image to verify it's valid its format
        image = Image.open(file)
        if image.format not in ["PNG", "JPG", "JPEG"]:
            return {"error": "Invalid image format. Supported formats: PNG, JPG, JPEG"}, 400

    except UnidentifiedImageError:
        return {"error": "Invalid image file."}, 400

    # Modify picture, Apply googly eyes: input:original_picture -> output: googly_picture = original_picture + googly_eye above
    try:
        processed_image = process_image(image)
    except Exception as e:
        return {"error": f"Not supported: {e}"}, 500

    # Return googly_picture
    img_io = io.BytesIO()
    processed_image.save(img_io, format="PNG")  # Convert to bytes
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")
