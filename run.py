import os
try:
    os.system('python alerter.py --shape-predictor shape_predictor_face_landmarks.dat')
except:
    os.system('python3 alerter.py --shape-predictor shape_predictor_face_landmarks.dat')