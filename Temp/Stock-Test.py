import tkinter as tk
from datetime import  datetime
import sqlite3 as db
from tkinter import *
from tkinter import ttk
import datetime
import time


win_stock = Tk()
tab_1 = ttk.Notebook(win_stock)
#-----------------------------------------------------------------
L_frame = LabelFrame(win_stock,text='DATA')
L_frame.pack(fill='both',expand='yes',padx=10,pady=10)

L_frame_2 = LabelFrame(win_stock,text="console")
L_frame_2.pack(fill='both', expand='yes',padx=10,pady=10)

L_T = Label(L_frame,text='Status : Connect DB Suscessfuly',font=20)
L_T.pack()
#-----------------------------------------------------------------

try:
    db_connect = db.connect('Stock_DB.db',timeout=1)
    print("Connect DB Suscessfuly")
    btn_color = Button(L_frame, text='CONNECTION', font=30,bg='green')
    btn_color.pack()

except Exception as e:
    print("Error is not connection to db : "+e)
    btn_color = Button(L_frame, text='DISCONNECTION', font=30,bg='red')
    btn_color.pack()
# ประกาศตัวแปร variable

#Create Windown and create table in DB
def windown_Create_tbl():
    create_table = Toplevel()
    create_table.title("Create Table")
    input_1 = Entry(create_table, font = 30)
    input_1.grid(row=0, column=1)
    L_name = Label(create_table,text="INPUT DATABASE NAME : ",font=30)
    L_name.grid(row=0,column=0)
    def create_tbl():
        try:
            sqlcommand = (f"create table {input_1.get()}(id_1 int primary key,name varchar(50),lastname varchar(50))")
            with db_connect as db_1:
                db_curr = db_1.cursor()
                db_curr.execute(sqlcommand)
        except Exception as e:
            print(f'Error is : {e}'.format())
        L_T.config(text=f"Status : Create Databse {input_1.get()} Suscessfuly")
        create_table.destroy()

    btn_Submit=Button(create_table,text="SUBMIT",command=create_tbl,font=30)
    btn_Submit.grid(row=0,column=2)

#inset data to DB and create new windon
def inser_data():
    count =1
    work_date_1 = time.strftime('%d')
    work_date_2 = time.strftime('%m')
    work_date_3 = time.strftime('%Y')
    x_10 = (f'{work_date_1}/{work_date_2}/{work_date_3}')

    insertdata = Toplevel()
    insertdata.title("Insert data")
    L_db = Label(insertdata,text='DATABASE NAME : ')
    L_db.grid(row=0,column=0)
    L_id=Label(insertdata,text='ID :',font=20).grid(row=1,column=0)
    L_name = Label(insertdata,text='Name : ',font=20).grid(row=2,column=0)
    L_name = Label(insertdata,text='Last Name : ',font=20).grid(row=3,column=0)
    L_tel = Label(insertdata,text='Date Work : ',font=20).grid(row=4,column=0)

    e_DB = Entry(insertdata, font=20)
    e_DB.grid(row=0,column=1)
    L_id_1=Label(insertdata)
    L_id_1.grid(row=1, column=1)
    e_name = Entry(insertdata,font=20)
    e_name.grid(row=2,column=1)
    e_Lname = Entry(insertdata,font=20)
    e_Lname.grid(row=3,column=1)
    L_date = Label(insertdata)
    L_date.grid(row=4,column=1)
    L_date.config(text=x_10,font=20)


#Select ดูค่าล่าสดของ ฟิลดด์ id_1 ใน tabel
    try:
        with db_connect as db_select:
            sql_command_select_1 = ('Select *from customer order by id_1 DESC LIMIT 1')
            db_curr_1 = db_select.cursor()
            db_curr_1.execute(sql_command_select_1)

            for  row in db_curr_1:
                count_id = row[0] +1
                #x_count = print(row[0]+1)
                L_id_1.config(text=f"000{row[0] +1}",font=20)

    except Exception as e:
        print(f'Error is cannot select data : [Error: {e}]'.format())

    def in_data():

        sql_command_1 = (f'insert into {e_DB.get()} values({count_id},"{e_name.get()}","{e_Lname.get()}","{x_10}")')
        print(f'{e_DB.get()} : 000{count_id} : {e_name.get()} : {e_Lname.get()} : {x_10} ')
        try:
            with db_connect as db_1:
                db_curr = db_1.cursor()
                db_curr.execute(sql_command_1)

        except Exception as e:
                print(f'Error is cant not to insert data : {e}'.format())

        L_T.config(text="Status : Insert Data Suscessfuly",font=20)
        insertdata.destroy()
    btn_insert = Button(insertdata,text="Insert Data",command = in_data )
    btn_insert.grid(row=5,column=1)

def update_data():
    count=1
    update_windown = Toplevel()
    update_windown.title('Update Data')
    update_windown.geometry('500x500')
    L_frame_update = LabelFrame(update_windown,text='Select data')
    L_frame_update.pack(fill='both',expand='yes',padx=10,pady=10)
    L_frame_update_control = LabelFrame(update_windown, text='Console')
    L_frame_update_control.pack(fill='both',expand='yes',padx=10,pady=10)

    Treeview_1 = ttk.Treeview(L_frame_update)
    Treeview_1['column'] = ('1', '2', '3', '4')
    Treeview_1.column('#0', width=0, minwidth=0, stretch=NO)
    Treeview_1.column('1', width=50, minwidth=270, stretch=NO)
    Treeview_1.column('2', width=150, minwidth=270, stretch=NO)
    Treeview_1.column('3', width=150, minwidth=270, stretch=NO)
    Treeview_1.column('4', width=150, minwidth=270, stretch=YES)

    Treeview_1.heading("#0", text='')
    Treeview_1.heading('1', text="ID")
    Treeview_1.heading('2', text="ID")
    Treeview_1.heading('3', text="ID")
    Treeview_1.heading('4', text="ID")



#select data from db to treeview
    try:
        with db_connect as db_2:
            sql_command=('select * from customer')
            db_curr=db_2.cursor()
            db_curr.execute(sql_command)
            col_sum = [tuple[0] for tuple in db_curr.description]


    except Exception as e:
        print(f'Error is : [{e}]'.format())



btn_create_tbl = Button(L_frame_2,text="Create Table",font=30,command=windown_Create_tbl)
btn_create_tbl.grid(row=0,column=0,padx=10,pady=10,stick='nwse')
btn_insert_data = Button(L_frame_2,text="Insert Data",font=30,command=inser_data)
btn_insert_data.grid(row=0,column=1,padx=10,pady=10,stick='nwse')
btn_update_data = Button(L_frame_2,text="Update Data",font=30,command=update_data)
btn_update_data.grid(row=0,column=2,padx=10,pady=10,stick='nwse')
win_stock.title("Stock")
win_stock.geometry('500x500')
win_stock.mainloop()