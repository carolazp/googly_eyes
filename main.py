from flask import Flask, render_template, request
from werkzeug.utils import secure_filename # upload photo to server
import os

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
    if request.method == "POST":
        # Take original_picture: <input type="file" name="image" required> from index.html -> image = image from bellow
        image = request.files["image"]
        basepath = os.path.dirname(__file__)
        print(basepath)

        # Modify picture: TODO input:original_picture -> output: googly_picture = original_picture + googly_eye above
        filename = secure_filename(image.filename)
        extension = os.path.splitext(filename)[1]
        new_name_file = "123" + extension

        # Upload googly_picture # TODO: DON'T ONLY SAVE IN THE DIRECTORY, SHOW TO THE USER TOO IN THE WEB
        upload_path = os.path.join(basepath, "static/archive_googlyeyes", new_name_file)
        image.save(upload_path)

        return "<br><br><center> Done and Have fun!</center>"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
