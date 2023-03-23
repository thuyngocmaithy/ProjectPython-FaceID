import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.ThongKeDAL import ThongKeDAL
from DAL.ThongKe import ThongKe
class ThongKeBUS:
    def svcount(self):
        return ThongKeDAL.getsv(self)

    def ddcount(self):
        return ThongKeDAL.getdd(self)

    def latecount(self):
        return ThongKeDAL.getlate(self)

    def absentcount(self):
        return ThongKeDAL.getabsent(self)

    def KDDcount(self):
        return ThongKeDAL.getKDD(self)

    def list_DiMuon(self):
        return ThongKeDAL.list_DiMuon(self)

    def list_Vang(self):
        return ThongKeDAL.list_Vang(self)

    def list_KDD(self):
        return ThongKeDAL.list_KDD(self)

