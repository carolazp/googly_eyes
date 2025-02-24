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
/googly_eyes

│── googly_service.py          # Flask service                      \
│── process_image.py           # Function that adds googly eyes     \
│── test_googly_service.py     # PyTest file for testing the googly service \
│── test_images/                                                    \
│   ├── input.jpg              # Input image (original)             \
│   ├── output.png             # Output image (processed)           \
│── requirements.txt       # Dependencies


## Results
Before: \
![Alt text](test_images/input.jpg)


After:\
![Alt text](test_images/output_images/output_jpg.png)

Have fun!
