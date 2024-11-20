# waapi-tools

This repository is a collection of tools to be used inside Audiokinetic Wwise. The tools use WAAPI (Wwise Authoring API) and Python to perform several automated tasks.

Refer to **General Setup Instructions** below, then find the specific instructions README.md in the sub-folders.

## Requirements
* Python 3.6+
* Running instance of Wwise.exe with the Wwise Authoring API enabled (Project > User Preferences... > Enable Wwise Authoring API)
* **waapi-client** python project installed

## General Setup Instructions

We recommend to use the Python Launcher for Windows which is installed with Python 3 from python.org.

### Install Python 3.6

* Install Python 3.6 or greater from: https://www.python.org/downloads/

### Install waapi-client

* **Windows**: `py -3 -m pip install waapi-client scipy`
* **Other platforms**: `python3 -m pip install waapi-client scipy`

Additional instructions can be found at:
https://pypi.org/project/waapi-client/
