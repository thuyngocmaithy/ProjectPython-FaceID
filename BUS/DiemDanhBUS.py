import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.DiemDanhDAL import DiemDanhDAL
from DAL.DiemDanh import DiemDanh
from DAL.SinhVien import SinhVien

class DiemDanhBUS:
    def get(self):
        return DiemDanhDAL.get()
    def generateID(self):
        return DiemDanhDAL.generateID()
    def update(self, dd:DiemDanh):
        return DiemDanhDAL.update(dd)
    def deleteAll(self):
        return DiemDanhDAL.deleteAll()
    def delete(self, id):
        return DiemDanhDAL.delete(id)
    def find(self, key, value):
        return DiemDanhDAL.find(key, value)
    def findMaDiemDanh(self, value):
        return DiemDanhDAL.findMaDiemDanh(value)
    def add(self, dd:DiemDanh):
        return DiemDanhDAL.add(dd)
    def updateGioRa(self, masinhvien, mabuoihoc, giora):
        return DiemDanhDAL.updateGioRa(masinhvien, mabuoihoc, giora)