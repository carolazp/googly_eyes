from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename  # upload photo to server
import os
import io
from PIL import Image
from process_image import process_image

# Declare name application and init
googly_service = Flask(__name__)

@googly_service.errorhandler(404)
def not_found(error):
    return "Route not found"

@googly_service.route("/googly_eyes", methods=["POST"])
def googly_eyes():
    """Handle image uploads and returns processed images with googly eyes."""

        # Modify picture, Apply googly eyes: input:original_picture -> output: googly_picture = original_picture + googly_eye above
        processed_image = process_image(image)

        # Upload googly_picture # TODO: DON'T ONLY SAVE IN THE DIRECTORY, SHOW TO THE USER TOO IN THE WEB
        # THESE LINE: SAVE PROCESSED IMAGE IN MEMORY
        img_io = io.BytesIO()
        processed_image.save(img_io, format="PNG")  # Convert to bytes
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
