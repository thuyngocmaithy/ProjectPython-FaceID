
import cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import QMessageBox
from .HinhAnhSVBUS import HinhAnhSVBUS
from DAL.HinhAnhSV import HinhAnhSV


class face_dataset(QThread):
    signal = pyqtSignal(np.ndarray)
    cap = None

    def __init__(self, index, id):
        self.index = index
        self.idSV = id
        super(face_dataset, self).__init__()

    def run(self):
        cam = cv2.VideoCapture(0)

        face_detector = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')

        count = 0
        hsBUS = HinhAnhSVBUS()
        # XÓa ảnh sinh viên trong database
        hsBUS.delete(self.idSV) 
        while (True):

            ret, img = cam.read()
            img = cv2.flip(img, 1)  # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
                        
            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                count += 1
                # Save the captured image into the datasets folder
                nameFile = f'./image/photo/{self.idSV}-image{count}.jpg'
                cv2.imwrite(nameFile, gray[y:y+h, x:x+w])
                # LƯU VÀO DATABASE
                hs = HinhAnhSV(self.idSV, nameFile)
                hsBUS.add(hs)

            if ret:
                self.signal.emit(img)

            if count >= 200:  # Take 30 face sample and stop video
                arr = np.array([0])
                self.signal.emit(arr)
                break

        cam.release()
