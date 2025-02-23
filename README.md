# googly_eyes
This repository contains the Googly Eyes web service, a technical exercise for Onfido. The service allows users to upload a photo, processes it by replacing eyes with randomized googly eyes, and returns the modified image.

```bash
pip install -r requirements.txt
```

Run the service localy:
```bash
flask --app googly_service run
```

TODO: slightly randomised both in size and orientation of the **pupils**
