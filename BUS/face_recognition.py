import cv2
import numpy as np
import time
from PyQt6.QtCore import QThread, pyqtSignal
from .SinhVienBUS import SinhVienBUS

class face_recognition(QThread):
    signal = pyqtSignal(np.ndarray)
    cap = None
    masinhvien_save = ''
    Id = ''
    image = ''
    link_image =''
    cv_img_cur = np.array([0])
    def __init__(self, index):
        self.index = index
        super(face_recognition, self).__init__()

    def run(self):
        self.arr_ID = []
        cap = cv2.VideoCapture(0)
        self.cap = cap
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("TrainingImageLabel/Trainner.yml")
        font = cv2.FONT_HERSHEY_SIMPLEX
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)  

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
                self.Id, conf = recognizer.predict(gray[y:y+h, x:x+w])        
                if (conf <75):
                    ten = ''
                    sv = SinhVienBUS()
                    masinhvien = "SV{0:03}".format(self.Id)   
                    # Lấy tên sinh viên
                    list = sv.findMaSinhVien(masinhvien)                    
                    if list is not None:
                            for row in list:
                                ten = row[1]
                    tt = masinhvien + "-"+ten
                    # KIỂM TRA MSV CÓ TRONG MẢNG CHƯA (Chưa => lưu điểm danh mới)
                    # SET flag firstImage 
                    if conf < 50 and masinhvien not in self.arr_ID:
                        self.masinhvien_save = masinhvien    
                        self.arr_ID.append(self.masinhvien_save)
                        self.cv_img_cur = gray[y:y+h, x:x+w]
                        t = time.localtime()
                        current_time = time.strftime("%H_%M_%S", t)                         
                        self.link_image = f'./image/diemdanh/{self.masinhvien_save}_{current_time}.jpg'
                        cv2.imwrite(self.link_image, gray[y:y+h, x:x+w])
                    
                    conf = "  {0}%".format(round(100 - conf))                                                                
                    
                else:
                    self.Id = "unknown"
                    tt = str(self.Id)
                    conf = "  {0}%".format(round(100 - conf))
                
                

                cv2.putText(cv_img, str(tt), (x+5,y-5), font, 1, (255,255,255), 2)

                
            if ret:
                self.signal.emit(cv_img)

    def stop(self):
        if self.cap is not None:
            self.cap.release()
        
        self.cap = None

    def getIDSV(self):
        return self.masinhvien_save
    
    def getCv_Image_Cur(self):
        return self.cv_img_cur
    
    def getLink_Image(self):
        return self.link_image
