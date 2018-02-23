# flask_platform
This is a flask app that uses a module named "systeminfo".

## Purpose:
The purpose of this app is to demonstrate the use of the system info package. The system info package runs the platform.platform() method to display information about the local OS platform.

The requirements.txt file details all package requirements for this flask app.

## Requirements:
See the requirements.txt file for a list of Python package requirements that can be installed using the pip command.

Systeminfo can be installed by using following bash command:
`pip install git+https://github.com/thanders/systeminfo\_a2.git`

## How to install flask_platform?

1. Install all required packages.
2. Clone the flask_platform Github repository:
`git clone https://github.com/thanders/flask_platform.git`
3. Change your machine's present working directory (PWD) to flask_platform folder.
4. Type the following commands: `export FLASK_APP=run.py` and then `python -m flask run

You should see:
![Flask_platform running](https://github.com/thanders/flask_platform/images/flask_platform_on_ec2.png "Flask platform_running")

`## How to uninstall flask_platform?
Delete the flask_platform directory and the installed required packages:
Type `rm -rf flask_platform` when your PWD is the parent folder


