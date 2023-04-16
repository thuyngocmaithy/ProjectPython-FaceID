
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .SinhVien import SinhVien
from .ConnectDatabase import ConnectDatabase
import re

class SinhVienDAL:

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
            cursor.execute("SELECT * FROM sinhvien")            
            for row in SinhVienDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

    def countAll():
        count = 0
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM sinhvien")   
            row = cursor.fetchone()         
            if row is not None:
                count = row[0]
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return count
    
    def generateID():
        ma = ""
        stt = ""
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT `masinhvien` "\
                    + "FROM `sinhvien` "\
                    + "ORDER BY `masinhvien` DESC "\
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
        ma = "SV{0:03}".format(stt)
        return ma


    def add( sv: SinhVien):
        query = "INSERT INTO sinhvien "\
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (sv._masinhvien, sv._hoten, sv._malop, sv._cmnd,
                sv._gioitinh, sv._ngsinh, sv._email, sv._sodienthoai, sv._khoahoc)           
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

    def update( sv: SinhVien):
       # Câu lệnh update dữ liệu
        query = """ UPDATE sinhvien
                    SET hoten = %s,
                    malop = %s,
                    cmnd =%s,
                    gioitinh = %s,
                    ngaysinh = %s,
                    email = %s,
                    sodienthoai = %s,
                    khoahoc = %s
                    WHERE masinhvien = %s """

        data = (sv._hoten, sv._malop, sv._cmnd, sv._gioitinh, sv._ngsinh,
                 sv._email, sv._sodienthoai, sv._khoahoc,sv._masinhvien)  
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
        query = "DELETE FROM sinhvien WHERE masinhvien = '{}'".format(id)
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
        query = "SELECT * FROM sinhvien WHERE {} LIKE '%{}%'".format(key, value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in SinhVienDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    def findMaSinhVien(value):
        list = []
        query = "SELECT * FROM sinhvien WHERE masinhvien LIKE '{}'".format(value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in SinhVienDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    def checkTonTai(key, value):
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT * FROM sinhvien WHERE {} = '{}'".format(key, value)
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is None and cursor.rowcount == -1):
                return True
        except Exception as ex:
            print(ex)
        return False


