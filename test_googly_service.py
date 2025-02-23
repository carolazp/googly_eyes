import pytest
import io
from PIL import Image
from googly_service import googly_service
from process_image import process_image

INPUT_IMAGE_PATH = "test_images/input.jpg"
OUTPUT_IMAGE_PATH = "test_images/output.png"

@pytest.fixture
def client():
    """Creates a test client for the Flask service."""
    googly_service.config["TESTING"] = True     # Enable test mode
    with googly_service.test_client() as client:  # Flask test client
        yield client

def test_upload_and_save_image(client):  # test1 & test3
    """Test uploading a valid JPG image and saving the processed PNG output."""
    with open(INPUT_IMAGE_PATH, "rb") as img_file:
        data = {"image": (img_file, "input.jpg")}  # Simulate file uplaod

        response = client.post("/googly_eyes", content_type="multipart/form-data", data=data)

        assert response.status_code == 200
        assert response.mimetype == "image/png"  # The response should be PNG

        # TODO: assert that there is content in the response body

        # Save the processed image
        with open(OUTPUT_IMAGE_PATH, "wb") as out_file:
            out_file.write(response.data)  # Save response image to output.png

        # Verify that the saved image is a valid PNG
        processed_img = Image.open(OUTPUT_IMAGE_PATH)
        assert processed_img.format == "PNG"    # Check file format

def test_process_image_and_save():
    """Test process_image function with a JPG input and save as PNG."""
    img = Image.open(INPUT_IMAGE_PATH)  # Open JPG input
    processed_img = process_image(img)

    assert isinstance(processed_img, Image.Image)  # Check if the output is an image

    # Save the processed image as PNG
    processed_img.save(OUTPUT_IMAGE_PATH, "PNG")  
