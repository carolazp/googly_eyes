from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename  # upload photo to server
import os
import io
from PIL import Image
from process_image import process_image

# Declare name application and init
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return "Route not found"

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    """Handle image uploads and returns processed images with googly eyes."""
    if request.method == "POST":

        # Take original_picture: <input type="file" name="image" required> from index.html -> image = image from bellow
        if "image" not in request.files:
            return {"error": "No file part"}, 400

        file = request.files["image"]
        if file.filename == "":
            return {"error": "No selected file!"}, 400

        image = Image.open(file)  # Upload image

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
