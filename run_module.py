import mysql.connector
from prime_gui import *
from land_check import *

Prime_Gui = Prime_Gui()
Prime_Gui.main_gui()
Land_Check = Land_Check()



mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd=""
		)
mycursor = mydb.cursor()
mycursor.execute("use airport;")
sql_query = "Select * from landing ;"
mycursor.execute(sql_query)
myresult = mycursor.fetchall()
for i in myresult:
	print(i)
	aircraft_id = i[1]
	aircraft_type = i[2]
	wt = i[4]
	origin = i[5]
	dest = i[6]
	pass_no = i[3]
	Land_Check.land_func(aircraft_id,pass_no,aircraft_type,origin,wt,dest)

