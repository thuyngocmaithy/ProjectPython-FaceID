import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.ChucNangDAL import ChucNangDAL
from DAL.ChucNang import ChucNang

class ChucNangBUS:
    def get(self):
        return ChucNangDAL.get()
    def generateID(self):
        return ChucNangDAL.generateID()
    def add(self, cn:ChucNang):
        return ChucNangDAL.add(cn)
    def update(self,cn:ChucNang):
        return ChucNangDAL.update(cn)
    def delete(self, id):
        return ChucNangDAL.delete(id)
    def find(self, key, value):
        return ChucNangDAL.find(key, value)
