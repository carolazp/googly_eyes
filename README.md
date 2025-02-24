# googly_eyes
This repository contains the Googly Eyes service, a technical exercise for Onfido. 
The service is implemented as an HTTP POST endpoint receiving the image and replacing the existing eyes with randomized googly eyes.


## File Structure
/googly_eyes                                                            \
│── service/                     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       # The core service                       \
│   ├── src/                     &emsp;&emsp;&emsp;                       # Source code for the service             \
│       ├── googly_service.py    &emsp;&emsp;&emsp;                       # Core Flask service logic for adding googly eyes \
│       ├── process_image.py     &emsp;&emsp;&emsp;                       # Image processing functions that add googly eyes \
│── test/                        &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       # Test files and resources               \
│   ├── resources/               &emsp;&emsp;&emsp;                       # Input and output images for testing    \
│       ├── input_images/        &emsp;&emsp;&emsp;                       # Sample input images                    \
│       ├── output_images/       &emsp;&emsp;&emsp;                       # Expected output images after processing\
│   ├── src/                     &emsp;&emsp;&emsp;                       # Test scripts                            \
│       ├── test_googly_service.py&emsp;&emsp;&emsp;                       # Integration tests for the service      \
│── requirements.txt             &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       # Python dependencies                    \
│── .gitignore                   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       # Git ignore file                        \
│── README.md                    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       # This README file                       \


## Installation

Install Python version 3.11.2.
Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the service:
- Start the Flask development server with the following command:
```bash
flask --app service/src/googly_service run
```
or
Run the tests:

- If using `pytest` directly (from the root of the project googly_eyes):
```bash
pytest
```


## Tests

The tests have been designed to ensure the functionality of the Googly Eyes service. For testing purposes, input images are provided and saved, and after processing, the output images are saved for visual verification.

The `test` directory is organized into two main subdirectories: `resources` and `src`.

- **`resources` directory**:\
Contains all the necessary resources for the test, including input images and a folder for output images.
    - `input_images/`: Stores the images used as input for the test.
    - `output_images/`: Stores the processed images that are generated as the test output.

- **`src` directory**:\
Contains the test script that runs the tests for the Googly Eyes service.
    - `test_googly_service.py`: The script that tests the functionality of the Googly Eyes service.

### Test Process

1. Input images are loaded from the `input_images` folder.
2. The Googly Eyes service processes these images.
3. The processed output is saved in the `output_images` folder.
4. The output images can be visually inspected to verify the service's correctness.

input_pdf.jpg: document.pdf renamed as input_pdf.jpg (corrupted .jpg file)

### Test Breakdown

Each test below focuses on different scenarios for the Googly Eyes service:

- **`test_png_to_png`**: 
  - **Input**: `input.png` (PNG format) with a face.
  - **Purpose**: Tests the service's ability to handle PNG images.
  - **What it does**: Uploads a valid PNG image, processes it, and checks if the output is also a valid PNG image.
  - **Assertion**: Confirms the status code is `200`, the response mimetype is `image/png`, and the output format is `PNG`.

- **`test_jpg_to_png`**: 
  - **Input**: `input.jpg` (JPG format) with four faces.
  - **Purpose**: Tests the service's handling of JPG images.
  - **What it does**: Uploads a valid JPG image, processes it, and checks if the output is also a valid PNG image.
  - **Assertion**: Confirms the status code is `200`, the response mimetype is `image/png`, and the output format is `PNG`.

- **`test_no_eyes`**: 
  - **Input**: `input_no_eyes.png` (PNG format) without any eyes.
  - **Purpose**: Tests the service's ability to process an image without eyes.
  - **What it does**: Uploads a PNG image without googly eyes and checks if the service still processes it correctly.
  - **Assertion**: Confirms the status code is `200`, the response mimetype is `image/png`, and the output format is `PNG`.

- **`test_pdf_error`**:
  - **Input**: `input.pdf` (PDF format).
  - **Purpose**: Ensures that files without images, like PDFs, are handled properly.
  - **What it does**: Uploads a PDF file and expects the service to return an error (`400 Bad Request`).
  - **Assertion**: Confirms the status code is `400`, indicating the service rejects unsupported file formats.

- **`test_gif_error`**:  (GIF format).
  - **Input**: `input.gif` input in format GIT
  - **Purpose**: Tests the service's response to unsupported image files.
  - **What it does**: Uploads a GIF file and expects the service to reject it with an error (`400 Bad Request`).
  - **Assertion**: Confirms the status code is `400`, indicating the service does not accept GIF files.

- **`test_get_error`**: 
  - **Purpose**: Ensures the service rejects GET requests to the `/googly_eyes` endpoint.
  - **What it does**: Sends a GET request to the `/googly_eyes` endpoint and expects a `405 Method Not Allowed` error.
  - **Assertion**: Confirms the status code is `405`, indicating that GET requests are not allowed at this endpoint.



## Results
Before: \
![Alt text](test/resources/input_images/input.jpg)


After:\
![Alt text](test/resources/output_images/output_jpg.png)


Have fun!
