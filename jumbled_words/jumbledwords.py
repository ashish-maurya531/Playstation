'''
THIS IS A JUMBLED WORD GAME THIS WILL HELP YOU TO INCREASE YOUR VOCABULARY .
YOU CAN COMPETE WITH YOUR FRIENDS. AND BECAME A WINNER.
YOU REALLY FIND IT VERY ENJOYING.
'''



#IMPORTING MODULES
from tkinter import*
from tkinter import messagebox 
from tkinter import ttk
import random
import sqlite3
import time
import threading
from threading import Timer
#MAKEING THE WHOLE CODE IN A FUNCTION TO CALL IT WHEN WE WANT TO PLAY THIS GAME
def main():
    def animal_window():
        global ANIMALS_WORD2,score_animal,animal_click_on_answer,animal_img_no,gamefile4,gamefile5,score_animal,animal_gameover,animal_random_index,animal_jword,count,animal_index_match,animal_click_on_answer,ANIMALS_WORD2,score_animal,answer_label,animal_index_match,animal_click_on_answer,correct_image,wrong_image

        ANIMALS_WORD = ['DRBI', 'DGO', 'OENDYK', 'GFRIEFA', 'GLOILARTA', 'TAC', 'EHSOR', 'OLIN', 'MYOEKN', 'EEB', 'KDUC',
                            'RGFO', 'TPNLEHEA', 'ORCDCIELO', 'POLNIHD', 'LARLIGO', 'EMSUO', 'EGTRI', 'ABRITB', 'ATR', ]

        ANIMALS_ANSWER = ['BIRD', 'DOG', 'DONKEY', 'GIRAFFE', 'ALLIGATOR', 'CAT', 'HORSE', 'LION', 'MONKEY', 'BEE', 'DUCK',
                            'FROG', 'ELEPHANT', 'CROCODILE', 'DOLPHIN', 'GORILLA', 'MOUSE', 'TIGER', 'RABBIT', 'RAT', ]

        ANIMALS_WORD2 =list(ANIMALS_WORD)



        animal_random_index=random.randrange(0,len(ANIMALS_WORD))
        animal_jword=ANIMALS_WORD2[animal_random_index]
        animal_index_match=ANIMALS_WORD.index(animal_jword)
        ANIMALS_WORD2.remove(animal_jword)



        score_animal=0
        animal_click_on_answer=0
        animal_img_no=0


        def animalmain():
            def animal_exit():
                qut=messagebox.askyesno("Exit the game","Do you really want to exit?")
                if (qut):
                    try:
                        animal_gameover.destroy()
                    except:
                        pass
                    option_fn()
            def ANIMAL_homepage():
                global ANIMALS_WORD2,score_animal,animal_click_on_answer,animal_img_no
                
                animal_gameover.destroy()
                ANIMALS_WORD2 =list(ANIMALS_WORD)
                score_animal=0
                animal_click_on_answer=0
                animal_img_no=0
                option_fn()
            def animal_GAMEOVER():
            
                animal_game.destroy()
                global gamefile4,gamefile5,score_animal,animal_gameover

            
            
            
                animal_gameover=Tk()
                animal_gameover.title("GAME OVER")
                animal_gameover.geometry("520x300+400+200")
                animal_gameover_canvas=Canvas(animal_gameover,width=520,height=300,bg="white")
                gamefile4=PhotoImage(file="images/gameover3_jumbledwords.png")
                gamefile5=PhotoImage(file="images/exitOVER_jumbledwords.png")
                gamefile6=PhotoImage(file="images/homepage_jumbledwords.png")
                animal_gameover_canvas.create_image(0,0,image=gamefile4,anchor=NW)
                animal_gameover_canvas.place(x=0,y=0)
                
                conn1 = sqlite3.connect("jum.db")
                c1 = conn1.cursor()
                c1.execute("UPDATE data SET score1='"+str(score_animal)+"' WHERE p1='"+save_username+"'")
                conn1.commit()
                c1.close()
                conn1.close()



                over_exit=Button(animal_gameover_canvas,image=gamefile5,borderwidth=0,command=animal_exit)
                over_exit.place(x=390,y=220)
                over_homepage=Button(animal_gameover_canvas,image=gamefile6,borderwidth=0,command=ANIMAL_homepage)
                over_homepage.place(x=50,y=220)
                animal_gameover_canvas.create_text(250,250,text="You Scored: "+str(score_animal),font=('Arial',20,'bold'),fill="blue")

                animal_gameover.mainloop()


            def animal_next_word():

                global animal_random_index,animal_jword,count,animal_index_match,animal_click_on_answer,ANIMALS_WORD2
                if len(ANIMALS_WORD2)==1:
                        next_button.config(state=DISABLED)
                    
                animal_random_index=random.randrange(0,len(ANIMALS_WORD2))
                animal_jword=ANIMALS_WORD2[animal_random_index]
                animal_index_match=ANIMALS_WORD.index(animal_jword)
                ANIMALS_WORD2.remove(animal_jword)
                animal_canvas.itemconfigure(label,text=animal_jword)
                useranswer_entry.delete(0,END)
            
                

                try:
                    animal_canvas.itemconfigure(answer_label,text='')
                    answer_button.config(state=NORMAL)
                    check_button.config(state=NORMAL)
                
                
                except:
                    pass

                if (((animal_click_on_answer==1) and (animal_img_no==1)) or(animal_img_no==1) ):
                    animal_canvas.delete(correct_image)

                elif (((animal_click_on_answer==1) and (animal_img_no==2)) or(animal_img_no==2)) :
                    animal_canvas.delete(wrong_image)



            def answer_check():
                global score_animal,answer_label,animal_index_match,animal_click_on_answer
                if (score_animal==0):
                    if (len(ANIMALS_WORD2)==0):
                        animal_canvas.itemconfigure(answer_label,text=ANIMALS_ANSWER[animal_index_match],font=('Arial',20,'bold'),fill="green")
                        answer_button.config(state=DISABLED)
                        check_button.config(state=DISABLED)
                        animal_game.after(1000,animal_GAMEOVER)
                    elif (len(ANIMALS_WORD2)!=0):
                        animal_canvas.itemconfigure(answer_label,text="           sorry!\nscore your score is 0",font=('Arial',13,'bold'),fill="blue")
                        print(len(ANIMALS_WORD2))
                else:
                    score_animal-=1
                    animal_click_on_answer+=1
                    animal_canvas.itemconfigure(score_label,text="Score: "+str(score_animal))
                    animal_canvas.itemconfigure(answer_label,text=ANIMALS_ANSWER[animal_index_match],font=('Arial',20,'bold'),fill="green")
                    answer_button.config(state=DISABLED)
                    check_button.config(state=DISABLED)
                    if len(ANIMALS_WORD2)==0:
                        print(len(ANIMALS_WORD2))
                        next_button.config(state=DISABLED)
                        print("game over")
                        animal_game.after(1000,animal_GAMEOVER)
                        check_button.config(state=DISABLED)
                        print("game over")
                    
            
            


            def check_answer():
                global score_animal,gamefile2,gamefile3,animal_img_no,correct_image,wrong_image

            
                
                gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
                gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
                if len(useranswer_entry.get())==0:
                    messagebox.showwarning("Warning!","              Invalid entry!\nYou have entered nothing in the box.")
                elif useranswer_entry.get()==(ANIMALS_ANSWER[animal_index_match]).upper():
                    score_animal+=1
                    animal_canvas.itemconfigure(score_label,text="Score: "+str(score_animal))
                
                    animal_img_no=1
                    correct_image=animal_canvas.create_image(670,245,image=gamefile2)
                    if len(ANIMALS_WORD2)==0:
                        print(len(ANIMALS_WORD2))
                        next_button.config(state=DISABLED)
                        print("game over")
                        animal_game.after(500,animal_GAMEOVER)
                    
                    
                    else:
                        animal_game.after(500,animal_next_word)

                elif useranswer_entry.get()!=(str(ANIMALS_ANSWER[animal_index_match])).upper():
                    wrong_image=animal_canvas.create_image(670,245,image=gamefile3)
                    animal_img_no=2


            
            global animal_game,animal_canvas,score_label,label,useranswer_entry,answer_label,check_button,next_button,answer_label_info,answer_button
            animal_game=Tk()
            animal_game.title("JUMBULED WORDS => ANIMAL")
            animal_game.geometry('800x533+200+100')
            animal_canvas=Canvas(animal_game,width=800,height=533,bg="red")
            animal_canvas.place(x=0,y=0)
            gamefile1=PhotoImage(file="images/game_jumbledwords.png")
            gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
            gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
            animal_canvas.create_image(0,0,image=gamefile1,anchor=NW)
            #global save_username
            #save_username_label=animal_canvas.create_text(520,15,text="PLAYER: "+str(save_username),font=('Arial',20,'bold'),fill="blue")
            score_label=animal_canvas.create_text(720,15,text="Score: "+str(score_animal),font=('Arial',20,'bold'),fill="blue")
            animal_canvas.create_text(200,15,text="Please open \'Caps Lock\' before starting",font=('Arial',15,'bold'),fill="blue")
            useranswer_entry=Entry(animal_canvas,width=22,font=('Arial',23,'bold'),borderwidth=0,justify="center",fg="red")
            useranswer_entry.place(x=240,y=230)

            label=animal_canvas.create_text(410,180,text=animal_jword,font=('Arial',40,'bold'),fill="blue")
            answer_label=animal_canvas.create_text(702,460,text=" ",font=('Arial',13,'bold'),fill="blue")
            check_button=Button(animal_canvas,text="Check",width=10,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=check_answer)
            check_button.place(x=350,y=300)
            next_button=Button(animal_canvas,text="next",width=10,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=animal_next_word)
            next_button.place(x=350,y=360)
            answer_label_info=animal_canvas.create_text(500,520,text="For correct answer click here==>",font=('Arial',10,'bold'),fill="blue")
            answer_button=Button(animal_canvas,text="Correct answer",width=15,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=answer_check)
            answer_button.place(x=620,y=494)


            animal_game.mainloop()
        animalmain()
        




    def fruit_window():
        global fruitS_WORD2,score_fruit,fruit_click_on_answer,fruit_img_no,gamefile4,gamefile5,score_fruit,fruit_gameover,fruit_random_index,fruit_jword,count,fruit_index_match,fruit_click_on_answer,fruitS_WORD2,score_fruit,answer_label,fruit_index_match,fruit_click_on_answer,correct_image,wrong_image

        fruitS_WORD = ['NABANA', 'NATACPELOU', 'RSAGPE','IIWK','BMULYRER','TWEARLOMEN','LOVEI','ROGEAN','PAPYAA','IENP PAPEL','BERASPRRY','STRBERARYW',
                             'LABBCKRREY','APPLE','GAAUV','NOOCCUT','MBOLACARA','CUSTARD PPALE','CRREHY']

        fruitS_ANSWER = ['BANANA', 'CANTALOUPE', 'GRAPES', 'KIWI', 'MULBERRY', 'WATERMELON', 'OLIVE', 'ORANGE', 'PAPAYA', 'PINE APPLE', 'RASPBERRY',
                            'STRAWBERRY', 'BLACKBERRY', 'APPLE', 'GUAVA', 'COCONUT', 'CARAMBOLA', 'CUSTARD APPLE', 'CHERRY']

        fruitS_WORD2 =list(fruitS_WORD)



        fruit_random_index=random.randrange(0,len(fruitS_WORD))
        fruit_jword=fruitS_WORD2[fruit_random_index]
        fruit_index_match=fruitS_WORD.index(fruit_jword)
        fruitS_WORD2.remove(fruit_jword)



        score_fruit=0
        fruit_click_on_answer=0
        fruit_img_no=0


        def fruitmain():
            def fruit_exit():
                qut=messagebox.askyesno("Exit the game","Do you really want to exit?")
                if (qut):
                    try:
                        fruit_gameover.destroy()
                    except:
                        pass
                    option_fn()
            def fruit_homepage():
                global fruitS_WORD2,score_fruit,fruit_click_on_answer,fruit_img_no
                
                fruit_gameover.destroy()
                fruitS_WORD2 =list(fruitS_WORD)
                score_fruit=0
                fruit_click_on_answer=0
                fruit_img_no=0
                option_fn()
            def fruit_GAMEOVER():
            
                fruit_game.destroy()
                global gamefile4,gamefile5,score_fruit,fruit_gameover

            
            
            
                fruit_gameover=Tk()
                fruit_gameover.title("GAME OVER")
                fruit_gameover.geometry("520x300+400+200")
                fruit_gameover_canvas=Canvas(fruit_gameover,width=520,height=300,bg="white")
                gamefile4=PhotoImage(file="images/gameover3_jumbledwords.png")
                gamefile5=PhotoImage(file="images/exitOVER_jumbledwords.png")
                gamefile6=PhotoImage(file="images/homepage_jumbledwords.png")
                fruit_gameover_canvas.create_image(0,0,image=gamefile4,anchor=NW)
                fruit_gameover_canvas.place(x=0,y=0)

                conn1 = sqlite3.connect("jum.db")
                c1 = conn1.cursor()
                c1.execute("UPDATE data SET score3='"+str(score_fruit)+"' WHERE p1='"+save_username+"'")
                conn1.commit()
                c1.close()
                conn1.close()



                over_exit=Button(fruit_gameover_canvas,image=gamefile5,borderwidth=0,command=fruit_exit)
                over_exit.place(x=390,y=220)
                over_homepage=Button(fruit_gameover_canvas,image=gamefile6,borderwidth=0,command=fruit_homepage)
                over_homepage.place(x=50,y=220)
                fruit_gameover_canvas.create_text(250,250,text="You Scored: "+str(score_fruit),font=('Arial',20,'bold'),fill="blue")

                fruit_gameover.mainloop()


            def fruit_next_word():

                global fruit_random_index,fruit_jword,count,fruit_index_match,fruit_click_on_answer,fruitS_WORD2
                if len(fruitS_WORD2)==1:
                        next_button.config(state=DISABLED)
                    
                fruit_random_index=random.randrange(0,len(fruitS_WORD2))
                fruit_jword=fruitS_WORD2[fruit_random_index]
                fruit_index_match=fruitS_WORD.index(fruit_jword)
                fruitS_WORD2.remove(fruit_jword)
                fruit_canvas.itemconfigure(label,text=fruit_jword)
                useranswer_entry.delete(0,END)
            
                

                try:
                    fruit_canvas.itemconfigure(answer_label,text='')
                    answer_button.config(state=NORMAL)
                    check_button.config(state=NORMAL)
                
                
                except:
                    pass

                if (((fruit_click_on_answer==1) and (fruit_img_no==1)) or(fruit_img_no==1) ):
                    fruit_canvas.delete(correct_image)

                elif (((fruit_click_on_answer==1) and (fruit_img_no==2)) or(fruit_img_no==2)) :
                    fruit_canvas.delete(wrong_image)



            def answer_check():
                global score_fruit,answer_label,fruit_index_match,fruit_click_on_answer
                if (score_fruit==0):
                    if (len(fruitS_WORD2)==0):
                        fruit_canvas.itemconfigure(answer_label,text=fruitS_ANSWER[fruit_index_match],font=('Arial',20,'bold'),fill="green")
                        answer_button.config(state=DISABLED)
                        check_button.config(state=DISABLED)
                        fruit_game.after(1000,fruit_GAMEOVER)
                    elif (len(fruitS_WORD2)!=0):
                        fruit_canvas.itemconfigure(answer_label,text="           sorry!\nscore your score is 0",font=('Arial',13,'bold'),fill="blue")
                        print(len(fruitS_WORD2))
                else:
                    score_fruit-=1
                    fruit_click_on_answer+=1
                    fruit_canvas.itemconfigure(score_label,text="Score: "+str(score_fruit))
                    fruit_canvas.itemconfigure(answer_label,text=fruitS_ANSWER[fruit_index_match],font=('Arial',20,'bold'),fill="green")
                    answer_button.config(state=DISABLED)
                    check_button.config(state=DISABLED)
                    if len(fruitS_WORD2)==0:
                        print(len(fruitS_WORD2))
                        next_button.config(state=DISABLED)
                        print("game over")
                        fruit_game.after(1000,fruit_GAMEOVER)
                        check_button.config(state=DISABLED)
                        print("game over")
                    
            
            


            def check_answer():
                global score_fruit,gamefile2,gamefile3,fruit_img_no,correct_image,wrong_image

            
                
                gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
                gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
                if len(useranswer_entry.get())==0:
                    messagebox.showwarning("Warning!","              Invalid entry!\nYou have entered nothing in the box.")
                elif useranswer_entry.get()==(fruitS_ANSWER[fruit_index_match]).upper():
                    score_fruit+=1
                    fruit_canvas.itemconfigure(score_label,text="Score: "+str(score_fruit))
                
                    fruit_img_no=1
                    correct_image=fruit_canvas.create_image(670,245,image=gamefile2)
                    if len(fruitS_WORD2)==0:
                        print(len(fruitS_WORD2))
                        next_button.config(state=DISABLED)
                        print("game over")
                        fruit_game.after(500,fruit_GAMEOVER)
                    
                    
                    else:
                        fruit_game.after(500,fruit_next_word)

                elif useranswer_entry.get()!=(str(fruitS_ANSWER[fruit_index_match])).upper():
                    wrong_image=fruit_canvas.create_image(670,245,image=gamefile3)
                    fruit_img_no=2


            
            global fruit_game,fruit_canvas,score_label,label,useranswer_entry,answer_label,check_button,next_button,answer_label_info,answer_button
            fruit_game=Tk()
            fruit_game.title("JUMBULED WORDS => fruit")
            fruit_game.geometry('800x533+200+100')
            fruit_canvas=Canvas(fruit_game,width=800,height=533,bg="red")
            fruit_canvas.place(x=0,y=0)
            gamefile1=PhotoImage(file="images/game_jumbledwords.png")
            gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
            gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
            fruit_canvas.create_image(0,0,image=gamefile1,anchor=NW)
            #global save_username
            #save_username_label=fruit_canvas.create_text(520,15,text="PLAYER: "+str(save_username),font=('Arial',20,'bold'),fill="blue")
            score_label=fruit_canvas.create_text(720,15,text="Score: "+str(score_fruit),font=('Arial',20,'bold'),fill="blue")
            fruit_canvas.create_text(200,15,text="Please open \'Caps Lock\' before starting",font=('Arial',15,'bold'),fill="blue")
            useranswer_entry=Entry(fruit_canvas,width=22,font=('Arial',23,'bold'),borderwidth=0,justify="center",fg="red")
            useranswer_entry.place(x=240,y=230)

            label=fruit_canvas.create_text(410,180,text=fruit_jword,font=('Arial',40,'bold'),fill="blue")
            answer_label=fruit_canvas.create_text(702,460,text=" ",font=('Arial',13,'bold'),fill="blue")
            check_button=Button(fruit_canvas,text="Check",width=10,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=check_answer)
            check_button.place(x=350,y=300)
            next_button=Button(fruit_canvas,text="next",width=10,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=fruit_next_word)
            next_button.place(x=350,y=360)
            answer_label_info=fruit_canvas.create_text(500,520,text="For correct answer click here==>",font=('Arial',10,'bold'),fill="blue")
            answer_button=Button(fruit_canvas,text="Correct answer",width=15,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=answer_check)
            answer_button.place(x=620,y=494)


            fruit_game.mainloop()
        fruitmain()





       
    def computer_window():
        
            global computerS_WORD2,score_computer,computer_click_on_answer,computer_img_no,gamefile4,gamefile5,score_computer,computer_gameover,computer_random_index,computer_jword,count,computer_index_match,computer_click_on_answer,computerS_WORD2,score_computer,answer_label,computer_index_match,computer_click_on_answer,correct_image,wrong_image

            computerS_WORD = ['OUMES','BKYOERDA','ONIMTRO','YTPONH','AAVJ','THMOREDRAOB','MAR','ERAWTSOR','DEMMO','KETWORKINGN','NETRETHE',
                                    'PI DDRASSE','CAKINGH','MMPGORRAING','NETRPRI','DENPRIVE','CSSPEORGIN','LEGACY TOOB','SOLID TATSE RIVED','SPAKERE']

            computerS_ANSWER = ['MOUSE','KEYBOARD','MONITIOR','PYTHON','JAVA','MOTHERBOARD','RAM','SOFTWARE','MODEM','NETWORKING','ETHERNET','IP ADDRESS',
                                 'HACKING', 'PROGRAMMING','PRINTER', 'PENDRIVE', 'PROCESSING','LEGACY BOOT', 'SOLID STATE DRIVE','SPEAKER']

            computerS_WORD2 =list(computerS_WORD)



            computer_random_index=random.randrange(0,len(computerS_WORD))
            computer_jword=computerS_WORD2[computer_random_index]
            computer_index_match=computerS_WORD.index(computer_jword)
            computerS_WORD2.remove(computer_jword)



            score_computer=0
            computer_click_on_answer=0
            computer_img_no=0


            def computermain():
                def computer_exit():
                    qut=messagebox.askyesno("Exit the game","Do you really want to exit?")
                    if (qut):
                        try:
                            computer_gameover.destroy()
                        except:
                            pass
                        option_fn()
                def computer_homepage():
                    global computerS_WORD2,score_computer,computer_click_on_answer,computer_img_no
                    
                    computer_gameover.destroy()
                    computerS_WORD2 =list(computerS_WORD)
                    score_computer=0
                    computer_click_on_answer=0
                    computer_img_no=0
                    option_fn()
                def computer_GAMEOVER():
                
                    computer_game.destroy()
                    global gamefile4,gamefile5,score_computer,computer_gameover

                
                
                
                    computer_gameover=Tk()
                    computer_gameover.title("GAME OVER")
                    computer_gameover.geometry("520x300+400+200")
                    computer_gameover_canvas=Canvas(computer_gameover,width=520,height=300,bg="white")
                    gamefile4=PhotoImage(file="images/gameover3_jumbledwords.png")
                    gamefile5=PhotoImage(file="images/exitOVER_jumbledwords.png")
                    gamefile6=PhotoImage(file="images/homepage_jumbledwords.png")
                    computer_gameover_canvas.create_image(0,0,image=gamefile4,anchor=NW)
                    computer_gameover_canvas.place(x=0,y=0)
                    conn1 = sqlite3.connect("jum.db")
                    c1 = conn1.cursor()
                    c1.execute("UPDATE data SET score2='"+str(score_computer)+"' WHERE p1='"+save_username+"'")
                    conn1.commit()
                    c1.close()
                    conn1.close()



                    over_exit=Button(computer_gameover_canvas,image=gamefile5,borderwidth=0,command=computer_exit)
                    over_exit.place(x=390,y=220)
                    over_homepage=Button(computer_gameover_canvas,image=gamefile6,borderwidth=0,command=computer_homepage)
                    over_homepage.place(x=50,y=220)
                    computer_gameover_canvas.create_text(250,250,text="You Scored: "+str(score_computer),font=('Arial',20,'bold'),fill="blue")

                    computer_gameover.mainloop()


                def computer_next_word():

                    global computer_random_index,computer_jword,count,computer_index_match,computer_click_on_answer,computerS_WORD2
                    if len(computerS_WORD2)==1:
                            next_button.config(state=DISABLED)
                        
                    computer_random_index=random.randrange(0,len(computerS_WORD2))
                    computer_jword=computerS_WORD2[computer_random_index]
                    computer_index_match=computerS_WORD.index(computer_jword)
                    computerS_WORD2.remove(computer_jword)
                    computer_canvas.itemconfigure(label,text=computer_jword)
                    useranswer_entry.delete(0,END)
                
                    

                    try:
                        computer_canvas.itemconfigure(answer_label,text='')
                        answer_button.config(state=NORMAL)
                        check_button.config(state=NORMAL)
                    
                    
                    except:
                        pass

                    if (((computer_click_on_answer==1) and (computer_img_no==1)) or(computer_img_no==1) ):
                        computer_canvas.delete(correct_image)

                    elif (((computer_click_on_answer==1) and (computer_img_no==2)) or(computer_img_no==2)) :
                        computer_canvas.delete(wrong_image)



                def answer_check():
                    global score_computer,answer_label,computer_index_match,computer_click_on_answer
                    if (score_computer==0):
                        if (len(computerS_WORD2)==0):
                            computer_canvas.itemconfigure(answer_label,text=computerS_ANSWER[computer_index_match],font=('Arial',20,'bold'),fill="green")
                            answer_button.config(state=DISABLED)
                            check_button.config(state=DISABLED)
                            computer_game.after(1000,computer_GAMEOVER)
                        elif (len(computerS_WORD2)!=0):
                            computer_canvas.itemconfigure(answer_label,text="           sorry!\nscore your score is 0",font=('Arial',13,'bold'),fill="blue")
                            print(len(computerS_WORD2))
                    else:
                        score_computer-=1
                        computer_click_on_answer+=1
                        computer_canvas.itemconfigure(score_label,text="Score: "+str(score_computer))
                        computer_canvas.itemconfigure(answer_label,text=computerS_ANSWER[computer_index_match],font=('Arial',20,'bold'),fill="green")
                        answer_button.config(state=DISABLED)
                        check_button.config(state=DISABLED)
                        if len(computerS_WORD2)==0:
                            print(len(computerS_WORD2))
                            next_button.config(state=DISABLED)
                            print("game over")
                            computer_game.after(1000,computer_GAMEOVER)
                            check_button.config(state=DISABLED)
                            print("game over")
                        
                
                


                def check_answer():
                    global score_computer,gamefile2,gamefile3,computer_img_no,correct_image,wrong_image

                
                    
                    gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
                    gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
                    if len(useranswer_entry.get())==0:
                        messagebox.showwarning("Warning!","              Invalid entry!\nYou have entered nothing in the box.")
                    elif useranswer_entry.get()==(computerS_ANSWER[computer_index_match]).upper():
                        score_computer+=1
                        computer_canvas.itemconfigure(score_label,text="Score: "+str(score_computer))
                    
                        computer_img_no=1
                        correct_image=computer_canvas.create_image(670,245,image=gamefile2)
                        if len(computerS_WORD2)==0:
                            print(len(computerS_WORD2))
                            next_button.config(state=DISABLED)
                            print("game over")
                            computer_game.after(500,computer_GAMEOVER)
                        
                        
                        else:
                            computer_game.after(500,computer_next_word)

                    elif useranswer_entry.get()!=(str(computerS_ANSWER[computer_index_match])).upper():
                        wrong_image=computer_canvas.create_image(670,245,image=gamefile3)
                        computer_img_no=2


                
                global computer_game,computer_canvas,score_label,label,useranswer_entry,answer_label,check_button,next_button,answer_label_info,answer_button
                computer_game=Tk()
                computer_game.title("JUMBULED WORDS => computer")
                computer_game.geometry('800x533+200+100')
                computer_canvas=Canvas(computer_game,width=800,height=533,bg="red")
                computer_canvas.place(x=0,y=0)
                gamefile1=PhotoImage(file="images/game_jumbledwords.png")
                gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
                gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
                computer_canvas.create_image(0,0,image=gamefile1,anchor=NW)
                #global save_username
                #save_username_label=computer_canvas.create_text(520,15,text="PLAYER: "+str(save_username),font=('Arial',20,'bold'),fill="blue")
                score_label=computer_canvas.create_text(720,15,text="Score: "+str(score_computer),font=('Arial',20,'bold'),fill="blue")
                computer_canvas.create_text(200,15,text="Please open \'Caps Lock\' before starting",font=('Arial',15,'bold'),fill="blue")
                useranswer_entry=Entry(computer_canvas,width=22,font=('Arial',23,'bold'),borderwidth=0,justify="center",fg="red")
                useranswer_entry.place(x=240,y=230)

                label=computer_canvas.create_text(410,180,text=computer_jword,font=('Arial',40,'bold'),fill="blue")
                answer_label=computer_canvas.create_text(702,460,text=" ",font=('Arial',13,'bold'),fill="blue")
                check_button=Button(computer_canvas,text="Check",width=10,font=('Arial',15,'bold'),
                    bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=check_answer)
                check_button.place(x=350,y=300)
                next_button=Button(computer_canvas,text="next",width=10,font=('Arial',15,'bold'),
                    bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=computer_next_word)
                next_button.place(x=350,y=360)
                answer_label_info=computer_canvas.create_text(500,520,text="For correct answer click here==>",font=('Arial',10,'bold'),fill="blue")
                answer_button=Button(computer_canvas,text="Correct answer",width=15,font=('Arial',15,'bold'),
                    bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=answer_check)
                answer_button.place(x=620,y=494)


                computer_game.mainloop()
            computermain()





       
    def celebrity_name():
        global CELEBRITY_NAMESS_WORD2,score_CELEBRITY_NAMES,CELEBRITY_NAMES_click_on_answer,CELEBRITY_NAMES_img_no,gamefile4,gamefile5,score_CELEBRITY_NAMES,CELEBRITY_NAMES_gameover,CELEBRITY_NAMES_random_index,CELEBRITY_NAMES_jword,count,CELEBRITY_NAMES_index_match,CELEBRITY_NAMES_click_on_answer,CELEBRITY_NAMESS_WORD2,score_CELEBRITY_NAMES,answer_label,CELEBRITY_NAMES_index_match,CELEBRITY_NAMES_click_on_answer,correct_image,wrong_image

        CELEBRITY_NAMESS_WORD = ['KHIITHR OSRANH','BHATIMA ANCHHCAB','MANLAS','AIFS LIA','LINA OOPKRA','AILA BTTHA','ULLA NUJRA','KHIRA WAASNT','KSHYAA MRAKU','RRYITANMICA','SOMAN KAPOOR',
                                        'DNAIVOG','REGIT SHFFOR','NHUKUC PENDAY','NMANAUYSH','AJAY','RIASHM RUIP','ANAGNAK TUNARA','YOHNNJ VELER']

        CELEBRITY_NAMESS_ANSWER = ['HRITHIK ROSHAN','AMITABH BACHCHAN','SALMAN','SAIF ALI','ANIL KAPOOR','ALIA BHATT', 'ALLU ARJUN', 'RAKHI SAWANT','AKSHAY KUMAR','CARRYMINATI','SONAM KAPOOR',
                                        'GOVINDA', 'TIGER SHROFF','CHUNKY PANDEY' ,'AYUSHMANN' ,'AJAY', 'AMRISH PURI','KANGANA RANAUT', 'JOHNNY LEVER']

        CELEBRITY_NAMESS_WORD2 =list(CELEBRITY_NAMESS_WORD)



        CELEBRITY_NAMES_random_index=random.randrange(0,len(CELEBRITY_NAMESS_WORD))
        CELEBRITY_NAMES_jword=CELEBRITY_NAMESS_WORD2[CELEBRITY_NAMES_random_index]
        CELEBRITY_NAMES_index_match=CELEBRITY_NAMESS_WORD.index(CELEBRITY_NAMES_jword)
        CELEBRITY_NAMESS_WORD2.remove(CELEBRITY_NAMES_jword)



        score_CELEBRITY_NAMES=0
        CELEBRITY_NAMES_click_on_answer=0
        CELEBRITY_NAMES_img_no=0


        def CELEBRITY_NAMESmain():
            def CELEBRITY_NAMES_exit():
                qut=messagebox.askyesno("Exit the game","Do you really want to exit?")
                if (qut):
                    try:
                        CELEBRITY_NAMES_gameover.destroy()
                    except:
                        pass
                    option_fn()
            def CELEBRITY_NAMES_homepage():
                global CELEBRITY_NAMESS_WORD2,score_CELEBRITY_NAMES,CELEBRITY_NAMES_click_on_answer,CELEBRITY_NAMES_img_no
                
                CELEBRITY_NAMES_gameover.destroy()
                CELEBRITY_NAMESS_WORD2 =list(CELEBRITY_NAMESS_WORD)
                score_CELEBRITY_NAMES=0
                CELEBRITY_NAMES_click_on_answer=0
                CELEBRITY_NAMES_img_no=0
                option_fn()
            def CELEBRITY_NAMES_GAMEOVER():
            
                CELEBRITY_NAMES_game.destroy()
                global gamefile4,gamefile5,score_CELEBRITY_NAMES,CELEBRITY_NAMES_gameover

            
            
            
                CELEBRITY_NAMES_gameover=Tk()
                CELEBRITY_NAMES_gameover.title("GAME OVER")
                CELEBRITY_NAMES_gameover.geometry("520x300+400+200")
                CELEBRITY_NAMES_gameover_canvas=Canvas(CELEBRITY_NAMES_gameover,width=520,height=300,bg="white")
                gamefile4=PhotoImage(file="images/gameover3_jumbledwords.png")
                gamefile5=PhotoImage(file="images/exitOVER_jumbledwords.png")
                gamefile6=PhotoImage(file="images/homepage_jumbledwords.png")
                CELEBRITY_NAMES_gameover_canvas.create_image(0,0,image=gamefile4,anchor=NW)
                CELEBRITY_NAMES_gameover_canvas.place(x=0,y=0)
                conn1 = sqlite3.connect("jum.db")
                c1 = conn1.cursor()
                c1.execute("UPDATE data SET score4='"+str(score_CELEBRITY_NAMES)+"' WHERE p1='"+save_username+"'")
                conn1.commit()
                c1.close()
                conn1.close()



                over_exit=Button(CELEBRITY_NAMES_gameover_canvas,image=gamefile5,borderwidth=0,command=CELEBRITY_NAMES_exit)
                over_exit.place(x=390,y=220)
                over_homepage=Button(CELEBRITY_NAMES_gameover_canvas,image=gamefile6,borderwidth=0,command=CELEBRITY_NAMES_homepage)
                over_homepage.place(x=50,y=220)
                CELEBRITY_NAMES_gameover_canvas.create_text(250,250,text="You Scored: "+str(score_CELEBRITY_NAMES),font=('Arial',20,'bold'),fill="blue")

                CELEBRITY_NAMES_gameover.mainloop()


            def CELEBRITY_NAMES_next_word():

                global CELEBRITY_NAMES_random_index,CELEBRITY_NAMES_jword,count,CELEBRITY_NAMES_index_match,CELEBRITY_NAMES_click_on_answer,CELEBRITY_NAMESS_WORD2
                if len(CELEBRITY_NAMESS_WORD2)==1:
                        next_button.config(state=DISABLED)
                    
                CELEBRITY_NAMES_random_index=random.randrange(0,len(CELEBRITY_NAMESS_WORD2))
                CELEBRITY_NAMES_jword=CELEBRITY_NAMESS_WORD2[CELEBRITY_NAMES_random_index]
                CELEBRITY_NAMES_index_match=CELEBRITY_NAMESS_WORD.index(CELEBRITY_NAMES_jword)
                CELEBRITY_NAMESS_WORD2.remove(CELEBRITY_NAMES_jword)
                CELEBRITY_NAMES_canvas.itemconfigure(label,text=CELEBRITY_NAMES_jword)
                useranswer_entry.delete(0,END)
            
                

                try:
                    CELEBRITY_NAMES_canvas.itemconfigure(answer_label,text='')
                    answer_button.config(state=NORMAL)
                    check_button.config(state=NORMAL)
                
                
                except:
                    pass

                if (((CELEBRITY_NAMES_click_on_answer==1) and (CELEBRITY_NAMES_img_no==1)) or(CELEBRITY_NAMES_img_no==1) ):
                    CELEBRITY_NAMES_canvas.delete(correct_image)

                elif (((CELEBRITY_NAMES_click_on_answer==1) and (CELEBRITY_NAMES_img_no==2)) or(CELEBRITY_NAMES_img_no==2)) :
                    CELEBRITY_NAMES_canvas.delete(wrong_image)



            def answer_check():
                global score_CELEBRITY_NAMES,answer_label,CELEBRITY_NAMES_index_match,CELEBRITY_NAMES_click_on_answer
                if (score_CELEBRITY_NAMES==0):
                    if (len(CELEBRITY_NAMESS_WORD2)==0):
                        CELEBRITY_NAMES_canvas.itemconfigure(answer_label,text=CELEBRITY_NAMESS_ANSWER[CELEBRITY_NAMES_index_match],font=('Arial',20,'bold'),fill="green")
                        answer_button.config(state=DISABLED)
                        check_button.config(state=DISABLED)
                        CELEBRITY_NAMES_game.after(1000,CELEBRITY_NAMES_GAMEOVER)
                    elif (len(CELEBRITY_NAMESS_WORD2)!=0):
                        CELEBRITY_NAMES_canvas.itemconfigure(answer_label,text="           sorry!\nscore your score is 0",font=('Arial',13,'bold'),fill="blue")
                        print(len(CELEBRITY_NAMESS_WORD2))
                else:
                    score_CELEBRITY_NAMES-=1
                    CELEBRITY_NAMES_click_on_answer+=1
                    CELEBRITY_NAMES_canvas.itemconfigure(score_label,text="Score: "+str(score_CELEBRITY_NAMES))
                    CELEBRITY_NAMES_canvas.itemconfigure(answer_label,text=CELEBRITY_NAMESS_ANSWER[CELEBRITY_NAMES_index_match],font=('Arial',20,'bold'),fill="green")
                    answer_button.config(state=DISABLED)
                    check_button.config(state=DISABLED)
                    if len(CELEBRITY_NAMESS_WORD2)==0:
                        print(len(CELEBRITY_NAMESS_WORD2))
                        next_button.config(state=DISABLED)
                        print("game over")
                        CELEBRITY_NAMES_game.after(1000,CELEBRITY_NAMES_GAMEOVER)
                        check_button.config(state=DISABLED)
                        print("game over")
                    
            
            


            def check_answer():
                global score_CELEBRITY_NAMES,gamefile2,gamefile3,CELEBRITY_NAMES_img_no,correct_image,wrong_image

            
                
                gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
                gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
                if len(useranswer_entry.get())==0:
                    messagebox.showwarning("Warning!","              Invalid entry!\nYou have entered nothing in the box.")
                elif useranswer_entry.get()==(CELEBRITY_NAMESS_ANSWER[CELEBRITY_NAMES_index_match]).upper():
                    score_CELEBRITY_NAMES+=1
                    CELEBRITY_NAMES_canvas.itemconfigure(score_label,text="Score: "+str(score_CELEBRITY_NAMES))
                
                    CELEBRITY_NAMES_img_no=1
                    correct_image=CELEBRITY_NAMES_canvas.create_image(670,245,image=gamefile2)
                    if len(CELEBRITY_NAMESS_WORD2)==0:
                        print(len(CELEBRITY_NAMESS_WORD2))
                        next_button.config(state=DISABLED)
                        print("game over")
                        CELEBRITY_NAMES_game.after(500,CELEBRITY_NAMES_GAMEOVER)
                    
                    
                    else:
                        CELEBRITY_NAMES_game.after(500,CELEBRITY_NAMES_next_word)

                elif useranswer_entry.get()!=(str(CELEBRITY_NAMESS_ANSWER[CELEBRITY_NAMES_index_match])).upper():
                    wrong_image=CELEBRITY_NAMES_canvas.create_image(670,245,image=gamefile3)
                    CELEBRITY_NAMES_img_no=2


            
            global CELEBRITY_NAMES_game,CELEBRITY_NAMES_canvas,score_label,label,useranswer_entry,answer_label,check_button,next_button,answer_label_info,answer_button
            CELEBRITY_NAMES_game=Tk()
            CELEBRITY_NAMES_game.title("JUMBULED WORDS => CELEBRITY_NAMES")
            CELEBRITY_NAMES_game.geometry('800x533+200+100')
            CELEBRITY_NAMES_canvas=Canvas(CELEBRITY_NAMES_game,width=800,height=533,bg="red")
            CELEBRITY_NAMES_canvas.place(x=0,y=0)
            gamefile1=PhotoImage(file="images/game_jumbledwords.png")
            gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
            gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
            CELEBRITY_NAMES_canvas.create_image(0,0,image=gamefile1,anchor=NW)
            
            score_label=CELEBRITY_NAMES_canvas.create_text(720,15,text="Score: "+str(score_CELEBRITY_NAMES),font=('Arial',20,'bold'),fill="blue")
            CELEBRITY_NAMES_canvas.create_text(200,15,text="Please open \'Caps Lock\' before starting",font=('Arial',15,'bold'),fill="blue")
            useranswer_entry=Entry(CELEBRITY_NAMES_canvas,width=22,font=('Arial',23,'bold'),borderwidth=0,justify="center",fg="red")
            useranswer_entry.place(x=240,y=230)

            label=CELEBRITY_NAMES_canvas.create_text(410,180,text=CELEBRITY_NAMES_jword,font=('Arial',40,'bold'),fill="blue")
            answer_label=CELEBRITY_NAMES_canvas.create_text(702,460,text=" ",font=('Arial',13,'bold'),fill="blue")
            check_button=Button(CELEBRITY_NAMES_canvas,text="Check",width=10,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=check_answer)
            check_button.place(x=350,y=300)
            next_button=Button(CELEBRITY_NAMES_canvas,text="next",width=10,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=CELEBRITY_NAMES_next_word)
            next_button.place(x=350,y=360)
            answer_label_info=CELEBRITY_NAMES_canvas.create_text(500,520,text="For correct answer click here==>",font=('Arial',10,'bold'),fill="blue")
            answer_button=Button(CELEBRITY_NAMES_canvas,text="Correct answer",width=15,font=('Arial',15,'bold'),
                bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=answer_check)
            answer_button.place(x=620,y=494)


            CELEBRITY_NAMES_game.mainloop()
        CELEBRITY_NAMESmain()
        































    def start_game(choose):
    
        try:
            game.destroy()
        except:
            pass
        if choose == 1:
            try:
                option.destroy()
            except:
                pass
            animal_window()
            
        
        elif choose == 2:
            try:
                option.destroy()
            except:
                pass
            computer_window()
       
        elif choose == 3:
            try:
                option.destroy()
            except:
                pass
            fruit_window()
        
        elif choose == 4:
            try:
                option.destroy()
            except:
                pass
            celebrity_name()
            
     
        
    def start():
    
    
        global game
        game=Tk()
        game.title("JUMBBLED WORDS")
        game.geometry('800x533+200+100')
        game.resizable(0,0)
        g_canvas=Canvas(game,width=800,height=533,bg="red")
        g_canvas.place(x=0,y=0)
        gamefile1=PhotoImage(file="images/game_jumbledwords.png")
        gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
        gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
        g_canvas.create_image(0,0,image=gamefile1,anchor=NW)
    
    
    
        username_entry=Entry(g_canvas,width=22,font=('Arial',20,'bold'),borderwidth=0,justify="center",fg="red")
        username_entry.place(x=250,y=230)

        label=g_canvas.create_text(400,160,text="       Enter your name to save your data",font=('Arial',20,'bold'),fill="blue")
        global option_fn
        def option_fn():
            global option
            try:
                game.destroy()
            except:
                pass
            option=Tk()
            option.title("JUMBBLED WORDS")
            option.geometry('800x533+200+100')
            option.resizable(0,0)
            option_canvas=Canvas(option,width=800,height=533,bg="red")
            option_canvas.place(x=0,y=0)
            gamefile1=PhotoImage(file="images/game_jumbledwords.png")
            gamefile2=PhotoImage(file="images/correct2_jumbledwords.png")
            gamefile3=PhotoImage(file="images/wrong_jumbledwords.png")
            option_canvas.create_image(0,0,image=gamefile1,anchor=NW)
            option_canvas.itemconfigure(label,text="             Choose your topic:",font=('Arial',30,'bold'))


            btn1 = Button(text="Animals",width=14,borderwidth=0,font=('Arial',20,'bold'),bg="black",fg="green",
                activebackground="red",activeforeground="blue",cursor="hand2",command=lambda: start_game(1))
            btn1.place(x=300,y=200)
            btn2 = Button(text="Computer",width=14,borderwidth=0,font=('Arial',20,'bold'),bg="black",fg="green",
                activebackground="red",activeforeground="blue",cursor="hand2",command=lambda: start_game(2))
            btn2.place(x=300,y=260)
            btn3 = Button(text="Fruits",width=14,borderwidth=0,font=('Arial',20,'bold'),bg="black",fg="green",
                activebackground="red",activeforeground="blue",cursor="hand2",command=lambda: start_game(3))
            btn3.place(x=300,y=320)
            btn4 = Button(text="Celebrity Names",width=14,borderwidth=0,font=('Arial',20,'bold'),bg="black",fg="green",
                activebackground="red",activeforeground="blue",cursor="hand2",command=lambda: start_game(4))
            btn4.place(x=300,y=380)
            btn5 = Button(text="EXIT",width=10,borderwidth=0,font=('Arial',15,'bold'),bg="black",fg="green",
                activebackground="red",activeforeground="blue",cursor="hand2",command=main)
            btn5.place(x=400,y=480)

            option.mainloop()
        def save():
            global save_username
            save_username=str(username_entry.get()).upper()
            
            if (len(save_username)==0) or (save_username==' '):
                messagebox.showwarning('Warning',"Please enter valid username")
            else:
                print(save_username)
                
                
                g_canvas.itemconfigure(label,text="             Choose your topic:",font=('Arial',30,'bold'))
                conn = sqlite3.connect("jum.db")
                c1 = conn.cursor()
                c1.execute("""CREATE TABLE IF NOT EXISTS data(
                        p1 VARCHAR(10),
                        score1 INTEGER(10),
                        score2 INTEGER(10),
                        score3 INTEGER(10),
                        score4 INTEGER(10)
                        
                        
                        
                        );""")
                c1.execute("INSERT INTO data(p1,score1,score2,score3,score4) VALUES('"+save_username+"',0,0,0,0)")
                conn.commit()
                option_fn()
        butsave=Button(g_canvas,text="save",width=10,font=('Arial',15,'bold'),
            bg='black',fg="green",activebackground="red",activeforeground="blue",borderwidth=0,command=save)
        butsave.place(x=350,y=320)
    
        game.mainloop()





    def play():
        intro.destroy()
        start()


    def exitgame():
        quitgame=messagebox.askyesno("QUIT THE GAME","ARE YOU REALLY WANT TO QUIT THE GAME")
        if (quitgame):
            try:
                intro.destroy()
            except:
                pass
            import playstationfile
            playstationfile.next2()
    def led():
        
        
        led=Tk()
        led.title("JUMBBLED WORDS GAME LEADERBOARD")
        led.geometry('850x500+100+100')
        led.resizable(0,0)
        led.configure(bg="yellow")
        ledcanvas=Canvas(led,height=100,width=1010,bg="yellow")
        ledcanvas.pack()

        
        ledtext=ledcanvas.create_text(420,40,text="LEADERBOARD",font=('Arial',50,'bold underline'),fill="blue")
        lframe=Frame(led)
        lframe.pack(padx=20)
        tab=ttk.Treeview(lframe,columns=(1,2,3,4,5,6),show="headings",height=14)
        tab.pack(fill="both")
        tab.column(1,width=200)
        tab.column(2,width=120)
        tab.column(3,width=150)
        tab.column(4,width=100)
        tab.column(5,width=130)
        tab.column(6,width=100)
        tab.heading(1,text="PLAYER NAME")
        tab.heading(2,text="ANIMALS NAME")
        tab.heading(3,text="COMPUTER PARTS NAME")
        tab.heading(4,text="FRUIT NAMES")
        tab.heading(5,text="CELEBRITY NAMES")
        tab.heading(6,text="TOTAL SCORE")
        conn=sqlite3.connect("jum.db")
        c=conn.cursor()
        c.execute("SELECT *  FROM data")
          
        rec=c.fetchall()
        for a in rec:
            total_sc=0 
            total_sc=a[1]+a[2]+a[3]+a[4]
            tab.insert('', 'end', values=(a[0], a[1], a[2],a[3],a[4],total_sc))     
        def back1111():
            led.destroy()
        back=Button(led,text="BACK",bg="yellow",activebackground="red",fg='blue',activeforeground='blue',borderwidth=0,font=('Arial',30,'bold'),command=back1111)
        back.pack(pady=20)
        led.mainloop()
    global file1,file2,file3,file4,intro
    try:
        option.destroy()
    except:
        pass
    intro=Tk()
    intro.geometry('701x455+300+100')
    intro.title("JUMBBLED WORDS GAME")
    intro.resizable(0,0)
    c=Canvas(intro,height=450,width=701,bg="white")
    c.place(x=0,y=0)
    file1=PhotoImage(file="images/intro1_jumbledwords.png")
    file2=PhotoImage(file="images/play1_jumbledwords.png")
    file3=PhotoImage(file="images/leaderboard_jumbledwords.png")
    file4=PhotoImage(file='images/exit_jumbledwords.png')
    c.create_image(0,0,anchor=NW,image=file1)
    bplay=Button(c,image=file2,anchor=NW,bg="white",activebackground="WHITE",borderwidth=0,command=play)
    bplay.place(x=300,y=370)
    
    bleaderboard=Button(c,image=file3,bg="white",activebackground="WHITE",borderwidth=0,command=led)
    bleaderboard.place(x=100,y=370)

    bexit=Button(c,image=file4,bg="white",activebackground="WHITE",borderwidth=0,command=exitgame)
    bexit.place(x=500,y=370)
    intro.mainloop()
