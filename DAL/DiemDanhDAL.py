
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .DiemDanh import DiemDanh
from .ConnectDatabase import ConnectDatabase
import re
# from DAL.SinhVienDAL import SinhVienDAL
from .SinhVien import SinhVien

class DiemDanhDAL:
    # DAL.SinhVien sv = SinhVienDAL
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
            query = "SELECT dd.madiemdanh, dd.masinhvien, sv.hoten, l.tenlop, "\
            + "dd.giovao, dd.giora, dd.ngay, dd.mabuoihoc, dd.trangthai, "\
            + "dd.hinhanh FROM diemdanh dd, sinhvien sv, lop l WHERE "\
            + "l.malop = sv.malop AND dd.masinhvien = sv.masinhvien"
            cursor.execute(query) 
            for row in DiemDanhDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

    def getCmbLop():
        list = []
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT tenlop FROM lop")        
            for row in DiemDanhDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    
    def getCmbIdBH():
        list = []
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT mabuoihoc FROM buoihoc")        
            for row in DiemDanhDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

    def generateID():
        ma = ""
        stt = ""
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT `madiemdanh` "\
                    + "FROM `diemdanh` "\
                    + "ORDER BY `madiemdanh` DESC "\
                    + "LIMIT 1"
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is not None and cursor.rowcount == 0):
                stt = "0"
            else:
                stt = row[0]
        except:
            print("Lỗi tăng id")
        stt = (int)(re.sub("[^0-9]", "",stt))+1
        ma = "ĐD{0:03}".format(stt)
        return ma

    def update( dd: DiemDanh):
       # Câu lệnh update dữ liệu
        query = """ UPDATE diemdanh
                    SET masinhvien = %s,
                    giovao = %s,
                    giora = %s,
                    ngay = %s,
                    trangthai = %s
                    WHERE madiemdanh = %s"""

        data = (dd._masinhvien, dd._giovao, dd._giora, 
                dd._ngay, dd._trangthai, dd._madiemdanh)

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
        query = "DELETE FROM diemdanh WHERE madiemdanh = '{}'".format(id)
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
        query = "SELECT dd.madiemdanh, sv.masinhvien, sv.hoten, l.tenlop, "\
            + "dd.giovao, dd.giora, dd.ngay, dd.mabuoihoc, dd.trangthai, "\
            + "dd.hinhanh FROM diemdanh dd, sinhvien sv, lop l WHERE "\
            + "l.malop = sv.malop AND dd.masinhvien = sv.masinhvien AND dd.{} LIKE '%{}%'".format(key, value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in DiemDanhDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    
    def add( dd: DiemDanh):
        query = "INSERT INTO diemdanh (madiemdanh, masinhvien, giovao, giora, ngay, mabuoihoc, trangthai)"\
                "VALUES(%s, %s, %s, %s, %s, %s, %s)"
        data = (dd._madiemdanh, dd._masinhvien, dd._giovao, dd._giora, 
                dd._ngay, dd._mabuoihoc, dd._trangthai)          
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

    # def checkLogin(email,password):
    #     global cursor
    #     query = 'SELECT * FROM `giangvien` WHERE `email` = %s and `matkhau` = %s'
    #     try:
    #          # Kết nối database
    #         connDb = ConnectDatabase()
    #         conn = connDb.Connect()
    #         cursor = conn.cursor()
    #         vals = (email, password)        
    #         cursor.execute(query, vals)
    #         user = cursor.fetchone()
    #         if user is not None:
    #             return True
    #     except Exception as ex:
    #         print(ex)
    
    #     finally:
    #         # Đóng kết nối
            
    #         cursor.close()
    #         conn.close()
    #     return False