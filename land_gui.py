from tkinter import *

def main_gui(self):
	root=Tk()
	lbl1 = Label(root, text="AIR TRAVEL", font=("Arial Bold", 20) )
	lbl1.grid(column=3,row=0)


	def get_takeoff():
		orig=e1.get()
		dest=e2.get()
		Airline_Name=e3.get()
		Airline_Type=e4.get()
		Total_number=e5.get()
		TakeOff_Weight=e6.get()
		Runway=e7.get()
		print(orig)
		print(dest)
		print(Airline_Name)
		print(Airline_Type)
		print(Total_number)
		print(TakeOff_Weight)
		print(Runway)
	

	def get_land():
		orig=e1.get()
		dest=e2.get()
		Airline_Name=e3.get()
		Airline_Type=e4.get()
		Total_number=e5.get()
		TakeOff_Weight=e6.get()
		Runway = 0
		print(orig)
		print(dest)
		print(Airline_Name)
		print(Airline_Type)
		print(Total_number)
		print(TakeOff_Weight)
			


	def takeoff():
		Label(root, text="SOURCE").grid(column=1,row=4)
		Label(root, text="TO").grid(column=3,row=4)
		Label(root, text="DESTINATION").grid(column=7,row=4)
		Label(root,text="Airline Name").grid(row=8,column=2)
		Label(root,text="Aircraft Type").grid(row=9,column=2)
		Label(root,text="No. of passenger and crew").grid(row=10,column=2)
		Label(root,text="TakeOff weight").grid(row=11,column=2)
		Label(root,text="Preferred Runnway").grid(row=12,column=2)
		e1.grid(row=4, column=2)
		e2.grid(row=4, column=5)
		e3.grid(row=8,column=3)
		e4.grid(row=9,column=3)
		e5.grid(row=10,column=3)
		e6.grid(row=11,column=3)
		e7.grid(row=12,column=3)
		Button(root,text="SUBMIT DETAILS",command=get_takeoff).grid(row=13,column=2,sticky=W,pady=4)
	def Landing():
		Label(root, text="SOURCE").grid(column=1,row=4)
		Label(root, text="TO").grid(column=3,row=4)
		Label(root, text="DESTINATION").grid(column=7,row=4)
		Label(root,text="Airline Name").grid(row=8,column=2)
		Label(root,text="Aircraft Type").grid(row=9,column=2)
		Label(root,text="No of passenger and crew").grid(row=10,column=2)
		Label(root,text="Current weight").grid(row=11,column=2)
		Label(root,text="                                            ").grid(row=12,column=2)
		e1.grid(row=4, column=2)
		e2.grid(row=4, column=5)
		e3.grid(row=8,column=3)
		e4.grid(row=9,column=3)
		e5.grid(row=10,column=3)
		e6.grid(row=11,column=3)
		e7.grid(row=12,column=3)
		e7.grid_remove()
	
	Button(root,text="SUBMIT DETAILS",command=get_land).grid(row=13,column=2,sticky=W,pady=4)
	Button(root,text="TAKEOFF",command=takeoff).grid(row=2,column=2,sticky=W,pady=4)
	Button(root,text="LANDING",command=Landing).grid(row=2,column=4,sticky=W,pady=4)
	e1=Entry(root)
	e2=Entry(root)
	e3=Entry(root)
	e4=Entry(root)
	e5=Entry(root)
	e6=Entry(root)
	e7=Entry(root)
	Button(root, text='Quit', command=root.quit).grid(row=14, column=2, sticky=W, pady=4)
	
	mainloop( )

		


