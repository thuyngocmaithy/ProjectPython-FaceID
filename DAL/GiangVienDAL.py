
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .GiangVien import GiangVien
from .ConnectDatabase import ConnectDatabase
import re

class GiangVienDAL:

    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row
    def get():
        list = []
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM giangvien")            
            for row in GiangVienDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    def getItem(value):    
        gv = None         
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM giangvien WHERE magiangvien = '{}'".format(value))            
            for row in cursor:
                gv = GiangVien(row[0],row[1],row[2],row[3])
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return gv
    def generateID():
        ma = ""
        stt = ""
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT `magiangvien` "\
                    + "FROM `giangvien` "\
                    + "ORDER BY `magiangvien` DESC "\
                    + "LIMIT 1"
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is None and cursor.rowcount == -1):
                stt = "0"
            else:
                stt = row[0]
        except:
            print("Lỗi tăng id")
        stt = (int)(re.sub("[^0-9]", "",stt))+1
        ma = "GV{0:03}".format(stt)
        return ma


    def add( gv: GiangVien):
        query = "INSERT INTO giangvien "\
                "VALUES(%s, %s, %s, %s)"
        data = (gv._magiangvien, gv._hoten,
                (int)(gv._sodienthoai), gv._mataikhoan)              
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query, data)         
            if cursor.rowcount>0:
                conn.commit()
                return True
            
        except Exception as ex:
            print(ex)
            return False

        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return False

    def update( gv: GiangVien):
       # Câu lệnh update dữ liệu
        query = """ UPDATE giangvien
                    SET hoten = %s,
                    sodienthoai = %s,
                    mataikhoan = %s
                    WHERE magiangvien = %s """

        data = (gv._hoten, (int)(gv._sodienthoai), gv._mataikhoan, gv._magiangvien)

        try:
            # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            if cursor.rowcount>0:
                conn.commit()
                return True
            
        except Exception as ex:
            print(ex)
            return False

        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return False
    def delete(id):
        query = "DELETE FROM giangvien WHERE magiangvien = '{}'".format(id)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            if cursor.rowcount>0:
                conn.commit()
                return True
            
        except Exception as ex:
            print(ex)
            return False
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return False
    def find(key, value):
        list = []
        query = "SELECT * FROM giangvien WHERE {} LIKE '%{}%'".format(key, value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in GiangVienDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

    def checkExistTaiKhoan(magiangvien):
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT * FROM giangvien WHERE mataikhoan = '{}'".format(magiangvien)
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is None and cursor.rowcount == -1):
                return True
        except Exception as ex:
            print(ex)
        return False

