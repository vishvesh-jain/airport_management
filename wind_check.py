import mysql.connector

class Weather_Check:
	runway_direc_1 = 9
	runway_direc_2 = 27        # length of the secondary list

	def weather_func(self):
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd=""
		)
		mycursor = mydb.cursor()

		import datetime
		a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")[:14]
		a = a+"30"
		date = a[:10]
		time = a[11:]
		mycursor.execute("use airport;")
		sql_query = "Select * from weather where date like '"+date+"'and time like '"+time+"';";
		mycursor.execute(sql_query)
		myresult = mycursor.fetchone()
		#print(sql_query)
		wind_dir = myresult[1] + 18 #18 is added to facilitate easy calculation
		wind_speed = myresult[2]
		visibility = myresult[3]
		flag=None
		

		print("VISIBILITY(in km) = ",visibility),
		if ((visibility < 5.0) and (visibility > 2.0)):
			print("visual land with caution")
		elif visibility <= 2.0:
			print ("divert to another airport")
			flag = "Divert_another_airport"
		else:
			print("visual landing cleared")		

		print("WIND DIRECTION (in 10's degree) =  ",(wind_dir-18))
		print("WIND SPEED = ",wind_speed)

		if (wind_speed > 30) :
			print("divert to another airport")
			flag = "Divert_another_airport"
		elif (wind_speed > 10):
			print("land with caution")
		else :
			print("clear to land")		


		if ((wind_dir-self.runway_direc_1) >= 0) and ((wind_dir-self.runway_direc_1) <=9) :
			print("land runway from the side ", self.runway_direc_1)
			flag_runway_direc = self.runway_direc_1
		else :
			print("land runway from the side ",self.runway_direc_2)
			flag_runway_direc = self.runway_direc_2


		if flag == "Divert_another_airport":
			print("Divert to another airport due to severe weather condition")
		else:
			print("weather clear, continue landing procedure")		
		
		return flag_runway_direc		