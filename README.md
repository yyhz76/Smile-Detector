# Smile-Detector
Detecting if a person is smiling in a video

## Algorithm Outline
* Find the lip coordinates using dlib facial landmark detection.
* For a person to be smiling, the ratio of lip width and height should be high.
* Return True if the ratio is higher than a preset threshold, else return False.

## Video Demo
https://youtu.be/ktJof-SPsQI
