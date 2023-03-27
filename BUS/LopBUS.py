import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.LopDAL import LopDAL
from DAL.Lop import Lop

class LopBUS:
    def get(self):
        return LopDAL.get()
    def generateID(self):
        return LopDAL.generateID()
    def add(self, sv:Lop):
        return LopDAL.add(sv)
    def update(self,sv:Lop):
        return LopDAL.update(sv)
    def delete(self, id):
        return LopDAL.delete(id)
    def find(self, key, value):
        return LopDAL.find(key, value)