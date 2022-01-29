# 1. Find the lip coordinates using the facial landmarks.
# 2. For a person to be smiling, the ratio of lip width and height should be high.
# 3. Return `True` if a smile is detected, else return `False`.


import cv2
import dlib
import numpy as np

# initialize dlib's face detector 
detector = dlib.get_frontal_face_detector()

# initialize the facial landmark predictor
shape_predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")


def smile_detector(imDlib):
    faces = detector(imDlib, 0)
    
    if len(faces):
        landmarks = shape_predictor(imDlib, faces[0])
    else:
        return False
    
    isSmiling = False

    leftLip = landmarks.parts()[48].x
    rightLip = landmarks.parts()[54].x

    upperLip = landmarks.parts()[51].y
    lowerLip = landmarks.parts()[8].y

    # the criterion for smile detection
    if ((rightLip - leftLip) / (lowerLip - upperLip) > 1.21):
        isSmiling = True
    
    return isSmiling


if __name__ == "__main__":
    # Initializing webcam capture object.
    capture = cv2.VideoCapture(0)

    if(False == capture.isOpened()):
        print("[ERROR] Webcam not opened properly")    
        
    frame_number = 0
    smile_frames = []

    while (True):
        # grab the next frame
        isGrabbed, frame = capture.read()
        if not isGrabbed:
            break
            
        imDlib = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_has_smile = smile_detector(imDlib)

        if (True == frame_has_smile):
            cv2.putText(frame, "Smiling :)", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
            smile_frames.append(frame_number)

        cv2.imshow("Smile Detector", frame) 
        key = cv2.waitKey(1) & 0xFF

        # exit if ESC is pressed
        if key==27: 
            sys.exit()

        frame_number += 1

    capture.release()