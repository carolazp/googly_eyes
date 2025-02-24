from flask import Flask, request, send_file
import io
from PIL import Image, UnidentifiedImageError
from process_image import process_image

# Declare and initialize the Flask
googly_service = Flask(__name__)

@googly_service.errorhandler(404)
def not_found(error):
    return "Route not found"

# Route for handling image uploads and processing
@googly_service.route("/googly_eyes", methods=["POST"])
def googly_eyes():
    """
    Handles image uploads, processes the image by adding googly eyes, and returns the processed image.

    Input:
        A POST request with a file uploaded under the form-data field 'image'.
        The supported image formats are PNG, JPG, and JPEG.
            
    Output:
        A PNG image with googly eyes added.
    """

    if "image" not in request.files:
        return {"error": "No file uploaded."}, 400

    # Retrieve the uploaded file from the request
    file = request.files["image"]

    try:
        # Open the image to ensure it's in a valid format (PNG, JPG, JPEG)
        image = Image.open(file)
        if image.format not in ["PNG", "JPG", "JPEG"]:
            return {"error": "Invalid image format. Supported formats: PNG, JPG, JPEG"}, 400

    except UnidentifiedImageError:
        # Handle invalid image format (unidentified or corrupt file)
        return {"error": "Invalid image file."}, 400


    # Modify picture
    try:
        # Apply googly eyes to the image
        processed_image = process_image(image)
    except Exception as e:
        return {"error": f"Not supported: {e}"}, 500

    # Return googly_picture
    img_io = io.BytesIO()
    processed_image.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")
