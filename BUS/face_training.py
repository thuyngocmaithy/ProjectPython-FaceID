''''
Training Multiple Faces stored on a DataBase:
	==> Each face should have a unique numeric integer ID as 1, 2, 3, etc                       
	==> LBPH computed model will be saved on trainer/ directory. (if it does not exist, pls create one)
	==> for using PIL, install pillow library with "pip install pillow"

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18   

'''
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QWidget
import cv2
import numpy as np
from PIL import Image
import os
import re
class face_training(QWidget):
    def __init__(self):
        super().__init__()
        # Path for face image database
        self.path = 'image\\photo'
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # function to get the images and label data
    def getImagesAndLabels(self, path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]    
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = os.path.split(imagePath)[-1].split("-")[0]
            id = (int)(re.sub("[^0-9]", "",id))
            faces = self.detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids
    def train(self):
        QMessageBox.information(self,"Thông báo","Đang training data. Vui lòng chờ vài phút...")
        faces,ids = self.getImagesAndLabels(self.path)
        self.recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        self.recognizer.write('TrainingImageLabel/Trainner.yml') # recognizer.save() worked on Mac, but not on Pi

        # Print the numer of faces trained and end program
        QMessageBox.information(self,"Thông báo","Traning data thành công")
