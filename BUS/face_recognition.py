import os
import cv2
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
from PyQt6.QtCore import QThread, pyqtSignal, Qt


class face_recognition(QThread):
    signal = pyqtSignal(np.ndarray)
    cap = None

    def __init__(self, index):
        self.index = index
        super(face_recognition, self).__init__()

    def run(self):
        cap = cv2.VideoCapture(0)
        self.cap = cap
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("TrainingImageLabel/Trainner.yml")
        df = pd.read_csv("StudentDetails/StudentDetails.csv")
        font = cv2.FONT_HERSHEY_SIMPLEX
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        col_names = ['Id', 'Name', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)

        minW = 0.1*cap.get(3)
        minH = 0.1*cap.get(4)

        while True:
            ret, cv_img = cap.read()
            if(cv_img is not None):
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(cv_img, (x, y), (x+w, y+h), (0, 225, 0), 2)
                Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
                if (conf != None):
                    # print(Id)
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(
                        ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(
                        ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    tt = str(Id) + "-"+aa
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                else:
                    Id = 'Unknown'
                    print("UNKNOWN")
                    tt = str(Id)
                if (conf > 75):
                    print("75")
                    noOfFile = len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown/Image" +
                                str(noOfFile) + ".jpg", cv_img[y:y+h, x:x+w])
                cv2.putText(cv_img, str(tt), (x, y+h),
                            font, 1, (255, 255, 255), 2)
                attendance = attendance.drop_duplicates(
                    subset=['Id'], keep='first')
            if ret:
                self.signal.emit(cv_img)

    def stop(self):
        if self.cap is not None:
            self.cap.release()
        
        self.cap = None
        # self.terminate()
