import tkinter
import sys
import random

root = tkinter.Tk()

mylist = []

with open("houkouzoku_list.txt", "r", encoding="utf-8") as fp:
    for line in fp:
        mylist.append(line.split())
        
aromatic = []
class Cmpd:
    def __init__(self, img, nam):
        self.image = img
        self.name = nam

for i in range(len(mylist)):
        cmpd = Cmpd(tkinter.PhotoImage(file=mylist[i][0]), mylist[i][1])
        aromatic.append(cmpd)

prog = 1 #問題進度を表す
score = 0 #得点をあらわす
mode = 2 #0->出題, 1->解答,得点, 2->スタート画面
total = len(aromatic) #問題数
img = tkinter.PhotoImage(file="start.png")
label1 = tkinter.Label(root,text="フラッシュ化学暗記ゲーム　芳香族化合物ver.")
label2 = tkinter.Label(root,text="SCORE: 　0　 PROGRESS:  0/{:2}".format(total))
label3 = tkinter.Label(root,image=img)
label4 = tkinter.Label(root,text="")

random.shuffle(aromatic) #化合物リストをシャッフル


def change(x, y): #x: 0->wrong, 1->next, 2->correct #y: progress
    global mode, score, prog
    
    if x==0 and mode==1:#wrong
        if prog>=total:
            score = score+0
            label2.configure(text="SCORE:{:3}  PROGRESS:{:3}/{:2}".format(score,prog,total))
            label4.configure(text="解答終了　合計{:2}問正解です".format(score))
        else:
            mode = 0
            score = score+0
            prog = prog+1
            label2.configure(text="SCORE:{:3}  PROGRESS:{:3}/{:2}".format(score,prog,total))
            label3.configure(image=aromatic[y].image)
            label4.configure(text="What is this compound's name?")
    elif x == 1: #next
        if mode==2 and y==1:
            mode = 0
            label2.configure(text="SCORE:{:3}  PROGRESS:{:3}/{:2}".format(score,prog,total))
            label3.configure(image=aromatic[y-1].image)
            label4.configure(text="What is this compound's name?")
        elif mode==0:
            mode = 1
            label4.configure(text="Answer: {:20}".format(aromatic[y-1].name))
    elif x==2 and mode==1: #correct  
        if prog>=total:
            score = score+1
            label2.configure(text="SCORE:{:3}  PROGRESS:{:3}/{:2}".format(score,prog,total))
            label4.configure(text="解答終了　合計{:2}問正解です".format(score))
        else:
            mode = 0
            score = score+1
            prog = prog+1
            label2.configure(text="SCORE:{:3}  PROGRESS:{:3}/{:2}".format(score,prog,total)) 
            label3.configure(image=aromatic[y].image)
            label4.configure(text="What is this compound's name?") 

button1 = tkinter.Button(root,text="　wrong...　",command=lambda:change(0,prog))
button2 = tkinter.Button(root,text="　 >>next　 ",command=lambda:change(1,prog))
button3 = tkinter.Button(root,text="　correct!　",command=lambda:change(2,prog))
button4 = tkinter.Button(root,text="　exit　",command=sys.exit)

label1.grid(row=0,column=0,columnspan=3,pady=5)
label2.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
label3.grid(row=1,column=1)
label4.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
button1.grid(row=4,column=0,padx=10)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2,padx=10)
button4.grid(row=5,column=1,pady=5)

root.mainloop()
