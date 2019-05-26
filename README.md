# Simple mp3-converter 

## General info
This project is simple mp3-converter , analog of https://www.onlinevideoconverter.com/mp3-converter. Paste link of your video in the form and download mp3 file.

## REQUIREMENTS

This App Uses Python 3.6, Django 2.2.1, youtube-dl.

## INSTALLATION

To clone and run this repository, you'll need Git installed on your computer. I used virtualenv for this project, you may feel free to use the same. From your command line:

```
$ git clone https://github.com/GarryGon4ar/mp3-converter.git
$ python3 -m venv sample_environment
$ source sample_environment/bin/activate
$ cd mp3-converter
$ pip install -r requirements.txt
$ python manage.py runsever