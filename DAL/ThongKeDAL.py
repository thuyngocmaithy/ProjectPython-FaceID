from .ThongKe import ThongKe
from .ConnectDatabase import ConnectDatabase
class ThongKeDAL:
    def getsv(self):
        global row, cursor, conn
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            So_luong_sv = "SELECT COUNT(*) FROM sinhvien;"
            cursor.execute(So_luong_sv)
            row = cursor.fetchone()

        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return row[0]

    def getdd(self):
        global row, cursor, conn
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            So_diem_danh = "SELECT COUNT(*) FROM diemdanh;"
            cursor.execute(So_diem_danh)
            row = cursor.fetchone()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row[0]

    def getlate(self):
        global row, cursor, conn
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            late = "SELECT COUNT(madiemdanh) FROM diemdanh dd JOIN buoihoc bh ON dd.mabuoihoc = bh.mabuoihoc WHERE giovao > giobatdau OR giovao = '00:00:00' AND giora != '00:00:00';"
            cursor.execute(late)
            row = cursor.fetchone()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row[0]

    def getabsent(self):
        global row, cursor, conn
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            absent = """
            SELECT COUNT(sv.masinhvien) 
            FROM sinhvien sv, sinhvien_buoihoc svbh, buoihoc bh
            WHERE sv.masinhvien = svbh.masinhvien 
            AND svbh.mabuoihoc = bh.mabuoihoc
            AND sv.masinhvien IN
            (SELECT sb.masinhvien
            FROM sinhvien_buoihoc sb left join diemdanh dd 
            ON sb.mabuoihoc = dd.mabuoihoc
            AND sb.masinhvien = dd.masinhvien
            WHERE dd.madiemdanh is NULL)
            """
            cursor.execute(absent)
            row = cursor.fetchone()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row[0]

    def getKDD(self):
        global row, cursor, conn
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            KDD = "SELECT COUNT(madiemdanh) FROM diemdanh dd JOIN buoihoc bh ON dd.mabuoihoc = bh.mabuoihoc WHERE giora < gioketthuc OR giora = '00:00:00' AND giovao != '00:00:00';"
            cursor.execute(KDD)
            row = cursor.fetchall()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row

    def list_DiMuon(self):
        global row, cursor, conn
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            svDiMuon = "SELECT dd.masinhvien, sv.hoten, sv.malop, dd.ngay, dd.mabuoihoc, dd.trangthai FROM sinhvien sv left join diemdanh dd on dd.masinhvien = sv.masinhvien join buoihoc bh  on dd.mabuoihoc = bh.mabuoihoc WHERE dd.giovao > bh.giobatdau OR dd.giovao = '00:00:00' AND dd.giora != '00:00:00'"
            cursor.execute(svDiMuon)
            row = cursor.fetchall()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row

    def list_Vang(self):
        global row, cursor, conn
        try:
            conndb = ConnectDatabase()
            conn = conndb.Connect()
            cursor = conn.cursor()
            svVang = """ SELECT sv.masinhvien, sv.hoten, sv.malop, bh.ngay, bh.mabuoihoc
            FROM sinhvien sv, sinhvien_buoihoc svbh, buoihoc bh
            WHERE sv.masinhvien = svbh.masinhvien 
            AND svbh.mabuoihoc = bh.mabuoihoc
            AND sv.masinhvien IN
            (SELECT sb.masinhvien
            FROM sinhvien_buoihoc sb left join diemdanh dd 
            ON sb.mabuoihoc = dd.mabuoihoc
            AND sb.masinhvien = dd.masinhvien
            WHERE dd.madiemdanh is NULL) """
            cursor.execute(svVang)
            row = cursor.fetchall()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row

    def list_KDD(self):
        global row, cursor, conn
        try:
            conndb = ConnectDatabase()
            conn = conndb.Connect()
            cursor = conn.cursor()
            svKDD = "SELECT dd.masinhvien, sv.hoten, sv.malop, dd.ngay, dd.mabuoihoc, dd.trangthai FROM sinhvien sv left join diemdanh dd on dd.masinhvien = sv.masinhvien join buoihoc bh  on dd.mabuoihoc = bh.mabuoihoc WHERE dd.giora < bh.gioketthuc OR dd.giora = '00:00:00' AND dd.giovao != '00:00:00'"
            cursor.execute(svKDD)
            row = cursor.fetchall()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return row



