import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.Quyen_ChucNangDAL import Quyen_ChucNangDAL
from DAL.Quyen_ChucNang import Quyen_ChucNang

class Quyen_ChucNangBUS:
    def get(self):
        return Quyen_ChucNangDAL.get()
    def generateID(self):
        return Quyen_ChucNangDAL.generateID()
    def add(self, q:Quyen_ChucNang):
        return Quyen_ChucNangDAL.add(q)
    def update(self,q:Quyen_ChucNang):
        return Quyen_ChucNangDAL.update(q)
    def delete(self, id):
        return Quyen_ChucNangDAL.delete(id)
    def getListChucNangTheoQuyen(self,maquyen):
        return Quyen_ChucNangDAL.getListChucNangTheoQuyen(maquyen)
    
