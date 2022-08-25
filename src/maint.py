from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from s2 import Ui_MainWindow
import psycopg2
import sys

class Ui :

    def __init__(self) :
        self.main_window = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_window)


        self.uic.but_viewpro.clicked.connect(self.show_screen1)
        self.uic.but_order.clicked.connect(self.show_screen2)
        self.uic.but_editdata.clicked.connect(self.show_screen3)
        self.uic.pushview_all.clicked.connect(self.loadData_pro)
        self.uic.pushexe.clicked.connect(self.get_input_pro)
        self.uic.but_order.clicked.connect(self.loadData_order)
        self.uic.but_edit_add.clicked.connect(self.get_input_add)
        self.uic.but_edit_upda.clicked.connect(self.get_input_update)
        self.uic.but_edit_dele.clicked.connect(self.get_input_delete)
        self.uic.but_chats.clicked.connect(self.show_fedb)


        if self.uic.pushexe.clicked.connect(self.get_input_pro) :
            self.uic.table_kho.defaultDropAction()
    

    def show(self) :
        self.main_window.show()

    def show_screen1(self) :
        self.uic.tabWidget.setCurrentWidget(self.uic.tab)

    def show_screen3(self) :
        self.uic.tabWidget.setCurrentWidget(self.uic.tab_2)
                            
    def show_screen2(self) :
        self.uic.tabWidget.setCurrentWidget(self.uic.tab_3)

    def show_fedb(self) :
        try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")
            cur = conn.cursor()

            for_chats = 'select sp.ten,tk.ten,nx.noidung,nx.sao from nhanxet nx join taikhoan tk on nx.user_id = tk.id join sanpham sp on sp.id = nx.product_id'
            cur.execute(for_chats)

            fet_chat = cur.fetchall()
            self.uic.table_chat.setRowCount(len(fet_chat))

            chat_row = 0
            for row1 in fet_chat :
                self.uic.table_chat.setItem(chat_row,0,QtWidgets.QTableWidgetItem(str(row1[0])))
                self.uic.table_chat.setItem(chat_row,1,QtWidgets.QTableWidgetItem(str(row1[1])))
                self.uic.table_chat.setItem(chat_row,2,QtWidgets.QTableWidgetItem(row1[2]))
                self.uic.table_chat.setItem(chat_row,3,QtWidgets.QTableWidgetItem(str(row1[3])))
                
                chat_row = chat_row + 1

        except Exception as e:
                print('Unable to connect %s' % str(e))
        finally:
                if conn is not None:
                    conn.close()        


    def get_input_delete(self) :
        try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")

            cur = conn.cursor()
            get_pro_id1 = self.uic.lineEdit_kho.text()

            for_delete = ("delete from sanpham where id = %s" % int(get_pro_id1))
            cur.execute(for_delete)

            conn.commit()


        except Exception as e:
                print('Unable to connect %s' % str(e))
        finally:
                if conn is not None:
                    conn.close()    

    def get_input_update(self) :
        try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")

            cur = conn.cursor()
            pro_update = self.uic.lineEdit_update.text()
            get_pro_id = self.uic.lineEdit_kho.text()
            tuple_update = pro_update.split(":")
            tuple_update.append(int(get_pro_id))
            tuple_up1 = tuple_update[1:3]

            print(tuple_update)
            if tuple_update[0] == 'gia' :
                for_update = "update sanpham set gia = %s where id = %s"
                cur.execute(for_update,tuple_up1)
            if tuple_update[0] == 'soluong' :
                for_update = "update sanpham set soluong = %s where id = %s"
                cur.execute(for_update,tuple_up1)
            if tuple_update[0] == 'ten' :
                for_update = "update sanpham set ten = %s where id = %s"
                cur.execute(for_update,tuple_up1)
            if tuple_update[0] == 'mota' :
                for_update = "update sanpham set mota = %s where id = %s"
                cur.execute(for_update,tuple_up1)

            conn.commit()

            
        except Exception as e:
                print('Unable to connect %s' % str(e))
        finally:
                if conn is not None:
                    conn.close()
            

    def get_input_add(self) :
        pro_price = self.uic.lineEdit_price.text()
        pro_amount = self.uic.lineEdit_amount.text()
        pro_name = self.uic.lineEdit_name.text()
        pro_descri = self.uic.lineEdit_descri.text()

        try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")

            cur = conn.cursor()
            sql_add = "insert into sanpham(gia,soluong,ten,mota) values(%s,%s,%s,%s)"
            tuple = (int(pro_price),int(pro_amount),pro_name,pro_descri)
            cur.execute(sql_add,tuple)

            self.uic.label_edit.setText("01 Product Added.")

            conn.commit()


        except Exception as e:
                print('Unable to connect %s' % str(e))
        finally:
                if conn is not None:
                    conn.close()

    def get_input_pro(self) :
       getInput_pro = self.uic.lineEdit_kho.text()
       try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")

            cur = conn.cursor()

            filt_pro = ("select * from sanpham where id = '%s'" % getInput_pro)

            cur.execute(filt_pro)
            fet_pro = cur.fetchall()
            self.uic.table_kho.setRowCount(len(fet_pro))

            table_row_filt = 0
            for row_pro in fet_pro :
                self.uic.table_kho.setItem(table_row_filt,0,QtWidgets.QTableWidgetItem(str(row_pro[0])))
                self.uic.table_kho.setItem(table_row_filt,1,QtWidgets.QTableWidgetItem(str(row_pro[1])))
                self.uic.table_kho.setItem(table_row_filt,2,QtWidgets.QTableWidgetItem(str(row_pro[2])))
                self.uic.table_kho.setItem(table_row_filt,3,QtWidgets.QTableWidgetItem(row_pro[3]))
                self.uic.table_kho.setItem(table_row_filt,4,QtWidgets.QTableWidgetItem(row_pro[4]))
                
                table_row_filt = table_row_filt + 1
                      

       except Exception as e:
            print('Unable to connect %s' % str(e))
       finally:
            if conn is not None:
                conn.close()

    def loadData_pro(self) :
        try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")

            cur = conn.cursor()

            view_pro = 'select * from sanpham'

            table_row_viewAll = 0
            cur.execute(view_pro)
            fet = cur.fetchall()
            self.uic.table_kho.setRowCount(len(fet))

            for row in fet :
                self.uic.table_kho.setItem(table_row_viewAll,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.uic.table_kho.setItem(table_row_viewAll,1,QtWidgets.QTableWidgetItem(str(row[1])))
                self.uic.table_kho.setItem(table_row_viewAll,2,QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic.table_kho.setItem(table_row_viewAll,3,QtWidgets.QTableWidgetItem((row[3])))
                self.uic.table_kho.setItem(table_row_viewAll,4,QtWidgets.QTableWidgetItem((row[4])))
                
                table_row_viewAll = table_row_viewAll + 1


        except Exception as e:
            print('Unable to connect %s' % str(e))
        finally:
            if conn is not None:
                conn.close()

    def loadData_order(self) :
        try :
            conn = psycopg2.connect(host="tung.postgres.database.azure.com",
            database="postgres", 
            user="tung", 
            password="Anm19042")

            cur = conn.cursor()

            view_order = 'select dh.id,tk.ten,tk.diachi,dh.trangthaidon,dh.ngaydat,dh.ngayhengiao,sp.ten,ctd.soluong,ctd.mausac,ctd.kichco from donhang dh join chitietdon ctd on dh.id = ctd.order_id join sanpham sp on ctd.product_id = sp.id join taikhoan tk on dh.user_id = tk.id'

            row_viewOrder = 0
            cur.execute(view_order)
            fet_order = cur.fetchall()
            self.uic.table_order.setRowCount(len(fet_order))

            for row in fet_order :
                self.uic.table_order.setItem(row_viewOrder,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.uic.table_order.setItem(row_viewOrder,1,QtWidgets.QTableWidgetItem(row[1]))
                self.uic.table_order.setItem(row_viewOrder,2,QtWidgets.QTableWidgetItem(str(row[2])))
                self.uic.table_order.setItem(row_viewOrder,3,QtWidgets.QTableWidgetItem(row[3]))
                self.uic.table_order.setItem(row_viewOrder,4,QtWidgets.QTableWidgetItem(str(row[4])))
                self.uic.table_order.setItem(row_viewOrder,5,QtWidgets.QTableWidgetItem(str(row[5])))
                self.uic.table_order.setItem(row_viewOrder,6,QtWidgets.QTableWidgetItem(row[6]))
                self.uic.table_order.setItem(row_viewOrder,7,QtWidgets.QTableWidgetItem(str(row[7])))
                self.uic.table_order.setItem(row_viewOrder,8,QtWidgets.QTableWidgetItem(row[8])) 
                self.uic.table_order.setItem(row_viewOrder,9,QtWidgets.QTableWidgetItem(str(row[9])))
                
                row_viewOrder = row_viewOrder + 1


        except Exception as e:
            print('Unable to connect %s' % str(e))
        finally:
            if conn is not None:
                conn.close()


app = QApplication(sys.argv)
main_window = Ui()
main_window.show()
sys.exit(app.exec_())