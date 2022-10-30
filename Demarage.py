from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
from Stock import *
import time
import Stock

w = Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)

w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#fff')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)
progress.place(x=-10,y=235)
def bar():
    l4=Label(w,text='Loading...',fg='white',bg='#5598D1', font=('Calibri (Body)',10))
    l4.place(x=18,y=210)
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1

    w.destroy()
    Stock.marcherBleu()


Frame(w,width=427,height=241,bg='#5598D1').place(x=0,y=0)
b1=Button(w,width=10,height=1,text='DEMARRE',command=bar,border=0,fg='#5598D1',bg='white')
b1.place(x=170,y=200)


l1=Label(w,text='MARCHE',fg='white',bg='#5598D1', font=('Calibri (Body)',18,'bold'))
l1.place(x=50,y=80)

l2=Label(w,text='BLEU',fg='white',bg='#5598D1', font=('Monotype Corsiva',16))
l2.place(x=155,y=82)

l3=Label(w,text='BON PRIX',fg='white',bg='#5598D1', font=('Calibri (Body)',13))
l3.place(x=50,y=110)

w.mainloop()

