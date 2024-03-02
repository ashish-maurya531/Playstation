'''
THIS IS A RACING GAME.
THERE ARE VARIOUS CARS. YOU CAN CHOOSE YOUR CAR
YOU CAN COMPETE WITH YOUR FRIENDS. AND BECAME A WINNER AS WELL AS RACER.
YOU REALLY FIND IT VERY ENJOYING.
'''
#importing modules
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import time
import sqlite3
import random
#MAKEING THE WHOLE CODE IN A FUNCTION TO CALL IT WHEN WE WANT TO PLAY THIS GAME
def startwindow():
	
	def playwindow():
		global play
		save.destroy()
		play=Tk()
		#THIS .attributes() IS TO OPEN GUI WINDOW IN FULLSCREEN MODE
		play.attributes("-fullscreen",True)
		play.geometry("1356x700")

		main_canvas=Canvas(play,bg='yellow',width=1366,height=768)
		main_canvas.place(x=0,y=0)
		up_canvas=Canvas(main_canvas,bg="red",height=30,width=1366)
		up_canvas.place(x=0,y=0)
		down_canvas=Canvas(main_canvas,bg="red",height=30,width=1366)
		down_canvas.place(x=0,y=735)
		left_canvas=Canvas(main_canvas,bg="red",height=768,width=30)
		left_canvas.place(x=0,y=0)
		right_canvas=Canvas(main_canvas,bg="red",height=768,width=30)
		right_canvas.place(x=1335,y=0)

		
	
		global finish1,finish2,p1_car,p2_car,filep1_1,filep1_2,filep1_3,filep1_4,filep1_5,filep1_6,filep1_7,filep1_8,filep1_9,filep1_10
		finish1=0
		finish2=0

		aaa=PhotoImage(file=p1_car)
		bbb=PhotoImage(file=p2_car)
		file_track=PhotoImage(file="images/track3.png")

		main_canvas.create_image(680,350,image=file_track)
		main_canvas.create_text(300,500,text="HOW TO PLAY ?",font=("Helvetia",20,"bold"),fill="blue")
		main_canvas.create_text(100,600,text="",font=("Helvetia",20,"bold"),fill="blue")
		main_canvas.create_text(350,550,text="1: Press START button to start race.",font=("Helvetia",20,"bold"),fill="blue")
		main_canvas.create_text(342,590,text=("2: coundown will we start 3-2-1-GO."),font=("Helvetia",20,"bold"),fill="blue")
		main_canvas.create_text(111,630,text=("3: "+PLAYER1+" will tap on A key from keyboard"),anchor=W,font=("Helvetia",20,"bold"),fill="blue")
		main_canvas.create_text(111,670,text=("4: "+PLAYER2+" will tap on L key from keyboard"),anchor=W,font=("Helvetia",20,"bold"),fill="blue")
		global inlead
		inlead=main_canvas.create_text(700,200,text="",font=("Helvetia",20,"bold"),fill="blue")
		car1_canvas=main_canvas.create_image(173,305,image=aaa)
		car2_canvas=main_canvas.create_image(173,400,image=bbb)
		main_canvas.create_text(210,100,text=(str(PLAYER1)).upper(),anchor=W,font=("Helvetia",50,"bold"),fill="blue")
		main_canvas.create_text(860,100,text=(str(PLAYER2)).upper(),anchor=W,font=("Helvetia",50,"bold"),fill="blue")
		file33=PhotoImage(file="images/VS34.png")
		main_canvas.create_image(580,20,image=file33,anchor=NW)
		car1=main_canvas.create_image(150,105,image=aaa)
		car2=main_canvas.create_image(800,100,image=bbb)
		coundown=main_canvas.create_text(650,200,text='',font=("Arial","50"),fill='green')
		global x,startrace_button
		x=3
		startrace_button=Button(main_canvas,text="  START  ",relief=FLAT,bg='black',fg="green",font=("Helvetia",20,"bold"),command=lambda:startrace(3))
		startrace_button.place(x=800,y=550)
		restart_button=Button(main_canvas,text="  RESTART  ",relief=FLAT,bg='black',font=("Helvetia",20,"bold"),fg="green",command=savewindow)
		restart_button.place(x=1000,y=550)
		def startrace(i):
			global x,startrace_button
			if i==-1:
				main_canvas.itemconfigure(coundown,text="")
				
				startrace_button.config(state=DISABLED)
				startrace_button.place(x=9000,y=600)
				
				return
			elif ((i==3) or (i==2) or (i==1)):
				main_canvas.itemconfigure(coundown,text=i)
				play.after(1000,lambda:startrace(i-1))
			elif i==0:
				main_canvas.itemconfigure(coundown,text="GO")
				
				play.bind('<a>',anim_car1)
				play.bind('<l>',anim_car2)
				play.bind('<A>',anim_car1)
				play.bind('<L>',anim_car2)
				play.after(1000,lambda:startrace(-1))

				
			



			
				
				

		def anim_car1(i):
			
			global finish1,finish2
			if finish1==70:
				conn=sqlite3.connect("race.db")
				c=conn.cursor()
				c.execute("UPDATE data SET winner='"+PLAYER1+"' WHERE p1='"+PLAYER1+"'")
				conn.commit()
				c.close()
				conn.close()
				main_canvas.itemconfigure(inlead,text=(str(PLAYER1)).upper()+" won the race!")
				message_win="Congrats!!!\n"+(str(PLAYER1)).upper()+" won the race."
				messagebox.showinfo("WINNWR!",message_win)
				mes=messagebox.askyesno("GAME OVER!!!","WAN\'T TO PLAY IT AGAIN")
				if (mes):
					savewindow()
				else:
					play.destroy()
					import playstationfile
					playstationfile.next2()

				play.unbind('<a>')
				play.unbind('<l>')
				play.unbind('<A>')
				play.unbind('<L>')
			else:
				finish1+=1
				x=15
				y=0
				main_canvas.move(car1_canvas,x,y)
				if (finish1>finish2):
					main_canvas.itemconfigure(inlead,text=(str(PLAYER1)).upper()+" has taken lead")
		def anim_car2(i):
			global finish2,finish1
			if finish2==70:
				conn=sqlite3.connect("race.db")
				c=conn.cursor()
				c.execute("UPDATE data SET winner='"+PLAYER2+"' WHERE p2='"+PLAYER2+"'")
				conn.commit()
				c.close()
				conn.close()
				main_canvas.itemconfigure(inlead,text=(str(PLAYER2)).upper()+" won the race!")
				message_win="Congrats!!!\n"+(str(PLAYER2)).upper()+" won the race."
				messagebox.showinfo("WINNWR!",message_win)
				mes=messagebox.askyesno("GAME OVER!!!","WAN\'T TO PLAY IT AGAIN")
				if (mes):
					savewindow()
				else:
					play.destroy()
					import playstationfile
					playstationfile.next2()
				play.unbind('<a>')
				play.unbind('<l>')
				play.unbind('<A>')
				play.unbind('<L>')
			else:
				finish2+=1
				x=15
				y=0
				main_canvas.move(car2_canvas,x,y)
				if (finish2>finish1):
					main_canvas.itemconfigure(inlead,text=(str(PLAYER2)).upper()+" has taken lead")


		def exitgame2():
			quitgame=messagebox.askyesno("QUIT THE GAME","ARE YOU REALLY WANT TO QUIT THE GAME")
			if (quitgame):
				try:
					play.destroy()
				except:
					pass
				startwindow()
		exit_button=Button(main_canvas,text="exit",relief=FLAT,bg='black',font=("Helvetia",15,"bold"),fg="green",command=exitgame2)
		exit_button.place(x=1284,y=697)

		
		



		play.mainloop()



	def savewindow():
		try:
			start.destroy()
		except:
			pass
		try:
			play.destroy()
		except:
			pass
		global save,P1entry,P2entry,filep1_1,filep1_2,filep1_3,filep1_4,filep1_5,filep1_6,filep1_7,filep1_8,filep1_9,filep1_10,p1_vehicle_choose,p1_car,p2_car,p2_vehicle_choose
		change_colour=1
		save=Tk()
		save.title("SAVE YOUR DATA")
		save.attributes("-fullscreen",True)
		save_canvas=Canvas(save,bg="cyan",height=770,width=1368)
		save_canvas.place(x=-1,y=-1)
		up_canvas=Canvas(save_canvas,bg="red",height=20,width=1366)
		up_canvas.place(x=0,y=0)
		down_canvas=Canvas(save_canvas,bg="red",height=20,width=1366)
		down_canvas.place(x=0,y=745)
		left_canvas=Canvas(save_canvas,bg="red",height=768,width=20)
		left_canvas.place(x=0,y=0)
		right_canvas=Canvas(save_canvas,bg="red",height=768,width=20)
		right_canvas.place(x=1345,y=0)
		############################
		file2=PhotoImage(file="images/PLAYER_ONE_xogame.png")
		file1=PhotoImage(file="images/PLAYER_TWO_xogame.png")
		filep1_1=PhotoImage(file="images/p1but11.png")
		filep1_2=PhotoImage(file="images/p1but12.png")
		filep1_3=PhotoImage(file="images/p1but13.png")
		filep1_4=PhotoImage(file="images/p1but14.png")
		filep1_5=PhotoImage(file="images/p1but15.png")
		filep1_6=PhotoImage(file="images/p1but21.png")
		filep1_7=PhotoImage(file="images/p1but22.png")
		filep1_8=PhotoImage(file="images/p1but23.png")
		filep1_9=PhotoImage(file="images/p1but24.png")
		filep1_10=PhotoImage(file="images/p1but25.png")
		save_canvas.create_text(1090,70,text="ENTER PLAYERS NAME",font=("Helvetia",32,"bold underline"),fill="blue")
		save_canvas.create_image(950,130,image=file2,anchor=NW)
		save_canvas.create_image(950,210,image=file1,anchor=NW)
		P1entry=Entry(save_canvas,width=15,font=('Arial',23,'bold'),borderwidth=0,bg="pink",justify="left",fg="black")
		P1entry.place(x=1055,y=140)
		P2entry=Entry(save_canvas,width=15,font=('Arial',23,'bold'),borderwidth=0,bg="pink",justify="left",fg="black")
		P2entry.place(x=1055,y=220)

		save_canvas.create_text(350,70,text="CHOOSE YOUR VEHICLE",font=("Helvetia",32,"bold underline"),fill="blue")
		save_canvas.create_text(350,130,text="LIST FOR PLAYER 1",font=("Helvetia",15,"bold underline"),fill="blue")
		save_canvas.create_text(350,440,text="LIST FOR PLAYER 2",font=("Helvetia",15,"bold underline"),fill="blue")
		
		p1_vehicle_choose=0
		p2_vehicle_choose=0
		

		def choose_vehicle(no):
			global p1_vehicle_choose,p1_car,p2_car,p2_vehicle_choose
			if str(no)=='p1_11':
				p1_vehicle_choose=1
				p1_car="images/p1but11.png"
				save_canvas.itemconfigure(p1_img,image=filep1_1)
			elif str(no)=='p1_12':
				p1_vehicle_choose=1
				p1_car="images/p1but12.png"
				save_canvas.itemconfigure(p1_img,image=filep1_2)
			elif str(no)=='p1_13':
				p1_vehicle_choose=1
				p1_car="images/p1but13.png"
				save_canvas.itemconfigure(p1_img,image=filep1_3)
			elif str(no)=='p1_14':
				p1_vehicle_choose=1
				p1_car="images/p1but14.png"
				save_canvas.itemconfigure(p1_img,image=filep1_4)
			elif str(no)=='p1_15':
				p1_vehicle_choose=1
				p1_car="images/p1but15.png"
				save_canvas.itemconfigure(p1_img,image=filep1_5)
			elif str(no)=='p1_21':
				p1_vehicle_choose=1
				p1_car="images/p1but21.png"
				save_canvas.itemconfigure(p1_img,image=filep1_6)
			elif str(no)=='p1_22':
				p1_vehicle_choose=1
				p1_car="images/p1but22.png"
				save_canvas.itemconfigure(p1_img,image=filep1_7)
			elif str(no)=='p1_23':
				p1_vehicle_choose=1
				p1_car="images/p1but23.png"
				save_canvas.itemconfigure(p1_img,image=filep1_8)
			elif str(no)=='p1_24':
				p1_vehicle_choose=1
				p1_car="images/p1but24.png"
				save_canvas.itemconfigure(p1_img,image=filep1_9)
			elif str(no)=='p1_25':
				p1_vehicle_choose=1
				p1_car="images/p1but25.png"
				save_canvas.itemconfigure(p1_img,image=filep1_10)





			#######################
			elif str(no)=='p2_11':
				p2_vehicle_choose=1
				p2_car="images/p1but11.png"
				save_canvas.itemconfigure(p2_img,image=filep1_1)
			elif str(no)=='p2_12':
				p2_vehicle_choose=1
				p2_car="images/p1but12.png"
				save_canvas.itemconfigure(p2_img,image=filep1_2)
			elif str(no)=='p2_13':
				p2_vehicle_choose=1
				p2_car="images/p1but13.png"
				save_canvas.itemconfigure(p2_img,image=filep1_3)
			elif str(no)=='p2_14':
				p2_vehicle_choose=1
				p2_car="images/p1but14.png"
				save_canvas.itemconfigure(p2_img,image=filep1_4)
			elif str(no)=='p2_15':
				p2_vehicle_choose=1
				p2_car="images/p1but15.png"
				save_canvas.itemconfigure(p2_img,image=filep1_5)
			elif str(no)=='p2_21':
				p2_vehicle_choose=1
				p2_car="images/p1but21.png"
				save_canvas.itemconfigure(p2_img,image=filep1_6)
			elif str(no)=='p2_22':
				p2_vehicle_choose=1
				p2_car="images/p1but22.png"
				save_canvas.itemconfigure(p2_img,image=filep1_7)
			elif str(no)=='p2_23':
				p2_vehicle_choose=1
				p2_car="images/p1but23.png"
				save_canvas.itemconfigure(p2_img,image=filep1_8)
			elif str(no)=='p2_24':
				p2_vehicle_choose=1
				p2_car="images/p1but24.png"
				save_canvas.itemconfigure(p2_img,image=filep1_9)
			elif str(no)=='p2_25':
				p2_vehicle_choose=1
				p2_car="images/p1but25.png"
				save_canvas.itemconfigure(p2_img,image=filep1_10)
			else:
				pass



		p1but11=Button(save_canvas,image=filep1_1,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_11'))
		p1but11.place(x=100,y=180)
		p1but12=Button(save_canvas,image=filep1_2,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_12'))
		p1but12.place(x=220,y=180)
		p1but13=Button(save_canvas,image=filep1_3,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_13'))
		p1but13.place(x=340,y=180)
		p1but14=Button(save_canvas,image=filep1_4,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_14'))
		p1but14.place(x=460,y=180)
		p1but15=Button(save_canvas,image=filep1_5,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_15'))
		p1but15.place(x=580,y=180)
		
		p1but21=Button(save_canvas,image=filep1_6,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_21'))
		p1but21.place(x=100,y=300)
		p1but22=Button(save_canvas,image=filep1_7,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_22'))
		p1but22.place(x=220,y=300)
		p1but23=Button(save_canvas,image=filep1_8,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_23'))
		p1but23.place(x=340,y=300)
		p1but24=Button(save_canvas,image=filep1_9,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_24'))
		p1but24.place(x=460,y=300)
		p1but25=Button(save_canvas,image=filep1_10,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p1_25'))
		p1but25.place(x=580,y=300)



		p2but11=Button(save_canvas,image=filep1_1,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_11'))
		p2but11.place(x=100,y=490)
		p2but12=Button(save_canvas,image=filep1_2,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_12'))
		p2but12.place(x=220,y=490)
		p2but13=Button(save_canvas,image=filep1_3,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_13'))
		p2but13.place(x=340,y=490)
		p2but14=Button(save_canvas,image=filep1_4,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_14'))
		p2but14.place(x=460,y=490)
		p2but15=Button(save_canvas,image=filep1_5,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_15'))
		p2but15.place(x=580,y=490)
		
		p2but21=Button(save_canvas,image=filep1_6,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_21'))
		p2but21.place(x=100,y=610)
		p2but22=Button(save_canvas,image=filep1_7,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_22'))
		p2but22.place(x=220,y=610)
		p2but23=Button(save_canvas,image=filep1_8,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_23'))
		p2but23.place(x=340,y=610)
		p2but24=Button(save_canvas,image=filep1_9,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_24'))
		p2but24.place(x=460,y=610)
		p2but25=Button(save_canvas,image=filep1_10,bg="cyan",relief=FLAT,command=lambda:choose_vehicle('p2_25'))
		p2but25.place(x=580,y=610)
		save_canvas.create_text(1150,350,text="PLAYER 1 SELECTED THIS VEHICLE:",font=("Helvetia",15,"bold underline"),fill="blue")
		save_canvas.create_text(1150,500,text="PLAYER 2 SELECTED THIS VEHICLE:",font=("Helvetia",15,"bold underline"),fill="blue")
		p1_img=save_canvas.create_image(1180,420,image=None)
		p2_img=save_canvas.create_image(1180,570,image=None)

		def save_data():
			global PLAYER1,PLAYER2,P1entry,P2entry
			PLAYER1=P1entry.get()
			PLAYER2=P2entry.get()
			
			
			if ((len(PLAYER1)==0) or (((str(PLAYER1)).isspace())==True)):
				messagebox.showwarning("Warning","Please enter valid username.")
			elif ((len(PLAYER1)==0) or (((str(PLAYER2)).isspace())==True)):
				messagebox.showwarning("Warning","Please enter valid username.")
			elif ((p1_vehicle_choose==0) and (p2_vehicle_choose==0)):
				messagebox.showwarning("Warning","Please choose your vehicle for race")
			elif (p1_vehicle_choose==0):
				messagebox.showwarning("Warning","Player1\nPlease choose your vehicle for race")
			elif (p2_vehicle_choose==0):
				messagebox.showwarning("Warning","Player2\nPlease choose your vehicle for race")
			else:
				conn=sqlite3.connect("race.db")
				c=conn.cursor()
				c.execute("""CREATE TABLE IF NOT EXISTS data(
					p1 VARCHAR(10),
					p2 VARCHAR(10),
					winner VARCHAR(10));""")
				c.execute("INSERT INTO data(p1,p2,winner) VALUES('"+PLAYER1+"','"+PLAYER2+"','"+"No"+"')")
				conn.commit()
				c.close()
				conn.close()
				playwindow()
		button_save=Button(save_canvas,text="  SAVE  ",borderwidth=0,relief=FLAT,bg="red",fg="black",font=("Arial",15,"bold"),command=save_data)
		button_save.place(x=1160,y=630)
		def exit_back():
			save.destroy()
			startwindow()
		button_exit=Button(save_canvas,text="  EXIT  ",borderwidth=0,relief=FLAT,bg="red",fg="black",font=("Arial",18,"bold"),command=exit_back)
		button_exit.place(x=1160,y=680)
		############################








		save.mainloop()
	start=Tk()
	start.title("ULTIMATE RACING GAME")
	start.attributes("-fullscreen",True)
	play_canvas=Canvas(start,height=769,width=1368)
	play_canvas.place(x=-1,y=-1)
	file_image=PhotoImage(file='images/play1.png')
	play_canvas.create_image(0,0,image=file_image,anchor=NW)
	
	

	def led():
		global ledvalue
		start.destroy()
		led=Tk()
		led.title("tic tac toe GAME SCOREBOARD")
		led.attributes('-fullscreen',True)
		led.resizable(0,0)
		led.configure(bg="yellow")
		ledcanvas=Canvas(led,height=180,width=1362,bg="yellow")
		ledcanvas.place(x=-1,y=-1)
		file_led1=PhotoImage(file='images/led1_xogame.png')
		ledcanvas.create_image(510,25,image=file_led1)
		ledcanvas.create_image(96,25,image=file_led1)
		
		iiiiii=ledcanvas.create_image(110,25,image=file_led1)
		iiiiii1=ledcanvas.create_image(96,25,image=file_led1)
		ledtext1=ledcanvas.create_text(710,50,text="LEADERBOARD",font=('Arial',60,'bold underline'),fill="blue")
		
		lcanvas=Canvas(led,height=530,width=1356,bg="yellow")
		lcanvas.place(x=5,y=180)
		

		tab=ttk.Treeview(lcanvas,columns=(1,2,3),show="headings",height=25)
		tab.place(x=400,y=0)
		
		tab.heading(1,text="     PLAYER 1 NAME    ")
		tab.heading(2,text="     PLAYER 2 NAME    ")
		tab.heading(3,text="   WINNER   ")

		conn=sqlite3.connect("race.db")
		c=conn.cursor()
		c.execute("SELECT * FROM data")
		rec=c.fetchall()
		for a in rec:
			tab.insert('', 'end', values=(a[0], a[1], a[2]))
		

		c.close()
		conn.close()
			
		def back1111():
			global ledvalue
			led.destroy()
			startwindow()
		back=Button(led,text="BACK",borderwidth=0,bg="red",relief=FLAT,width=15,fg="black",font=("Arial",18,"bold"),command=back1111)
		back.place(x=570,y=725)
	global name
	name=play_canvas.create_text(500,150,text="STREET\nRACING GAME",font=("Arial",90,"bold"),fill="blue")
	def exit_game():
		exit_gamegame=messagebox.askyesno("Warning!!!","ARE YOU REALLY WANT TO EXIT THE GAME")
		if (exit_gamegame):
			try:
				start.destroy()
			except:
				pass
			try:
				save.destroy()
			except:
				pass
			try:
				play.destroy()
			except:
				pass
			import playstationfile
			playstationfile.next2()
	

	play_button=Button(start,text="PLAY",bg="red",relief=FLAT,width=11,fg="black",font=("Arial",18,"bold"),command=lambda:change(1))
	play_button.place(x=640,y=650)
	led_button=Button(start,text="LEADERBOARD",bg="red",relief=FLAT,width=13,fg="black",font=("Arial",18,"bold"),command=led)
	led_button.place(x=250,y=650)
	exit_button=Button(start,text="EXIT",bg="red",relief=FLAT,width=11,fg="black",font=("Arial",18,"bold"),command=exit_game)
	exit_button.place(x=1000,y=650)
	def change(z):
		if z==1:
			savewindow()
		else:
			aaaa=("red","green","black","blue","brown")
			play_canvas.itemconfigure(name,fill=random.choice(aaaa))
			start.after(300,lambda:change(0))
			
	change(0)	







	start.mainloop()

