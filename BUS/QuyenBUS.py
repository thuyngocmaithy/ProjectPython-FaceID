import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.QuyenDAL import QuyenDAL
from DAL.Quyen import Quyen

class QuyenBUS:
    def get(self):
        return QuyenDAL.get()
    def generateID(self):
        return QuyenDAL.generateID()
    def add(self, q:Quyen):
        return QuyenDAL.add(q)
    def update(self,q:Quyen):
        return QuyenDAL.update(q)
    def delete(self, id):
        return QuyenDAL.delete(id)
    def find(self, key, value):
        return QuyenDAL.find(key, value)
