import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.GiangVienDAL import GiangVienDAL
from DAL.GiangVien import GiangVien

class GiangVienBUS:
    def get(self):
        return GiangVienDAL.get()
    def getItem(self, value):  
        return GiangVienDAL.getItem(value)
    def generateID(self):
        return GiangVienDAL.generateID()
    def add(self, gv:GiangVien):
        return GiangVienDAL.add(gv)
    def update(self,gv:GiangVien):
        return GiangVienDAL.update(gv)
    def delete(self, id):
        return GiangVienDAL.delete(id)
    def find(self, key, value):
        return GiangVienDAL.find(key, value)
    def checkExistTaiKhoan(self, magiangvien):
        return GiangVienDAL.checkExistTaiKhoan(magiangvien)
