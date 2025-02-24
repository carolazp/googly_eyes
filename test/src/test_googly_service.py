import pytest
import os
from PIL import Image
import sys

# Add the 'service/src' directory to the Python path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../service/src'))
)
# Import the googly_service module
from googly_service import googly_service


# Inputs paths for images files
INPUT_IMAGE_PNG_PATH = os.path.join("test", "resources", "input_images", "input.png")
INPUT_IMAGE_JPG_PATH = os.path.join("test", "resources", "input_images", "input.jpg")
INPUT_PDF_PATH = os.path.join("test", "resources", "input_images", "input.pdf")
INPUT_IMAGE_GIF_PATH = os.path.join("test", "resources", "input_images", "input.gif")
INPUT_IMAGE_NO_EYES_PATH = os.path.join("test", "resources", "input_images", "input_no_eyes.png")

# Output directory where processed images will be saved
OUTPUT_DIR = os.path.join("test", "resources", "output_images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

@pytest.fixture
def client():
    """Creates a test client for the Flask service."""
    googly_service.config["TESTING"] = True          # Enable test mode
    with googly_service.test_client() as client:     # Flask test client
        yield client

def save_output_image(response_data, filename):
    """Saves processed image data to a specified file path."""
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "wb") as out_file:
        out_file.write(response_data)
        return output_path

def test_png_to_png(client):  # Test1
    """Test uploading a valid PNG image and serving a processed PNG as output."""
    with open(INPUT_IMAGE_PNG_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.png")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG (header)
        assert response.data  # Ensure the response body contains data

        # Save and verify the processed image
        output_path = save_output_image(response.data, "output_png.png")
        processed_img = Image.open(output_path)
        assert processed_img.format == "PNG"    # Check file format


def test_jpg_to_png(client):  # test2
    """Test uploading a valid JPG image and serving the processed PNG as output."""
    with open(INPUT_IMAGE_JPG_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.jpg")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG (header)
        assert response.data  # Ensure the response body contains data

        # Save and verify the processed image
        output_path = save_output_image(response.data, "output_jpg.png")
        processed_img = Image.open(output_path)
        assert processed_img.format == "PNG"    # Check file format


def test_no_eyes(client):  # test1.1
    """Test uploading a PNG image with no eyes and serving the processed PNG as output."""
    with open(INPUT_IMAGE_NO_EYES_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.png")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG (header)
        assert response.data    # Ensure the response body contains data

        # Save and verify the processed image
        output_path = save_output_image(response.data, "output_no_eyes.png")
        processed_img = Image.open(output_path)
        assert processed_img.format == "PNG"    # Check file format

def test_pdf_error(client):  # test3
    """Test uploading an invalid PDF document, expecting an error response."""
    with open(INPUT_PDF_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.pdf")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 400


def test_gif_error(client):  # test5
    """Test uploading an invalid GIF image, expecting an error response."""
    with open(INPUT_IMAGE_GIF_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.gif")}
        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 400


def test_get_error(client):  # test4
    """Test a GET request to the /googly_eyes endpoint, expecting a 405 Method Not Allowed error."""
    response = client.get("/googly_eyes")

    assert response.status_code == 405  # Expect "Method Not Allowed" for GET resquests
