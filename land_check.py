import re
import time
from wind_check import *
Weather_Check = Weather_Check()
class Land_Check:

	def land_func(self,aircraft_id_check,no_of_pass_check,aircraft_type_check,origin_check,wt_check,dest_check):
		
		start_time = time.time()
		taxiway_name = ["Juliet 1","Juliet 2","Juliet 3"]

		 #get details from GUI
		aircraft_id = aircraft_id_check
		no_of_pass = no_of_pass_check
		aircraft_type = aircraft_type_check
		origin = origin_check
		wt = wt_check
		dest = dest_check

		print("\n",aircraft_id,"\t",origin,"\t",dest)
		 #then get details from database
		import mysql.connector
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd=""
		)

		mycursor = mydb.cursor()
		mycursor.execute("use airport;")
		sql_query = "SELECT * FROM aircraft where aircraft_type='"+aircraft_type+"';"
		#print(sql_query)
		mycursor.execute(sql_query)

		myresult = mycursor.fetchone()
		aircraft_length = myresult[1]
		minwt = myresult[3]
		maxwt = myresult[4]
		min_landing_dist = myresult[6]
		extra_wt = wt-minwt
		extra_landing_dist = (wt/1000)*5
		total_landing_dist = min_landing_dist+extra_landing_dist

		runway_direc = Weather_Check.weather_func()
		if minwt <= wt <= maxwt:
			print("WEIGHT LIMIT OK ,proceed toward landing from side ",runway_direc)
		elif wt>=maxwt:
			print("Move to Holding pattern and change your heading to 11 and continue fuel burn")	


		a = ['rct1','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rct2','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rc','rct3']
		check_list = []
		hostname_set = set(a)
		for i in hostname_set:
			check_list.append(i[:2])
			check_set = set(check_list)
		if ('rt'or'rw') in check_set:
			print("STOP LANDING, runway not cleared")
		else:
			print("RUNWAY EMPTY, proceed to land")	

		array_dist =(int)(total_landing_dist/40)

		b = []
		c = []
		r = re.compile(".*t.*")
		newlist = list(filter(r.match, a))
		for i in newlist:
			b.append(a.index(i))


		if runway_direc is 9:
			c=b
		else:
			for i in b:
				c.append(len(a)-i-1)

		for i in c:
			if i>array_dist:
				taxiway_no = c.index(i)
				
				break

		print("TAXI OUT from TAXIWAY :",taxiway_name[taxiway_no])
		sql_query = " insert into landing_complete values(now(),'6e-110', 'A350', 235, 200000, 'DEL', 'BOM');"
		#val = (aircraft_id,aircraft_type,no_of_pass,wt,origin,dest)
		#print(sql_query)
		#mycursor.execute(sql_query)
		sql_query2 = "Delete from landing where airline_id = '"+aircraft_id+"';"
		
		#mycursor.execute(sql_query2)
		#mydb.commit()
		time.sleep(3)


		print("PLANE EXITED THE RUNWAY, CLEARED FOR NEXT OPERATION")	