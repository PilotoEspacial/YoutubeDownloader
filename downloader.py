#bin/python3

from pytube import YouTube
import os
import subprocess
import time

while True:
    url = input("URL: ")

    # Title and Time
    print("...")

    # Filename specification
    # Prevents any errors during conversion due to illegal characters in name
    _filename = input("Filename: ")

    # Downloading
    print("Downloading....")
    YouTube(url).streams.first().download(filename=_filename)
    time.sleep(1)

    # Converting
    mp4 = "'%s'.mp4" % _filename
    mp3 = "'%s'.mp3" % _filename
    ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
    subprocess.call(ffmpeg, Shell=True)

    # Completion
    print("\nCOMPLETE\n")
