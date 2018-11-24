# UART
A program for randomly choosing an art reference.

## Description
It is a basic Qt desktop application that opens a random image based on a list of folders provided. Unlike some applications, it will recursively search folders for images. 
I built it primarily for personal use and thought someone might find it handy. I plan on expanding it later to be more like QuickPoses' figure drawing application. 


## Screenshots 

![UART Screenshot](https://i.imgur.com/POPBmUj.png "")

## How to Build 
The build process was done by following this [tutorial](https://build-system.fman.io/python-qt-tutorial). If this doesn't work you can 
refer to this. 

To summarize:

Clone this repository to your computer and change directory into it.

Create a virtual environment
`python -m venv virtualenv`

Turn on the virtualenvironment
`call virtualenv\scripts\activate.bat`

Install PySide2 (You may need to prefix this with python -m on Windows)
`pip install PySide2`

Install the build tools FBS and PyInstaller
`pip install fbs PyInstaller==3.4`

Run it (optional)
`fbs run`

Build it 
`fbs freeze` or if you want to debug it `fbs freeze --debug`










