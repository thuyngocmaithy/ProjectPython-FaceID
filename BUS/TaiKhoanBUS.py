import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.TaiKhoanDAL import TaiKhoanDAL
from DAL.TaiKhoan import TaiKhoan

class TaiKhoanBUS:
    def get(self):
        return TaiKhoanDAL.get()
    def generateID(self):
        return TaiKhoanDAL.generateID()
    def add(self, tk:TaiKhoan):
        return TaiKhoanDAL.add(tk)
    def update(self,tk:TaiKhoan):
        return TaiKhoanDAL.update(tk)
    def delete(self, id):
        return TaiKhoanDAL.delete(id)
    def find(self, key, value):
        return TaiKhoanDAL.find(key, value)
    def checkLogin(self,email, password):
        return TaiKhoanDAL.checkLogin(email,password)
    def changePassword(self, email, mkmoi):
        return TaiKhoanDAL.changePassword(email,mkmoi)
    def checkNotTaiKhoanAmin(self, mataikhoan):
        return TaiKhoanDAL.checkNotTaiKhoanAmin(mataikhoan)
    def checkEmailTonTai(self, email):
        return TaiKhoanDAL.checkEmailTonTai(email)
