import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.BuoiHocDAL import BuoiHocDAL
from DAL.BuoiHoc import BuoiHoc

class BuoiHocBUS:
    def get(self):
        return BuoiHocDAL.get()