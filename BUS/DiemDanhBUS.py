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
    def getCmbLop(self):
        return DiemDanhDAL.getCmbLop()
    def getCmbIdBH(self):
        return DiemDanhDAL.getCmbIdBH()
    def generateID(self):
        return DiemDanhDAL.generateID()
    def add(self, dd:DiemDanh):
        return DiemDanhDAL.add(dd)
    def update(self, dd:DiemDanh):
        return DiemDanhDAL.update(dd)
    # def update(self, dd:DiemDanh, sv:SinhVien):
    #     return DiemDanhDAL.update(dd, sv)
    def delete(self, id):
        return DiemDanhDAL.delete(id)
    def find(self, key, value):
        return DiemDanhDAL.find(key, value)
    def add(self, dd:DiemDanh):
        return DiemDanhDAL.add(dd)
    # def checkLogin(self,email, password):
    #     return DiemDanhDAL.checkLogin(email,password)