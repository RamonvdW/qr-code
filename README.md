# QR-code

Need to setup an OTP application that does not support manual entry (like FreeOTP)?
With this small Django project you can re-create the QR code.

## Installation instructions:

- Tested on Linux (Debian11) with Python 3.9.2

- Create a venv:
```
$ python3 -m venv qrcode-venv
$ cd qrcode-venv
$ source bin/activate
```

- Clone the project files
```
$ git clone https://github.com/RamonvdW/qr-code.git
```

- Install the pip packages
```
$ pip install pip -U
$ pip install pip-tools -U
$ pip-sync qr-code/django_proj/requirements/requirements.txt
```

- Run the application:
```
$ cd qr-code
$ chmod +x ./run.sh ./manage.py
$ ./run.sh
```

- Point your local browser to localhost:8000
  Fill in the fields and press Update to get a new QR code

For questions, you can contact me on this gmail: nhb.ramonvdw
You may find that some comments are in Dutch.
