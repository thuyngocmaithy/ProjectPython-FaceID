import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.SinhVienDAL import SinhVienDAL
from DAL.SinhVien import SinhVien

class SinhVienBUS:
    def get(self):
        return SinhVienDAL.get()
    def generateID(self):
        return SinhVienDAL.generateID()
    def add(self, sv:SinhVien):
        return SinhVienDAL.add(sv)
    def update(self,sv:SinhVien):
        return SinhVienDAL.update(sv)
    def delete(self, id):
        return SinhVienDAL.delete(id)
    def find(self, key, value):
        return SinhVienDAL.find(key, value)
    # def checkLogin(self,email, password):
    #     return SinhVienDAL.checkLogin(email,password)
