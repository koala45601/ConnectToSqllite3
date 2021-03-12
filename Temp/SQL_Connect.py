import sqlite3 as db

db_connect = db.connect('customer.sqlite')
db_curr = db_connect.cursor()
'''
#Select data
sql_command=('select *from customer_id')
db_result=db_curr.execute(sql_command)  #ในวงเล็บใส่คสั่ง sql
for row in db_result:
    print(f'Name : {row[1]} Lastname : {row[2]} Tel : {row[3]}')
#print('Select database successfully')
db_connect.close()'''

'''
#insert into ข้อมูล
sql_command_insert=('insert into customer_id values(4,"Friday","March","012311921")')
try:
    db_curr_insert=db_connect.execute(sql_command_insert)
    print('Suscessfuly insert data')
except Exception as e:
    print('Error is',e)
'''
'''
#update data
sql_command = ('update customer_id set id_1 = 5 where name = "Friday"')
db_curr_update = db.connect(sql_command)
db_connect.close()
'''