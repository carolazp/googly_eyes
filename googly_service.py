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
    Input: any image format (PNG, JPG)
    Output: always PNG file
    """

    if "image" not in request.files:
        return {"error": "No file uploaded."}, 400

    file = request.files["image"]
    if file.filename == "":
        return {"error": "No selected file."}, 400

    try:
        # Open image to verify it's valid its format
        image = Image.open(file)

        if image.format not in ["PNG", "JPG"]:
            return {"error": "Invalid image format. Supported formats: PNG, JPG"}, 400

    except UnidentifiedImageError:
        return {"error": "Invalid image file."}, 400


    # Modify picture, Apply googly eyes: input:original_picture -> output: googly_picture = original_picture + googly_eye above
    processed_image = process_image(image)

    # Upload googly_picture # TODO: DON'T ONLY SAVE IN THE DIRECTORY, SHOW TO THE USER TOO IN THE WEB
    # THESE LINE: SAVE PROCESSED IMAGE IN MEMORY
    img_io = io.BytesIO()
    processed_image.save(img_io, format="PNG")  # Convert to bytes
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")
