# googly_eyes
This repository contains the Googly Eyes service, a technical exercise for Onfido. The service allows users to upload a photo, processes it by replacing eyes with randomized googly eyes, and returns the modified image.

The service itself does not save any image. As a consequence, for testing purpose, the image is received and saved as input for the test. The output image, after processing, is also saved for visual inspection during testing.

## Instalation
TODO: use Poetry
```bash
pip install -r requirements.txt
```

## Usage

Run the service localy:
```bash
flask --app googly_service run
```

Running the Test
```bash
pytest -v test_googly_service.py
```
## Input
input.jpg    : standar picture  \
input_pdf.jpg: document.pdf renamed as input_pdf.jpg (corrupted .jpg file)


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


## Results
Before: \
![Alt text](test/resources/input_images/input.jpg)


After:\
![Alt text](test/resources/output_images/output_jpg.png)


Have fun!
