'''
                                        PLAYSTATION --THE WORLD OF GAMING 
                                    THIS APP PROVIDE YOU TO PLAY VARIOUS GAMES. 
                 THE PURPOSE OF MAKING THIS APP IS TO PLAY GAMES AND MAKE YOUR MIND STRESS FREE.
                                YOU CAN COMPETE WITH YOUR FRIENDS AND HAVE FUN......
'''
#THIS IS THE CODE FOR MAIN WINDOW (INTRODUCTION)
#importing modules

from tkinter import*
from tkinter import messagebox
import random
from tkinter import ttk
#CALLING OTHER PYTHON FILES OF THIS GAME
from jumbled_words import jumbledwords
from memory_game import memorygame
from tic_tac_toe import xo
from racing_game import racinggame


inital=1

#function to open first page
def give_inital(ii):
	global inital
	if ii==1:
		inital=0
		playstationmain()
	else:
		inital=0
		pass
def next2():
	try:
		playstation2.destroy()
	except:
		pass
	global playstation3,inital
	inital=0
	playstation3=Tk()
	playstation3.title("Playstation =>Game List")
	#THIS .attributes() IS TO OPEN GUI WINDOW IN FULLSCREEN MODE
	playstation3.attributes("-fullscreen",True)
	playstation3_canvas=Canvas(playstation3,height=768,width=1366)
	playstation3_canvas.place(x=-1,y=-1)
	
	#THE PHOTO IMAGE IS USE TO OPEN IMAGES IN GUI
	fileback1=PhotoImage(file="images/playstation_back1.png")

	playback=playstation3_canvas.create_image(0,0,image=fileback1,anchor=NW)
	
	file5=PhotoImage(file="images/moving_line.png")
	file6=PhotoImage(file="images/moving_line_verticle.png")
	file7=PhotoImage(file="images/logo1_playstation2.png")
	file8=PhotoImage(file="images/namelogo1_playstation2.png")
	file9=PhotoImage(file="images/but_xo2.png")
	file10=PhotoImage(file="images/but_jumbled3.png")
	file11=PhotoImage(file="images/but_memorygame2.png")
	file12=PhotoImage(file="images/but_racing.png")
	playstation3_canvas.create_image(50,50,image=file7,anchor=NW)
	playstation3_canvas.create_image(300,70,image=file8,anchor=NW)
	#THIS FUNCTION IS FOR ANIMATING THE BORDER OF MAIN PAGE
	def animation01(i):
		if i==1360:
			
			i=0
			animation01(0)

		else:

			
			moving_line_img=playstation3_canvas.create_image(i,0,image=file5,anchor=NW)
			moving_line_img=playstation3_canvas.create_image(i,740,image=file5,anchor=NW)
			playstation3.after(1,lambda:animation01(i+40))
	animation01(0)


	

	def animation04(i):
		if i==780:
			
			i=0
			animation04(0)

		else:

			moving_line_img=playstation3_canvas.create_image(0,i,image=file6,anchor=NW)
			moving_line_img=playstation3_canvas.create_image(1340,i,image=file6,anchor=NW)

			playstation3.after(1,lambda:animation04(i+30))
	animation04(0)




	#BUIDING BUTTONS TO CHOOSE YOUR GAME TO PLAY
	button1=Button(playstation3_canvas,text="memory game",image=file11,command=lambda:execute(1))
	button1.place(x=500,y=300)
	button2=Button(playstation3_canvas,text="jumbbled game",image=file10,command=lambda:execute(2))
	button2.place(x=500,y=500)
	button3=Button(playstation3_canvas,text="xo game",image=file9,command=lambda:execute(3))
	button3.place(x=900,y=300)
	button4=Button(playstation3_canvas,text="racing game",image=file12,command=lambda:execute(4))
	button4.place(x=100,y=300)
	
	button4=Button(playstation3_canvas,text="EXIT",bg='red',relief=FLAT,activebackground="black",activeforeground="red",font=("Arial","15","bold"),command=quit)
	button4.place(x=1281,y=700)
	#THIS FUNCTION IS TO INITIALIZE THE OTHER MAIN FUNCTION IN OTHER .py
	def execute(a):
		if a==1:
			try:
				playstation3.destroy()
			except:
				pass
			#OPENING MEMORY GAME
			memorygame.memorymain()
			
		elif a==2:
			try:
				playstation3.destroy()
			except:
				pass
			#OPENING JUMBLED WORD GAME
			jumbledwords.main()
		elif a==3:
			try:
				playstation3.destroy()
			except:
				pass
			#OPENING TIC TAC TOE GAME 
			xo.xomain()
		elif a==4:
			try:
				playstation3.destroy()
			except:
				pass
			#OPENING STREET RACING GAME 
			racinggame.startwindow()
			

	playstation3.mainloop()

def next1():
	try:
		playstation.destroy()
	except:
		pass
	global playstation2,inital
	inital=0
	playstation2=Tk()
	playstation2.title("Playstation =>About")
	playstation2.attributes("-fullscreen",True)
	playstation2_canvas=Canvas(playstation2,height=768,width=1366,bg="YELLOW")
	playstation2_canvas.place(x=-1,y=-1)
	
	button1=Button(playstation2_canvas,text="NEXT",command=next2,relief=FLAT,font=('Arial','20',"bold"),bg='black',fg="green",activebackground="green",activeforeground="black")
	button1.place(x=650,y=680)
	file5=PhotoImage(file="images/moving_line.png")
	file6=PhotoImage(file="images/moving_line_verticle.png")
	playstation2_canvas.create_text(700,200,text="ABOUT: ",font=('Arial','50',"bold"),fill='blue')
	playstation2_canvas.create_text(750,310,text="DESIGNED AND DEVELOPED BY:",font=('Arial','40',"bold"),fill='blue')
	playstation2_canvas.create_text(720,450,text="ASHISH MAURYA",font=('Arial','50',"bold"),fill='blue')
	
	#playstation2_canvas.create_text(575,380,text="2: NIKHIL DIXIT",font=('Arial','30',"bold"),fill='blue')
	#playstation2_canvas.create_text(650,500,text="GUIDED BY:",font=('Arial','40',"bold"),fill='blue')
	#playstation2_canvas.create_text(650,580,text="MR.RAMESH BHATT",font=('Arial','30',"bold"),fill='blue')
	#playstation2_canvas.create_text(950,620,text="PGT- Computer Science",font=('Arial','20',"bold"),fill='blue')
	def animation01(i):
		if i==1360:
			
			i=0
			animation01(0)

		else:

			
			moving_line_img=playstation2_canvas.create_image(i,0,image=file5,anchor=NW)
			moving_line_img=playstation2_canvas.create_image(i,740,image=file5,anchor=NW)
			playstation2.after(1,lambda:animation01(i+40))
	animation01(0)

	
	def animation04(i):
		if i==780:
			
			i=0
			animation04(0)

		else:

			moving_line_img=playstation2_canvas.create_image(0,i,image=file6,anchor=NW)
			moving_line_img=playstation2_canvas.create_image(1340,i,image=file6,anchor=NW)

			playstation2.after(1,lambda:animation04(i+30))
	animation04(0)




	playstation2.mainloop()
def playstationmain():
	





	


 
	global playstation,x,y,give_inital
	x=-185
	y=-180
	inital=0
	playstation=Tk()
	playstation.title("PLAYSTATION 1.0")
	playstation.attributes("-fullscreen",True)
	canvas=Canvas(playstation,bg="yellow",height=768,width=1366)
	canvas.place(x=-3,y=-3)
	logo1_canvas=Canvas(canvas,width=817,height=185,bg="yellow")
	logo1_canvas.place(x=280,y=200)
	file1=PhotoImage(file='images/logo1_playstation.png')
	file2=PhotoImage(file='images/namelogo1_playstation.png')
	file5=PhotoImage(file="images/moving_line.png")
	file6=PhotoImage(file="images/moving_line_verticle.png")


	button4=Button(canvas,text="EXIT",bg='red',relief=FLAT,activebackground="black",activeforeground="red",font=("Arial","15","bold"),command=quit)
	button4.place(x=1281,y=700)

	def amination1(i):
		if i==-1:

			return
			
		else:
			logo1_img=logo1_canvas.create_image(-1,i,image=file1,anchor=NW)
			playstation.after(1,lambda:amination1(i-3))
			
	amination1(185)
	namelogo1_canvas=Canvas(canvas,width=817,height=185,bg="yellow")
	namelogo1_canvas.place(x=280,y=395)
	canvas.create_line(276,198,1104,198,width=8,fill="black")
	canvas.create_line(280,393,1100,393,width=8,fill="black")
	canvas.create_line(280,585,1104,586,width=8,fill="black")
	canvas.create_line(277,195,277,590,width=8,fill="black")
	canvas.create_line(1104,194,1104,590,width=8,fill="black")
	def amination2(i):
		if i==-1:
			canvas.create_text(700,608,text="EXPERIENCE THE WORLD OF GAMING",font=('Arial','20',"bold"),fill='blue')
			canvas.create_text(710,650,text="LOADING....",font=('Arial','15',"bold"),fill='black')
			playstation.after(500,lambda:animation3(0))

			return
			
		else:
			logo1_img=namelogo1_canvas.create_image(-1,i,image=file2,anchor=NW)
			playstation.after(1,lambda:amination2(i-3))
	playstation.after(300,lambda:amination2(185))
	def animation01(i):
		if i==1360:
			
			i=0
			animation01(0)

		else:

			
			moving_line_img=canvas.create_image(i,0,image=file5,anchor=NW)
			moving_line_img=canvas.create_image(i,740,image=file5,anchor=NW)
			playstation.after(1,lambda:animation01(i+40))
	animation01(0)


	



	def animation04(i):
		if i==780:
			
			i=0
			animation04(0)

		else:

			moving_line_img=canvas.create_image(0,i,image=file6,anchor=NW)
			moving_line_img=canvas.create_image(1340,i,image=file6,anchor=NW)

			playstation.after(1,lambda:animation04(i+30))
	animation04(0)



	
	
			
	
	
	loading_canvas=Canvas(canvas,width=650,height=41,bg="yellow")
	loading_canvas.place(x=400,y=670)
	file3=PhotoImage(file="images/LOADING_BAR.png")
	file4=PhotoImage(file="images/LOADING_GREEN_BAR.png")
	
	
	def animation3(i):
		if i==0:
			loading_bar=loading_canvas.create_image(326,22,image=file3)
		elif i==339:
			pass
			playstation.after(2000,next1)
			
			
		else:
			loading_green_bar=loading_canvas.create_image(i,22,image=file4)
			playstation.after(70,lambda:animation3(i+20))
			
	
	playstation.after(6000,lambda:animation3(99))
	
	

	


	playstation.mainloop()

give_inital(inital)