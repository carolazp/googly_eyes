import pytest
import io
import os
from PIL import Image
from googly_service import googly_service
from process_image import process_image

# Inputs paths
INPUT_IMAGE_PNG_PATH = "test_images/input.png"
INPUT_IMAGE_JPG_PATH = "test_images/input.jpg"
INPUT_PDF_PATH = "test_images/input.pdf"
INPUT_IMAGE_GIF_PATH = "test_images/input.gif"
INPUT_IMAGE_NO_EYES_PATH = "test_images/input_no_eyes.png"

# Output directory
OUTPUT_DIR = "test_images/output_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_IMAGE_PATH = "test_images/output.png"

@pytest.fixture
def client():
    """Creates a test client for the Flask service."""
    googly_service.config["TESTING"] = True          # Enable test mode
    with googly_service.test_client() as client:     # Flask test client
        yield client

def save_output_image(response_data, filename):
    """Saves processed images from response data."""
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "wb") as out_file:
        out_file.write(response_data)
        return output_path

def test_png_to_png(client):  # test1
    """ Test upload a valid PNG image as input and serve the processed PNG as output."""

    with open(INPUT_IMAGE_PNG_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.png")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG (header)
        assert response.data  # if there any content in the body? True; no response: empty-> False

        # Save the processed image
        output_path = save_output_image(response.data, "output_png.png")

        # Verify output is a PNG
        processed_img = Image.open(output_path)
        assert processed_img.format == "PNG"    # Check file format


def test_jpg_to_png(client):  # test2
    """ Test upload a valid JPG image as input and serve the processed PNG as output."""

    with open(INPUT_IMAGE_JPG_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.jpg")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG (header)
        assert response.data  # if there any content in the body? True; no response: empty-> False

         # Save processed image
        output_path = save_output_image(response.data, "output_jpg.png")

        # Verify output is a PNG
        processed_img = Image.open(output_path)
        assert processed_img.format == "PNG"    # Check file format


def test_no_eyes(client):  # test1.1
    """ Test upload a valid PNG image as input and serve the processed PNG as output."""

    with open(INPUT_IMAGE_NO_EYES_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.png")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG (header)
        assert response.data  # if there any content in the body? True; no response: empty-> False

        # Save the processed image
        output_path = save_output_image(response.data, "output_no_eyes.png")

        # Verify output is a PNG
        processed_img = Image.open(output_path)
        assert processed_img.format == "PNG"    # Check file format

def test_pdf_error(client):  # test3
    """ Test upload an invalid PDF document as input."""

    with open(INPUT_PDF_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.pdf")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 400


def test_gif_error(client):  # test5
    """ Test upload an invalid GIF image as input."""

    with open(INPUT_IMAGE_GIF_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.gif")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 400


def test_get_error(client):  # test4
    """Test that a GET request to the endpoint returns 405 Method Not Allowed."""

    response = client.get("/googly_eyes")

    assert response.status_code == 405  # Expect "Method Not Allowed"
