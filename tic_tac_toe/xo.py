'''
THIS IS A TIC TAC TOE GAME.
YOU CAN PLAY WITH CPU OR
YOU CAN COMPETE WITH YOUR FRIENDS. AND BECAME A WINNER .
YOU REALLY FIND IT VERY ENJOYING.
'''

from tkinter import*
from tkinter import messagebox
import time
import random
import sqlite3

from tkinter import ttk

i=1
#MAKEING THE WHOLE CODE IN A FUNCTION TO CALL IT WHEN WE WANT TO PLAY THIS GAME
def xomain():
	def game_over(who_win):
		try:
			sp_game.destroy()
		except:
			pass
		try:
			mp_game.destroy()
		except:
			pass
		g_over=Tk()
		#THIS .attributes() IS TO OPEN GUI WINDOW IN FULLSCREEN MODE
		g_over.attributes("-fullscreen",True)
		g_over_canvas=Canvas(g_over,width=1366,height=768)
		g_over_canvas.place(x=-1,y=-1)
		file4=PhotoImage(file="images/gameover_xogame.png")
		g_over_canvas.create_image(-1,-1,image=file4,anchor=NW)
		result_text=g_over_canvas.create_text(530,40,text=str(who_win)+" wins",font=('Arial',50,'bold underline'),fill="blue")
		g_over.mainloop()
	def exitgame(event):
		if event==11:
			try:
				sp_game.destroy()
			except:
				pass
				
			try:
				mp_game.destroy()
			except:
				pass
			choose()

		else:		
		    quitgame=messagebox.askyesno("QUIT THE GAME","ARE YOU REALLY WANT TO QUIT THE GAME")
		    if (quitgame):
		    	try:
		    		sp_game.destroy()
		    	except:
		    		pass
		    	try:
		    		mp_game.destroy()
		    	except:
		    		pass
		    	try:
		    		start_mp.destroy()
		    	except:
		    		pass
		    	try:
		    		start_sp.destroy()
		    	except:
		    		pass
		    	try:
		    		start.destroy()
		    	except:
		    		pass
		    	import playstationfile
		    	inital=0
		    	playstationfile.next2()
	def mpgame():
		global file2,mp_game
		
		try:
			start_mp.destroy()
		except:
			pass

		mp_game=Tk()
		mp_game.title("PLAYER V/S PLAYER MODE")
		mp_game.attributes("-fullscreen",True)
		mp_game_canvas=Canvas(mp_game,width=1366,height=768,bg="black")
		mp_game_canvas.place(x=-2,y=-2)
		button_exit=Button(mp_game_canvas,text="EXIT",borderwidth=0,relief=FLAT,bg="red",width=10,fg="black",font=("Arial",18,"bold"),command=lambda:exitgame(11))
		button_exit.place(x=1100,y=680)
		file2=PhotoImage(file="images/mpsp_xogame.png")
		file3=PhotoImage(file="images/VS33_xogame.png")
		
		mp_game_canvas.create_image(-1,-1,image=file2,anchor=NW)
		mp_game_canvas.create_image(530,5,image=file3,anchor=NW)
		
		mp_game_canvas.create_text(300,120,text=(str(PLAYER1_MP)).upper(),font=("Helvetia",50,"bold underline"),fill="magenta")
		mp_game_canvas.create_text(1050,120,text=(str(PLAYER2_MP)).upper(),font=("Helvetia",50,"bold underline"),fill="magenta")
		mp_game_canvas.create_text(1040,330,text="TURN OF:",font=("Helvetia",20,"bold"),fill="red")
		aaa=mp_game_canvas.create_text(1180,330,text=(str(PLAYER1_MP)).upper(),font=("Helvetia",20,"bold"),fill="red")
		file100=PhotoImage(file="images/boy1_xogame.png")
		mp_game_canvas.create_image(535,60,image=file100,anchor=NW)
		mp_game_canvas.create_image(760,60,image=file100,anchor=NW)
		winx='HURRAH !'+' \"'+(str(PLAYER1_MP)).upper()+'\"'+" WINS"
		wino='HURRAH !'+' \"'+(str(PLAYER2_MP)).upper()+'\"'+" WINS"
		errorx='INVALID MOVE BY PLAYER \"'+(str(PLAYER1_MP)).upper()+'\"'+'\n TRY AGAIN'
		erroro='INVALID MOVE BY PLAYER \"'+(str(PLAYER2_MP)).upper()+'\"'+'\n TRY AGAIN'
		filecross=PhotoImage(file='images/cross1_xogame.png')
		fileo=PhotoImage(file='images/o1_xogame.png')
		
		def process(b):
			global i
			if(i%2==1):
				if(b['text']==''):
					b['text']='X'
					b['height']=97
					b['width']=100
					b['image']=filecross
					
					b['fg']='red'
					i=i+1
					mp_game_canvas.itemconfigure(aaa,text=(str(PLAYER2_MP)).upper())
				elif(b['text']=='X' or b['text']=='O'):
					messagebox.showinfo('ERROR',errorx)
			elif(i%2==0):
				if(b['text']==''):
					b['text']='O'
					b['height']=97
					b['image']=fileo
					b['width']=100
					b['fg']='blue'
					i=i+1
					mp_game_canvas.itemconfigure(aaa,text=(str(PLAYER1_MP)).upper())
				elif(b['text']=='X' or b['text']=='O'):
					messagebox.showinfo('ERROR',erroro)
			if(b1['text']==b2['text']==b3['text']=='X' or 
				b4['text']==b5['text']==b6['text']=='X' or
	            b7['text']==b8['text']==b9['text']=='X' or
	            b1['text']==b4['text']==b7['text']=='X' or
	            b2['text']==b5['text']==b8['text']=='X' or
	            b3['text']==b6['text']==b9['text']=='X' or
	            b1['text']==b5['text']==b9['text']=='X' or
	        	b3['text']==b5['text']==b7['text']=='X'):
					#game_over('X')
					messagebox.showinfo('GAME OVER',winx)
					
					conn1=sqlite3.connect("tic1.db")
					c1=conn1.cursor()
					c1.execute("UPDATE data1 SET winner='"+PLAYER1_MP+"' WHERE p2='"+PLAYER2_MP+"'")
				
					print(PLAYER1_MP)
					conn1.commit()
					c1.close()
					conn1.close()

					ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
					if(ans=='yes'):
						i=1
						mp_game.destroy()
						MULTIPLATER_player()
					elif(ans=='no'):
						i=1
						mp_game.destroy()
						choose()
					
			if(b1['text']==b2['text']==b3['text']=='O' or
	            b4['text']==b5['text']==b6['text']=='O' or
	            b7['text']==b8['text']==b9['text']=='O' or
	            b1['text']==b4['text']==b7['text']=='O' or
	            b2['text']==b5['text']==b8['text']=='O' or
	            b3['text']==b6['text']==b9['text']=='O' or
	            b1['text']==b5['text']==b9['text']=='O' or
	            b3['text']==b5['text']==b7['text']=='O'):
					#game_over("O")
					
					messagebox.showinfo('GAME OVER',wino)
					conn1=sqlite3.connect("tic1.db")
					c1=conn1.cursor()
					c1.execute("UPDATE data1 SET winner= '"+PLAYER2_MP+"' WHERE p1='"+PLAYER1_MP+"'")
					print(PLAYER2_MP)
					conn1.commit()
					c1.close()
					
					conn1.close()
					ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
					if(ans=='yes'):
						i=1
						mp_game.destroy()
						MULTIPLATER_player()
					elif(ans=='no'):
						i=1
						mp_game.destroy()
						choose()
			if(i>=10):
				conn=sqlite3.connect('tic1.db')
				c=conn.cursor()
				c.execute("UPDATE data1 SET winner='"+"GAME TIE"+"' WHERE p1='"+PLAYER1_MP+"'")
				conn.commit()
				c.close()
				conn.close()
				
				messagebox.showinfo('GAME OVER','OPPS!\nGAME TIE.')
				ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
				if(ans=='yes'):
					i=1
					mp_game.destroy()
					MULTIPLATER_player()
				elif(ans=='no'):
					i=1
					mp_game.destroy()
					choose()

		b1=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b1))
		b1.place(x=450,y=300)
		b2=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b2))
			
		b2.place(x=590,y=300)
		b3=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b3))
		b3.place(x=730,y=300)
		b4=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b4))
		b4.place(x=450,y=430)
		b5=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b5))
		b5.place(x=590,y=430)
		b6=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b6))
		b6.place(x=730,y=430)
		b7=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b7))
		b7.place(x=450,y=550)
		b8=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b8))
		b8.place(x=590,y=550)
		b9=Button(mp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',activebackground="pink",fg='black',command=lambda:process(b9))
		b9.place(x=730,y=550)

		#font=('Algerian','20')

		mp_game.mainloop()

	def spgame():
		global file2,sp_game
		
		try:
			start_sp.destroy()
		except:
			pass

		sp_game=Tk()
		sp_game.title("PLAYER V/S PLAYER MODE")
		sp_game.attributes("-fullscreen",True)
		sp_game_canvas=Canvas(sp_game,width=1366,height=768,bg="black")
		sp_game_canvas.place(x=-2,y=-2)
		file2=PhotoImage(file="images/mpsp_xogame.png")
		
		sp_game_canvas.create_image(-1,-1,image=file2,anchor=NW)
		file3=PhotoImage(file="images/VS33_xogame.png")
		sp_game_canvas.create_image(540,10,image=file3,anchor=NW)
		
		button_exit=Button(sp_game_canvas,text="EXIT",borderwidth=0,relief=FLAT,bg="red",width=13,fg="black",font=("Arial",18,"bold"),command=lambda:exitgame(11))
		button_exit.place(x=1080,y=720)
		
		sp_game_canvas.create_text(300,120,text=(str(PLAYER1_SP)).upper(),font=("Helvetia",50,"bold underline"),fill="magenta")
		sp_game_canvas.create_text(1030,120,text='CPU',font=("Helvetia",50,"bold underline"),fill="magenta")
		file12=PhotoImage(file="images/boy1_xogame.png")
		file13=PhotoImage(file="images/cpu1_xogame.png")
		sp_game_canvas.create_image(535,60,image=file12,anchor=NW)
		sp_game_canvas.create_image(780,60,image=file13,anchor=NW)
		
		winx='HURRAH !'+' \"'+(str(PLAYER1_SP)).upper()+'\"'+" WINS"
		errorx='INVALID MOVE BY PLAYER \"'+(str(PLAYER1_SP)).upper()+'\"'+'\n TRY AGAIN.'
		wino='OOPS! \nCPU WINS'
		filecross=PhotoImage(file='images/cross1_xogame.png')
		fileo=PhotoImage(file='images/o1_xogame.png')
		

		############################
		def process(b):
                        global i
                        def checkwin():
                                global i
	                
                                if(b1['text']==b2['text']==b3['text']=='X' or
                                   b4['text']==b5['text']==b6['text']=='X' or
                                   b7['text']==b8['text']==b9['text']=='X' or
                                   b1['text']==b4['text']==b7['text']=='X' or
                                   b2['text']==b5['text']==b8['text']=='X' or
                                   b3['text']==b6['text']==b9['text']=='X' or
                                   b1['text']==b5['text']==b9['text']=='X' or
                                   b3['text']==b5['text']==b7['text']=='X'):
                                        messagebox.showinfo('GAME OVER',winx)
                                        
                                     
                                        conn=sqlite3.connect('tic.db')
                                        c=conn.cursor()
                                        c.execute("UPDATE data SET winner='"+PLAYER1_SP+"' WHERE p1='"+PLAYER1_SP+"'")
                                        conn.commit()
                                        c.close()
                                        conn.close()
                                        ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
                                        if(ans=='yes'):
                                                i=1
                                                sp_game.destroy()
                                                single_player()
                                        elif(ans=='no'):
                                                i=1
                                                sp_game.destroy()
                                                choose()

                                if(b1['text']==b2['text']==b3['text']=='O' or
                                   b4['text']==b5['text']==b6['text']=='O' or
                                   b7['text']==b8['text']==b9['text']=='O' or
                                   b1['text']==b4['text']==b7['text']=='O' or
                                   b2['text']==b5['text']==b8['text']=='O' or
                                   b3['text']==b6['text']==b9['text']=='O' or
                                   b1['text']==b5['text']==b9['text']=='O' or
                                   b3['text']==b5['text']==b7['text']=='O'):
                                        messagebox.showinfo('GAME OVER',wino)
                                        
                                     
                                        conn=sqlite3.connect('tic.db')
                                        c=conn.cursor()
                                        c.execute("UPDATE data SET winner='"+"CPU"+"' WHERE p1='"+PLAYER1_SP+"'")
                                        conn.commit()
                                        c.close()
                                        conn.close()
                                        ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
                                        if(ans=='yes'):
                                                i=1
                                                sp_game.destroy()
                                                single_player()
                                        elif(ans=='no'):
                                                i=1
                                                sp_game.destroy()
                                                choose()

                                if(i>=10):
                                        messagebox.showinfo('GAME OVER','OPPS!\nGAME TIE.')
                                        
                                
                                        conn=sqlite3.connect('tic.db')
                                        c=conn.cursor()
                                        c.execute("UPDATE data SET winner='"+"Game Tie"+"' WHERE id='"+PLAYER1_SP+"'")
                                        conn.commit()
                                        c.close()
                                        conn.close()
                                        ans=messagebox.askquestion("GAME OVER",'WANNA PLAY AGAIN?')
                                        if(ans=='yes'):
                                            i=1
                                            sp_game.destroy()
                                            single_player()
                                        elif(ans=='no'):
                                                i=1
                                                sp_game.destroy()
                                                choose()

                        def pcturn():
                                global i
                                if(i%2==0):

                                    #try to win moves....
	                    
                                    if((b2['text']==b3['text']=='O' or b4['text']==b7['text']=='O' or b5['text']==b9['text']=='O')and b1['text']==''):
                                        b1['text']='O'
                                        b1['height']=97
                                        b1['width']=100
                                        b1['image']=fileo
                                        b1['fg']='blue'

                                    elif((b1['text']==b3['text']=='O' or b5['text']==b8['text']=='O')and b2['text']==''):
                                        b2['text']='O'
                                        b2['height']=97
                                        b2['width']=100
                                        b2['image']=fileo
                                        b2['fg']='blue'

                                    elif((b1['text']==b2['text']=='O' or b5['text']==b7['text']=='O' or b6['text']==b9['text']=='O')and b3['text']==''):
                                        b3['text']='O'
                                        b3['height']=97
                                        b3['width']=100
                                        b3['image']=fileo

                                        b3['fg']='blue'
	                    
                                    elif((b1['text']==b7['text']=='O' or b5['text']==b6['text']=='O')and b4['text']==''):
                                        b4['text']='O'
                                        b4['height']=97
                                        b4['width']=100
                                        b4['image']=fileo
                                        b4['fg']='blue'

                                    elif((b2['text']==b8['text']=='O' or b3['text']==b7['text']=='O' or b4['text']==b6['text']=='O' or b1['text']==b9['text']=='O')and b5['text']==''):
                                        b5['text']='O'
                                        b5['height']=97
                                        b5['width']=100
                                        b5['image']=fileo
                                        b5['fg']='blue'

                                    elif((b3['text']==b7['text']=='O' or b4['text']==b5['text']=='O')and b6['text']==''):
                                        b6['text']='O'
                                        b6['height']=97
                                        b6['width']=100
                                        b6['image']=fileo
                                        b6['fg']='blue'
                                    
                                    elif((b1['text']==b4['text']=='O' or b3['text']==b5['text']=='O' or b8['text']==b9['text']=='O')and b7['text']==''):
                                        b7['text']='O'
                                        b7['height']=97
                                        b7['width']=100
                                        b7['image']=fileo
                                        b7['fg']='blue'

                                    elif((b2['text']==b5['text']=='O' or b7['text']==b9['text']=='O')and b8['text']==''):
                                        b8['text']='O'
                                        b8['height']=97
                                        b8['width']=100
                                        b8['image']=fileo
                                        b8['fg']='blue'

                                    elif((b1['text']==b5['text']=='O' or b3['text']==b6['text']=='O' or b7['text']==b8['text']=='O')and b9['text']==''):
                                        b9['text']='O'
                                        b9['height']=97
                                        b9['width']=100
                                        b9['image']=fileo
                                        b9['fg']='blue'


                                    #defence moves.....

                                        
                                    elif((b2['text']==b3['text']=='X' or b4['text']==b7['text']=='X' or b5['text']==b9['text']=='X')and b1['text']==''):
                                        b1['text']='O'
                                        b1['height']=97
                                        b1['width']=100
                                        b1['image']=fileo
                                        b1['fg']='blue'

                                    elif((b1['text']==b3['text']=='X' or b5['text']==b8['text']=='X')and b2['text']==''):
                                        b2['text']='O'
                                        b2['height']=97
                                        b2['width']=100
                                        b2['image']=fileo
                                        b2['fg']='blue'

                                    elif((b1['text']==b2['text']=='X' or b5['text']==b7['text']=='X' or b6['text']==b9['text']=='X')and b3['text']==''):
                                        b3['text']='O'
                                        b3['height']=97
                                        b3['width']=100
                                        b3['image']=fileo
                                        b3['fg']='blue'
                                    
                                    elif((b1['text']==b7['text']=='X' or b5['text']==b6['text']=='X')and b4['text']==''):
                                        b4['text']='O'
                                        b4['height']=97
                                        b4['width']=100
                                        b4['image']=fileo
                                        b4['fg']='blue'

                                    elif((b2['text']==b8['text']=='X' or b3['text']==b7['text']=='X' or b4['text']==b6['text']=='X' or b1['text']==b9['text']=='X')and b5['text']==''):
                                        b5['text']='O'
                                        b5['height']=97
                                        b5['width']=100
                                        b5['image']=fileo
                                        b5['fg']='blue'

                                    elif((b3['text']==b9['text']=='X' or b4['text']==b5['text']=='X')and b6['text']==''):
                                        b6['text']='O'
                                        b6['height']=97
                                        b6['width']=100
                                        b6['image']=fileo
                                        b6['fg']='blue'
                                    
                                    elif((b1['text']==b4['text']=='X' or b3['text']==b5['text']=='X' or b8['text']==b9['text']=='X')and b7['text']==''):
                                        b7['text']='O'
                                        b7['height']=97
                                        b7['width']=100
                                        b7['image']=fileo
                                        b7['fg']='blue'

                                    elif((b2['text']==b5['text']=='X' or b7['text']==b9['text']=='X')and b8['text']==''):
                                        b8['text']='O'
                                        b8['height']=97
                                        b8['width']=100
                                        b8['image']=fileo
                                        b8['fg']='blue'

                                    elif((b1['text']==b5['text']=='X' or b3['text']==b6['text']=='X' or b7['text']==b8['text']=='X')and b9['text']==''):
                                        b9['text']='O'
                                        b9['height']=97
                                        b9['width']=100
                                        b9['image']=fileo
                                        b9['fg']='blue'

                                    #basic moves..... 
                                    

                                    elif(b5['text']==''):
                                        b5['text']='O'
                                        b5['height']=97
                                        b5['width']=100
                                        b5['image']=fileo
                                        b5['fg']='blue'

                                    elif(b1['text']==''):
                                        b1['text']='O'
                                        b1['height']=97
                                        b1['width']=100
                                        b1['image']=fileo
                                        b1['fg']='blue'

                                    elif(b3['text']==''):
                                        b3['text']='O'
                                        b3['height']=97
                                        b3['width']=100
                                        b3['image']=fileo
                                        b3['fg']='blue'
                                        

                                    elif(b7['text']==''):
                                        b7['text']='O'
                                        b7['height']=97
                                        b7['width']=100
                                        b7['image']=fileo
                                        b7['fg']='blue'

                                    elif(b9['text']==''):
                                        b9['text']='O'
                                        b9['height']=97
                                        b9['width']=100
                                        b9['image']=fileo
                                        b9['fg']='blue'    
                                i=i+1
                                checkwin()

                     
                                    

                        if(i%2==1):
                                if(b['text']==''):
                                 b['text']='X'
                                 b['image']=filecross
                                 b['height']=97
                                 b['width']=100

                                 b['fg']='red'
                                 i=i+1
                                 checkwin()
                                 sp_game.after(300,lambda:pcturn())
                                elif(b['text']=='X' or b['text']=='O'):
                                 messagebox.showinfo('ERROR',errorx)
		b1=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b1))
		b1.place(x=450,y=300)
		b2=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b2))
			
		b2.place(x=590,y=300)
		b3=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b3))
		b3.place(x=730,y=300)
		b4=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b4))
		b4.place(x=450,y=430)
		b5=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b5))
		b5.place(x=590,y=430)
		b6=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b6))
		b6.place(x=730,y=430)
		b7=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b7))
		b7.place(x=450,y=550)
		b8=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b8))
		b8.place(x=590,y=550)
		b9=Button(sp_game_canvas,text='',image=None,height=6,width=14,relief=FLAT,bg='white',fg='black',command=lambda:process(b9))
		b9.place(x=730,y=550)
		sp_game.mainloop()

		##########################










		sp_game.mainloop()
	def save_mp():
		global PLAYER1_MP,PLAYER2_MP,default_winner
		PLAYER1_MP=P1entry_mp.get()
		PLAYER2_MP=P2entry_mp.get()
		default_winner="Data Not Available"
		conn=sqlite3.connect("tic1.db")
		c1=conn.cursor()
		c1.execute("""CREATE TABLE IF NOT EXISTS data1(
                p1 VARCHAR(10),
                P2 VARCHAR(10),
                winner VARCHAR(10),
                id INTEGER PRIMARY KEY AUTOINCREMENT
                );""")
		c1.execute("INSERT INTO data1(p1,p2,winner) VALUES('"+PLAYER1_MP+"','"+PLAYER2_MP+"','"+default_winner+"')")
		conn.commit()
		if ((len(PLAYER1_MP)!=0) and(len(PLAYER2_MP)!=0)):
			mpgame()
		elif ((len(PLAYER1_MP)==0)):
			messagebox.showwarning('Warning',"Please enter valid username")
		elif ((len(PLAYER2_MP)==0)):
			messagebox.showwarning('Warning',"Please enter valid username")
		else:
			pass

	

	def save_sp():

		global PLAYER1_SP
		PLAYER1_SP=P1entry_sp.get()
		conn=sqlite3.connect("tic.db")
		c=conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS data(
					p1 VARCHAR(10),
					P2 VARCHAR(10),
					winner VARCHAR(10),
					id INTEGER PRIMARY KEY AUTOINCREMENT
				);""")
		
		c.execute("INSERT INTO data(p1,p2,winner) VALUES('"+PLAYER1_SP+"','"+"CPU"+"','"+"No"+"')")
		conn.commit()
		if ((len(PLAYER1_SP)!=0)):
			spgame()
		elif (len(PLAYER1_SP)==0):
			messagebox.showwarning('Warning',"Please enter valid username")
		
		else:
			pass
	def single_player():
		global start_sp,P1entry_sp,ledvalue
		
		try:
			start.destroy()
			
		except:
			pass
		ledvalue="sp"
		start_sp=Tk()
		start_sp.title("tic tac toe")
		start_sp.attributes("-fullscreen",True)

		startsp_canvas=Canvas(start_sp,width=1366,height=768,bg="black")
		startsp_canvas.place(x=-2,y=-2)
		file1=PhotoImage(file="images/MAIN3_xogame.png")
		startsp_canvas.create_image(-1,-1,image=file1,anchor=NW)
		file5=PhotoImage(file="images/PLAYER_VS_CPU_xogame.png")
		file8=PhotoImage(file="images/PLAYER_ONE_xogame.png")
		startsp_canvas.create_image(1000,80,image=file5,anchor=NW)
		
		startsp_canvas.create_text(1150,220,text="ENTER PLAYER NAME",font=("Helvetia",25,"bold underline"),fill="red")
		
		startsp_canvas.create_image(980,270,image=file8,anchor=NW)
		
		P1entry_sp=Entry(startsp_canvas,width=15,font=('Arial',23,'bold'),borderwidth=0,bg="pink",justify="left",fg="black")
		P1entry_sp.place(x=1080,y=280)
		
		button_save_sp=Button(startsp_canvas,text="  SAVE  ",borderwidth=0,bg="red",fg="black",font=("Arial",15,"bold"),command=lambda:sp_change_colour_save(1))
		button_save_sp.place(x=1150,y=340)
		global backgame
		def backgame():
			try:
				start_sp.destroy()
			except:
				pass
			try:
				start_mp.destroy()
			except:
				pass
			choose()
		button_exit=Button(startsp_canvas,text="EXIT",borderwidth=0,bg="red",width=13,fg="black",font=("Arial",18,"bold"),command=lambda:sp_change_colour_exit(1))
		button_exit.place(x=1080,y=720)
		file7=PhotoImage(file="images/leaderboard_xogame.png")
		startsp_canvas.create_image(1110,480,image=file7,anchor=NW)
		button_LEADERBOARD=Button(startsp_canvas,text="LEADERBOARD",borderwidth=0,width=17,bg="red",fg="black",font=("Arial",18,"bold"),command=lambda:sp_change_colour_led(1))
		button_LEADERBOARD.place(x=1040,y=600)




		def sp_change_colour_save(a=0):
			if a==0:
				current=button_save_sp.cget("bg")
				text=button_save_sp.cget("text")
				'''
				if text=="  SAVE  ":
					button_save_mp.config(place(x=1100,y=380),text="CLICK HERE TO")'''
				if current=="red":
					button_save_sp.config(bg="green")
			
				else:
					#button_save_mp.config(place(x=1150,y=380),bg="red",text="  SAVE  ")
					button_save_sp.config(bg="red",text="  SAVE  ")
				start_sp.after(500,sp_change_colour_save)
			elif a==1:
				save_sp()
			else:
				pass
		sp_change_colour_save()


		def sp_change_colour_led(a=0):
			if a==0:
				current=button_LEADERBOARD.cget("bg")
				text=button_LEADERBOARD.cget("text")
				'''if text=="LEADERBOARD":
					button_LEADERBOARD.config(text="CLICK HERE TO VIEW ")'''
				if current=="red":
					button_LEADERBOARD.config(bg="green")
			
				else:
					button_LEADERBOARD.config(bg="red",text="LEADERBOARD")
				start_sp.after(500,sp_change_colour_led)
			elif a==1:
				led()
			else:
				pass
		sp_change_colour_led()

		def sp_change_colour_exit(a=0):
			if a==0:
				current=button_exit.cget("bg")
				text=button_exit.cget("text")
				'''
				if text=="EXIT":
					button_exit.config(text="CLICK HERE TO")'''
				if current=="red":
					button_exit.config(bg="green")
			
				else:
					button_exit.config(bg="red",text="EXIT")
				start_sp.after(500,sp_change_colour_exit)
			elif a==1:
				backgame()
			else:
				pass
		sp_change_colour_exit()






		start_sp.mainloop()
	def MULTIPLATER_player():
		global P1entry_mp,P2entry_mp,start_mp,ledvalue,PLAYER1_MP,PLAYER2_MP
		try:
			start.destroy()
			
		except:
			pass
		ledvalue="mp"
		start_mp=Tk()
		start_mp.title("tic tac toe")
		start_mp.attributes("-fullscreen",True)

		startmp_canvas=Canvas(start_mp,width=1366,height=768,bg="black")
		startmp_canvas.place(x=-2,y=-2)
		file1=PhotoImage(file="images/MAIN3_xogame.png")
		startmp_canvas.create_image(-1,-1,image=file1,anchor=NW)
		
		file5=PhotoImage(file="images/PLAYER_VS_PLAYER_xogame.png")
		file8=PhotoImage(file="images/PLAYER_ONE_xogame.png")
		file9=PhotoImage(file="images/PLAYER_TWO_xogame.png")
		startmp_canvas.create_image(1000,80,image=file5,anchor=NW)
		
		startmp_canvas.create_text(1150,220,text="ENTER PLAYERS NAME",font=("Helvetia",25,"bold underline"),fill="blue")
		
		startmp_canvas.create_image(980,260,image=file8,anchor=NW)
		startmp_canvas.create_image(980,320,image=file9,anchor=NW)
		
		
		
		P1entry_mp=Entry(startmp_canvas,width=15,font=('Arial',23,'bold'),borderwidth=0,bg="pink",justify="left",fg="black")
		P1entry_mp.place(x=1080,y=280)
		P2entry_mp=Entry(startmp_canvas,width=15,font=('Arial',23,'bold'),borderwidth=0,bg="pink",justify="left",fg="black")
		P2entry_mp.place(x=1080,y=330)
		PLAYER1_MP=P1entry_mp.get()
		PLAYER2_MP=P2entry_mp.get()
		button_save_mp=Button(startmp_canvas,text="  SAVE  ",borderwidth=0,relief=FLAT,bg="red",fg="black",font=("Arial",15,"bold"),command=lambda:mp_change_colour_save(1))
		button_save_mp.place(x=1150,y=380)
		button_exit=Button(startmp_canvas,text="EXIT",borderwidth=0,relief=FLAT,bg="red",width=13,fg="black",font=("Arial",18,"bold"),command=lambda:mp_change_colour_exit(1))
		button_exit.place(x=1080,y=720)
		file7=PhotoImage(file="images/leaderboard_xogame.png")
		startmp_canvas.create_image(1110,480,image=file7,anchor=NW)
		button_LEADERBOARD=Button(startmp_canvas,text="LEADERBOARD",relief=FLAT,borderwidth=0,width=13,bg="red",fg="black",font=("Arial",18,"bold"),command=lambda:mp_change_colour_led(1))
		button_LEADERBOARD.place(x=1080,y=600)



		def mp_change_colour_save(a=0):
			if a==0:
				current=button_save_mp.cget("bg")
				text=button_save_mp.cget("text")
				'''
				if text=="  SAVE  ":
					button_save_mp.config(place(x=1100,y=380),text="CLICK HERE TO")'''
				if current=="red":
					button_save_mp.config(bg="green")
			
				else:
					#button_save_mp.config(place(x=1150,y=380),bg="red",text="  SAVE  ")
					button_save_mp.config(bg="red",text="  SAVE  ")
				start_mp.after(500,mp_change_colour_save)
			elif a==1:
				save_mp()
			else:
				pass
		mp_change_colour_save()


		def mp_change_colour_led(a=0):
			if a==0:
				current=button_LEADERBOARD.cget("bg")
				text=button_LEADERBOARD.cget("text")
				
				if current=="red":
					button_LEADERBOARD.config(bg="green")
			
				else:
					button_LEADERBOARD.config(bg="red",text="LEADERBOARD")
				start_mp.after(500,mp_change_colour_led)
			elif a==1:
				led()
			else:
				pass
		mp_change_colour_led()

		def mp_change_colour_exit(a=0):
			if a==0:
				current=button_exit.cget("bg")
				text=button_exit.cget("text")
				'''
				if text=="EXIT":
					button_exit.config(text="CLICK HERE TO")'''
				if current=="red":
					button_exit.config(bg="green")
			
				else:
					button_exit.config(bg="red",text="EXIT")
				start_mp.after(500,mp_change_colour_exit)
			elif a==1:
				backgame()
			else:
				pass
		mp_change_colour_exit()

		start_mp.mainloop()

	def led():
			global ledvalue
			try:
				start.destroy()
			except:
				pass
			try:
				start_sp.destroy()
			except:
				pass
			try:
				start_mp.destroy()
			except:
				pass
			led=Tk()
			led.title("tic tac toe GAME SCOREBOARD")
			led.attributes('-fullscreen',True)
			led.resizable(0,0)
			led.configure(bg="yellow")
			ledcanvas=Canvas(led,height=180,width=1358,bg="yellow")
			ledcanvas.place(x=-2,y=-2)
			file_led1=PhotoImage(file='images/led1_xogame.png')
			file_led2=PhotoImage(file='images/led2_xogame.png')
			ledcanvas.create_image(110,-25,image=file_led1,anchor=NW)
			ledcanvas.create_image(960,-25,image=file_led1,anchor=NW)
			#ledcanvas.create_image(100,10,anchor=NE,image=file11)
			ledtext1=ledcanvas.create_text(630,50,text="LEADERBOARD",font=('Arial',60,'bold underline'),fill="blue")
			ledtext2=ledcanvas.create_text(250,150,text="SINGLE PLAYER MODE",font=('Arial',20,'bold underline'),fill="blue")
			ledtext2=ledcanvas.create_text(1100,150,text="MULTI PLAYER MODE",font=('Arial',20,'bold underline'),fill="blue")
			lframe=Frame(led,height=530,width=1356,bg="yellow")
			lframe.place(x=5,y=180)
			#lframe.image(960,25,image=file_led2,anchor=NW)
			conn=sqlite3.connect("tic.db")
			c=conn.cursor()
			c.execute("SELECT * FROM data")
			rec=c.fetchall()
			

			tabSP=ttk.Treeview(lframe,columns=(1,2,3),show="headings",height=25)
			tabSP.place(x=10,y=0)
			tabSP.heading(1,text="     PLAYER 1 NAME    ")
			tabSP.heading(2,text="     PLAYER 2 NAME    ")
			tabSP.heading(3,text="   Winner   ")
			for a in rec:
				tabSP.insert('','end',values=(a[0],a[1],a[2]))
				
			
			conn1=sqlite3.connect("tic1.db")
			c1=conn1.cursor()
			c1.execute("SELECT * FROM data1")
			rec1=c1.fetchall()
			tabMP=ttk.Treeview(lframe,columns=(1,2,3),show="headings",height=25)
			tabMP.place(x=740,y=0)
			tabMP.heading(1,text="     PLAYER 1 NAME    ")
			tabMP.heading(2,text="     PLAYER 2 NAME    ")
			tabMP.heading(3,text="   Winner   ")
			for i in rec1:
				tabMP.insert('','end',values=(i[0],i[1],i[2]))
			back=Button(led,text="BACK",borderwidth=0,bg="red",relief=FLAT,width=15,fg="black",font=("Arial",18,"bold"),command=lambda:change_colour_back(1))
			back.place(x=570,y=725)
			def back1111():
				global ledvalue
				led.destroy()
				if ledvalue=="mp":
					MULTIPLATER_player()
				elif ledvalue=="sp":
					single_player()
				elif ledvalue=="choose":
					choose()
				else:
					pass
			def change_colour_back(a=0):
				if a==0:
					current=back.cget("bg")
					if current=="red":
						back.config(bg="green")
			
					else:
						back.config(bg="red")
					led.after(500,change_colour_back)
				elif a==1:
					back1111()
				else:
					pass
			change_colour_back()






			
			
			
			
			led.mainloop()

	def choose():
		global start_canvas,start,file1,ledvalue
		try:
			intro.destroy()
		except:
			pass
		ledvalue="choose"
		start=Tk()
		start.title("tic tac toe")
		start.attributes("-fullscreen",True)
		
		
		start_canvas=Canvas(start,width=1366,height=768,bg="black")
		start_canvas.place(x=-2,y=-2)
		file1=PhotoImage(file="images/MAIN3_xogame.png")
		file5=PhotoImage(file="images/PLAYER_VS_CPU_xogame.png")
		file6=PhotoImage(file="images/PLAYER_VS_PLAYER_xogame.png")
		start_canvas.create_image(-1,-1,image=file1,anchor=NW)
		start_canvas.create_image(1000,80,image=file5,anchor=NW)
		start_canvas.create_image(1000,280,image=file6,anchor=NW)


		button_exit=Button(start_canvas,text="EXIT",borderwidth=0,bg="red",relief=FLAT,width=13,fg="black",font=("Arial",18,"bold"),command=lambda:choose_change_colour_exit(1))
		button_exit.place(x=1080,y=720)
		button_SP=Button(start_canvas,text="PLAYER V/S CPU",borderwidth=0,relief=FLAT,width=17,bg="red",fg="black",font=("Arial",18,"bold"),command=lambda:change_colour_sp(1))
		button_SP.place(x=1040,y=190)
		button_MP=Button(start_canvas,text="PLAYER V/S PLAYER",borderwidth=0,relief=FLAT,width=17,bg="red",fg="black",font=("Arial",18,"bold"),command=lambda:change_colour_mp(1))
		button_MP.place(x=1040,y=390)
		file7=PhotoImage(file="images/leaderboard_xogame.png")
		start_canvas.create_image(1110,480,image=file7,anchor=NW)
		button_LEADERBOARD=Button(start_canvas,text="LEADERBOARD",borderwidth=0,relief=FLAT,width=17,bg="red",fg="black",font=("Arial",18,"bold"),command=lambda:choose_change_colour_led(1))
		button_LEADERBOARD.place(x=1040,y=600)

		def change_colour_sp(a=0):
			if a==0:
				current=button_SP.cget("bg")
				text=button_SP.cget("text")
				if text=="PLAYER V/S CPU":
					button_SP.config(text="CLICK HERE FOR ")
				if current=="red":
					button_SP.config(bg="green")
			
				else:
					button_SP.config(bg="red",text="PLAYER V/S CPU")
				start.after(500,change_colour_sp)
			elif a==1:
				single_player()
			else:
				pass
		change_colour_sp()
		def change_colour_mp(a=0):
			if a==0:
				current=button_MP.cget("bg")
				text=button_MP.cget("text")
				if text=="PLAYER V/S PLAYER":
					button_MP.config(text=" CLICK HERE FOR ")
				if current=="red":
					button_MP.config(bg="green")
			
				else:
					button_MP.config(bg="red",text="PLAYER V/S PLAYER")
				start.after(500,change_colour_mp)
			elif a==1:
				MULTIPLATER_player()
			else:
				pass
		change_colour_mp()
		def choose_change_colour_led(a=0):
			if a==0:
				current=button_LEADERBOARD.cget("bg")
				text=button_LEADERBOARD.cget("text")
				if text=="LEADERBOARD":
					button_LEADERBOARD.config(text="CLICK HERE TO VIEW ")
				if current=="red":
					button_LEADERBOARD.config(bg="green")
			
				else:
					button_LEADERBOARD.config(bg="red",text="LEADERBOARD")
				start.after(500,choose_change_colour_led)
			elif a==1:
				led()
			else:
				pass
		choose_change_colour_led()

		def choose_change_colour_exit(a=0):
			if a==0:
				current=button_exit.cget("bg")
				text=button_exit.cget("text")
				if text=="EXIT":
					button_exit.config(text="CLICK HERE TO")
				if current=="red":
					button_exit.config(bg="green")
			
				else:
					button_exit.config(bg="red",text="EXIT")
				start.after(500,choose_change_colour_exit)
			elif a==1:
				exitgame(1)
			else:
				pass
		choose_change_colour_exit()






		
		start.mainloop()

	def intro1():
		global intro
		intro=Tk()
		intro.title("Tic Tac Toe")
		intro.attributes('-fullscreen',True)

		file1=PhotoImage(file="images/MAIN4_xogame.png")
		#file2=PhotoImage(file="images/start_xogame.png")
		intro.configure(bg="BLACK")
		main_canvas=Canvas(intro,width=1366,height=768,bg="black")
		main_canvas.place(x=-2,y=-2)
		main_canvas.create_image(-1,-1,image=file1,anchor=NW)
		clicked=0
		def change_colour(a=0):
			if a==0:
				current=start_button.cget("bg")
				text=start_button.cget("text")
				if text=="click here to":
					start_button.config(text="START")
				if current=="red":
					start_button.config(bg="green")
			
				else:
					start_button.config(bg="red",text="click here to")
				intro.after(500,change_colour)
			elif a==1:
				choose()
			else:
				pass
		
		start_button=Button(main_canvas,text="START",borderwidth=0,relief=FLAT,bg="red",width=10,fg="black",font=("Arial",18,"bold"),command=lambda:change_colour(1))
		start_button.place(x=1100,y=680)	
		change_colour()
			
		

		
		intro.mainloop()
	intro1()


