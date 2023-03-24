import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.BuoiHocDAL import BuoiHocDAL
from DAL.BuoiHoc import BuoiHoc

class BuoiHocBUS:
    def get(self):
        return BuoiHocDAL.get()
    def getCmbLop(self):
        return BuoiHocDAL.getCmbLop()
    def getCmbGv(self):
        return BuoiHocDAL.getCmbGv()
    def generateID(self):
        return BuoiHocDAL.generateID()
    def add(self, bh:BuoiHoc):
        return BuoiHocDAL.add(bh)
    def update(self,bh:BuoiHoc):
        return BuoiHocDAL.update(bh)
    def delete(self, id):
        return BuoiHocDAL.delete(id)
    def find(self, key, value):
        return BuoiHocDAL.find(key, value)