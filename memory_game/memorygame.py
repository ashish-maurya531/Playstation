
'''
THIS IS A MEMORY GAME THIS WILL HELP YOU TO INCREASE YOUR MEMORY AND GRASPING POWER .
YOU CAN COMPETE WITH YOUR FRIENDS. AND BECAME A WINNER.
YOU REALLY FIND IT VERY ENJOYING.
'''
#importing modules

from tkinter import *
from tkinter import messagebox
import time
from tkinter.ttk import*
from tkinter import ttk
import random
import sqlite3
array=[None]*36
img=[None]*36
txt=[None]*37
recbtn=None
default=None
click=1
match=0


e=None
textentry1=None

now=0
#MAKEING THE WHOLE CODE IN A FUNCTION TO CALL IT WHEN WE WANT TO PLAY THIS GAME
def memorymain():
    def start():
            global times,game
            inital1='1:   THERE ARE TOTAL 36 BLOCKS'
            inital2='2: 2-2 BLOCKS ARE IN PAIR WHICH\n HAVE SAME IMAGE'
            inital3='3: YOU HAVE TO MAKE PAIR OF ALL\n IMAGES BY HIT & TRIAL METHOD'
            game=Tk()
            game.title("MEMORY GAME")
            game.geometry('1100x640+100+10')
            game.resizable(0,0)
            def restart11():
                global match,u_timer,v_timer
                u_timer=time.time()
                v_timer=0
                match=0
                game.destroy()
                start()
        	
        	

            global u_timer
            #this give time since epoch i.e(january1,1970,00.00.00)=1566454995.8361387
            u_timer=time.time()

            print('u',u_timer)
            f=Canvas(game,height=600,width=400,bg="YELLOW")
            f.place(x=670,y=20)
            f.create_text(200,30,text="RULES TO PLAY:",font=("Helvetia",20,"bold"),fill="RED")
            f.create_text(190,70,text=inital1,font=("Helvetia",15,"bold"),fill="PURPLE")
            f.create_text(190,120,text=inital2,font=("Helvetia",15,"bold"),fill="PURPLE")
            f.create_text(190,170,text=inital3,font=("Helvetia",15,"bold"),fill="PURPLE")
            f.create_line(0,200,400,200,width=7,fill="red")
            f.create_line(4,4,400,4,400,598,4,598,4,4,width=7,fill="red")
            global e,textentry1,textentry,def_username
            textentry=f.create_text(200,250,text="If you want to save your data, then\nplease enter your name here and\npress save button.\nOtherwise keep playing as a guest.",font=("Helvetia",16,"bold"),fill="RED")
            e=Entry(f,width=32,font=('Arial',15))
            e.place(x=20,y=300)
            global username
            if len(e.get())==0:
                    username="unknown player"
            
              
            def save(a=None):
                global e,textentry1,textentry,username
                username=e.get()
                if len(e.get())!=0:
                    conn = sqlite3.connect('data.db')
                    conn.execute("INSERT INTO player VALUES('"+username+"',0,0)")
                    conn.commit()
                    
                    
                    
                    f.create_text(200,250,text="CURRENT USERNAME :",font=("Helvetia",25,"bold underline"),fill="blue")
                    textentry1=str(username)
                
                    e.destroy()
                    butsave.destroy()
                    f.delete(textentry)

                    textentry=f.create_text(160,300,text=textentry1,font=("Helvetia",25,"bold"),fill="BLACK")

                else:
                    b=messagebox.showwarning('Warning',"Please enter valid username")
            

            
            restart=PhotoImage(file="images/restart1_memorygame.png")
            exit=PhotoImage(file="images/exitgame1_memorygame.png")
            save_name=PhotoImage(file="images/save_memorygame.png")
            butsave=Button(f,image=save_name,command=save,border=None)
            butsave.place(x=150,y=332)

            butsave.bind("<Return>",save)
            restartbut=Button(f,image=restart,command=restart11)
            restartbut.place(x=120,y=400)
            def exitgame2():
                quitgame=messagebox.askyesno("QUIT THE GAME","ARE YOU REALLY WANT TO QUIT THE GAME")
                if (quitgame):
                    try:
                        game.destroy()
                    except:
                        pass
                    memorymain()
            
            exitbut=Button(f,image=exit,command=exitgame2)
            exitbut.place(x=120,y=500)


        

            
            def checkwin():
              global match,v_timer,u_timer,now
              if(match==18):
                v_timer=time.time()
                print("v=",v_timer)
                now=float(str(((v_timer)-(u_timer))/60)[:4])
                print(now)
                print(username)
                       
                score1=messagebox.askyesno("GAME OVER","ALL MATCHES FOUND PERFECTLY\nYOU WANT TO PLAY IT AGAIN\nTIME TAKEN:  %f minutes"%now)
                
               
                if (score1):
                    conn=sqlite3.connect('data.db')
                    conn.execute("UPDATE player SET time='"+str(now)+"' WHERE name='"+username+"'")    
                    conn.commit() 
                    restart11()
                else:
                    game.destroy()
                    conn=sqlite3.connect('data.db')
                    conn.execute("UPDATE player SET time='"+str(now)+"' WHERE name='"+username+"'")    
                    conn.commit() 
                    u_timer=time.time()
                    v_timer=0
                    match=0
            def checkmatch(b):
                global match,recbtn
                if(b['text']==recbtn['text'] and b!=recbtn):
                    b.destroy()
                    recbtn.destroy()
                    match+=1
                    checkwin()
                else:
                    b['image']=default
                    recbtn['image']=default
                    
                

            def but1(b):
                global img,recbtn,match,click
                b['image']=img[0]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but2(b):
                global img,recbtn,click
                b['image']=img[1]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but3(b):
                global img,recbtn,click
                b['image']=img[2]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but4(b):
                global img,recbtn,click
                b['image']=img[3]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but5(b):
                global img,recbtn,click
                b['image']=img[4]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but6(b):
                global img,recbtn,click
                b['image']=img[5]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but7(b):
                global img,recbtn,click
                b['image']=img[6]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but8(b):
                global img,recbtn,click
                b['image']=img[7]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but9(b):
                global img,recbtn,click
                b['image']=img[8]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but10(b):
                global img,recbtn,click
                b['image']=img[9]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but11(b):
                global img,recbtn,click
                b['image']=img[10]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but12(b):
                global img,recbtn,click
                b['image']=img[11]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but13(b):
                global img,recbtn,click
                b['image']=img[12]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but14(b):
                global img,recbtn,click
                b['image']=img[13]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but15(b):
                global img,recbtn,click
                b['image']=img[14]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but16(b):
                global img,recbtn,click
                b['image']=img[15]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but17(b):
                global img,recbtn,click
                b['image']=img[16]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but18(b):
                global img,recbtn,click
                b['image']=img[17]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but19(b):
                global img,recbtn,click
                b['image']=img[18]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but20(b):
                global img,recbtn,click
                b['image']=img[19]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but21(b):
                global img,recbtn,click
                b['image']=img[20]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but22(b):
                global img,recbtn,click
                b['image']=img[21]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but23(b):
                global img,recbtn,click
                b['image']=img[22]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but24(b):
                global img,recbtn,click
                b['image']=img[23]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but25(b):
                global img,recbtn,click
                b['image']=img[24]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but26(b):
                global img,recbtn,click
                b['image']=img[25]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but27(b):
                global img,recbtn,click
                b['image']=img[26]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but28(b):
                global img,recbtn,click
                b['image']=img[27]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but29(b):
                global img,recbtn,click
                b['image']=img[28]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but30(b):
                global img,recbtn,click
                b['image']=img[29]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but31(b):
                global img,recbtn,click
                b['image']=img[30]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but32(b):
                global img,recbtn,click
                b['image']=img[31]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but33(b):
                global img,recbtn,click
                b['image']=img[32]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but34(b):
                global img,recbtn,click
                b['image']=img[33]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but35(b):
                global img,recbtn,click
                b['image']=img[34]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1

            def but36(b):
                global img,recbtn,click
                b['image']=img[35]
                if(click==1):
                    recbtn=b
                    click=2

                elif(click==2):
                    game.after(200,lambda:checkmatch(b))
                    click=1
            

            
            loc1=r'images/doraemon_memorygame.png'
            loc2=r'images/nobita_memorygame.png'
            loc3=r'images/manny_memorygame.png'
            loc4=r'images/buzz_memorygame.png'
            loc5=r'images/buck_memorygame.png'
            loc6=r'images/hima_memorygame.png'
            loc7=r'images/olaf_memorygame.png'
            loc8=r'images/po_memorygame.png'
            loc9=r'images/pumba_memorygame.png'
            loc10=r'images/shinchan_memorygame.png'
            loc11=r'images/shifu_memorygame.png'
            loc12=r'images/tigress_memorygame.png'
            loc13=r'images/woody_memorygame.png'
            loc14=r'images/bird_memorygame.png'
            loc15=r'images/tiger_memorygame.png'
            loc16=r'images/frog_memorygame.png'
            loc17=r'images/jellyfish_memorygame.png'
            loc18=r'images/bat_memorygame.png'

            
            loc=r'images/BACK_memorygame.png'
            default=PhotoImage(file=loc)
            
            
            
            global img,text

            array=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc9,loc10,loc11,loc12,loc13,loc14,loc15,loc16,loc17,loc18]
            templist=array
            
            array=array+array
            
            for i in range(0,36,1):
                x=random.choice(array)
                img[i]=PhotoImage(file=x)
                txt[i+1]=str(x)
                array.remove(x)
        
            b11=Button(game,image=default,text=txt[1], width=88,command=lambda:but1(b11))
            b11.place(x=10,y=20)
            b12=Button(game,image=default,text=txt[2], width=88,command=lambda:but2(b12))
            b12.place(x=120,y=20)
            b13=Button(game,image=default,text=txt[3], width=88,command=lambda:but3(b13))
            b13.place(x=230,y=20)
            b14=Button(game,image=default,text=txt[4], width=88,command=lambda:but4(b14))
            b14.place(x=340,y=20)
            b15=Button(game,image=default,text=txt[5], width=88,command=lambda:but5(b15))
            b15.place(x=450,y=20)
            b16=Button(game,image=default,text=txt[6], width=88,command=lambda:but6(b16))
            b16.place(x=560,y=20)

    #row2
            b21=Button(game,image=default,text=txt[7], width=88 ,command=lambda:but7(b21))
            b21.place(x=10,y=122)
            b22=Button(game,image=default,text=txt[8], width=88 ,command=lambda:but8(b22))
            b22.place(x=120,y=122)
            b23=Button(game,image=default,text=txt[9], width=88 ,command=lambda:but9(b23))
            b23.place(x=230,y=122)
            b24=Button(game,image=default,text=txt[10], width=88 ,command=lambda:but10(b24))
            b24.place(x=340,y=122)
            b25=Button(game,image=default,text=txt[11], width=88 ,command=lambda:but11(b25))
            b25.place(x=450,y=122)
            b26=Button(game,image=default,text=txt[12], width=88 ,command=lambda:but12(b26))
            b26.place(x=560,y=122)

    #row3
            b31=Button(game,image=default,text=txt[13], width=88,command=lambda:but13(b31))
            b31.place(x=10,y=224)
            b32=Button(game,image=default,text=txt[14], width=88,command=lambda:but14(b32))
            b32.place(x=120,y=224)
            b33=Button(game,image=default,text=txt[15], width=88,command=lambda:but15(b33))
            b33.place(x=230,y=224)
            b34=Button(game,image=default,text=txt[16], width=88,command=lambda:but16(b34))
            b34.place(x=340,y=224)
            b35=Button(game,image=default,text=txt[17], width=88,command=lambda:but17(b35))
            b35.place(x=450,y=224)
            b36=Button(game,image=default,text=txt[18], width=88,command=lambda:but18(b36))
            b36.place(x=560,y=224)

    #row4
            b41=Button(game,image=default,text=txt[19], width=88,command=lambda:but19(b41))
            b41.place(x=10,y=326)
            b42=Button(game,image=default,text=txt[20], width=88,command=lambda:but20(b42))
            b42.place(x=120,y=326)
            b43=Button(game,image=default,text=txt[21], width=88,command=lambda:but21(b43))
            b43.place(x=230,y=326)
            b44=Button(game,image=default,text=txt[22], width=88,command=lambda:but22(b44))
            b44.place(x=340,y=326)
            b45=Button(game,image=default,text=txt[23], width=88,command=lambda:but23(b45))
            b45.place(x=450,y=326)
            b46=Button(game,image=default,text=txt[24], width=88,command=lambda:but24(b46))
            b46.place(x=560,y=326)

    #row5
            b51=Button(game,image=default,text=txt[25], width=88,command=lambda:but25(b51))
            b51.place(x=10,y=428)
            b52=Button(game,image=default,text=txt[26], width=88,command=lambda:but26(b52))
            b52.place(x=120,y=428)
            b53=Button(game,image=default,text=txt[27], width=88,command=lambda:but27(b53))
            b53.place(x=230,y=428)
            b54=Button(game,image=default,text=txt[28], width=88,command=lambda:but28(b54))
            b54.place(x=340,y=428)
            b55=Button(game,image=default,text=txt[29], width=88,command=lambda:but29(b55))
            b55.place(x=450,y=428)
            b56=Button(game,image=default,text=txt[30], width=88,command=lambda:but30(b56))
            b56.place(x=560,y=428)

    #row6
            b61=Button(game,image=default,text=txt[31], width=88,command=lambda:but31(b61))
            b61.place(x=10,y=530)
            b62=Button(game,image=default,text=txt[32], width=88,command=lambda:but32(b62))
            b62.place(x=120,y=530)
            b63=Button(game,image=default,text=txt[33], width=88,command=lambda:but33(b63))
            b63.place(x=230,y=530)
            b64=Button(game,image=default,text=txt[34], width=88,command=lambda:but34(b64))
            b64.place(x=340,y=530)
            b65=Button(game,image=default,text=txt[35], width=88,command=lambda:but35(b65))
            b65.place(x=450,y=530)
            b66=Button(game,image=default,text=txt[36], width=88,command=lambda:but36(b66))
            b66.place(x=560,y=530)
            game.mainloop()
    def exit1():
        global match,u_timer,v_timer
        u_timer=time.time()
        v_timer=0
        match=0
        intro.destroy()
        start()

    def led():
            led=Tk()
            led.title("MEMORY GAME LEADERBOARD")
            led.geometry('1024x500+100+100')
            led.resizable(0,0)
            led.configure(bg="yellow")
            ledcanvas=Canvas(led,height=100,width=1010,bg="yellow")
            ledcanvas.pack()
            #ledcanvas.create_image(100,10,anchor=NE,image=file11)
            ledtext=ledcanvas.create_text(530,40,text="LEADERBOARD",font=('Arial',50,'bold underline'),fill="blue")
            lframe=Frame(led)
            lframe.pack( fill='both',padx=20)
            tab=ttk.Treeview(lframe,columns=(1,2),show="headings",height=14)
            tab.pack(fill="both")
            
            tab.heading(1,text="PLAYER NAME")
            tab.heading(2,text="TIME TAKEN (minutes)")
            conn=sqlite3.connect('data.db')
            c=conn.cursor()
            c.execute('SELECT * FROM player')
            records=c.fetchall()
            for a  in records:
                    print(a)
                    tab.insert('','end',values=(a[0],a[2]))
            
            led.resizable(0,0)
            def back1111():
                    led.destroy()
            back=Button(led,text="BACK", width=30,border=None,command=back1111)
            back.pack(pady=20)
            led.mainloop()

    def exitgame():
        quitgame=messagebox.askyesno("QUIT THE GAME","ARE YOU REALLY WANT TO QUIT THE GAME")
        if (quitgame):
            try:
                intro.destroy()
            except:
                pass
            try:
                game.destroy()
            except:
                pass
            import playstationfile
            from playstationfile import inital
            inital=0
            playstationfile.next2()


    	

    intro=Tk() 
    intro.title("MEMORY GAME ")
    intro.geometry("1024x500+100+100")
    intro.resizable(0,0)
    c=Canvas(intro, bg="WHITE",height=500,width=1024)
    file1=PhotoImage(file="images/intro_memorygame.png")
        
    id=c.create_image(0,0,anchor=NW, image=file1)
    c.place(x=0,y=0)
       
        
        


    file2=PhotoImage(file="images/st3_memorygame.png")
    file3=PhotoImage(file="images/l_memorygame.png")
    file4=PhotoImage(file="images/exit2_memorygame.png")
    bu1=Button(width=40,image=file2,command=exit1)
    bu1.place(x=230,y=400)
    bu2=Button(width=30,image=file3,command=led)
    bu2.place(x=450,y=400)
    bu3=Button(width=30,image=file4,command=exitgame)
    bu3.place(x=730,y=400)
        
    intro.mainloop()


















